from strands import Agent
from strands.models import BedrockModel
from mcp import stdio_client, StdioServerParameters
from strands.tools.mcp import MCPClient
from strands_tools import http_request,think,current_time
import logging
import json
import argparse
from bedrock_agentcore.runtime import BedrockAgentCoreApp
from botocore.config import Config

# Enables Strands debug log level
logging.getLogger("strands").setLevel(logging.INFO)

# Sets the logging format and streams logs to stderr
logging.basicConfig(
    format="%(levelname)s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler()]
)

app = BedrockAgentCoreApp()

# Create an agent with MCP tools
all_tools = [http_request,
             current_time
            ]

bedrock_config = Config(
    read_timeout=600,        # 10 minutes
    connect_timeout=60,
    retries={'max_attempts': 5}
)

model = BedrockModel(
    model_id="us.anthropic.claude-sonnet-4-6",
    boto_client_config=bedrock_config
)

prompt="""
You are an expert at analyzing RSS feeds and extracting relevant technical announcements. Your task is to process AWS's "What's New" RSS feed and identify announcements related to a specific topic published on a specific date.

**TASK**

Fetch and Parse: Retrieve the AWS RSS feed from https://aws.amazon.com/about-aws/whats-new/recent/feed/
Filter by Date: Only include items published on specific dates
Filter by Topic: Only include items related to [TOPIC_PLACEHOLDER] (to be specified by user)
Analyze Content: For each relevant item (appears in <item> element), extract detailed information from <description> element
Generate Output: Create a well-formatted MARKUP summary

**PROCESSING STEPS**
Follow this exact sequence:

Fetch RSS Feed: Use http_requests tool to retrieve the XML content
Parse XML: Extract items matching the RSS schema structure
Date Filter: Keep only items with pubDate matching dates specified in the request later.
Topic Filter: Analyze title, description, and category fields for topic relevance
Content Analysis:

If requested topic was found also check for additional content related to title element. This information can be found in AWS Documentation, 
Ask  AWS Documentation to return the summary of the topic. Don't search in documentation if to related topics were found.

**GENERATE MARKUP OUTPUT** 
Create formatted summary with all relevant links

RSS Feed Schema Reference
The feed contains these key elements for each item:

title: Announcement title
description: Brief summary
pubDate: Publication date
category: Topic category
link: Full announcement URL
author: Publisher

**OUTPUT FORMAT**
For each relevant announcement, provide:
Title: [Exact title from RSS item]
Short Description: [1-2 sentence summary from RSS description field]
Long Description: [comprehensive summary including:

Key features and benefits
Technical details
AWS Documentation content summary if you can find it.
All relevant links like (Blogs, DOcumentation Links, Github samples)

**SUCCESS CRITERIA**
Only include items from specified dates
Only include items clearly related to the specified topic
Include AWS documentation content analysis if possible
Maintain technical accuracy
Use professional, clear language
Generate well-formatted MARKUP output

**IMPORTANT**

Stop after generating the MARKUP output - no follow-up questions needed
Focus on accuracy over speed
Include all relevant links in the MARKUP output
Ensure AWS Documentation content is properly summarized.
"""


def create_mcp_client():
    """Create a fresh MCP client for each invocation to avoid session conflicts."""
    return MCPClient(lambda: stdio_client(
        StdioServerParameters(
            command="uvx",
            args=["awslabs.aws-documentation-mcp-server@latest"],
            env={
                "FASTMCP_LOG_LEVEL": "ERROR",
                "AWS_DOCUMENTATION_PARTITION": "aws"
            },
        )
    ))


@app.entrypoint
def strands_agent_bedrock(payload):
    """
    Invoke the agent with a payload
    """
    user_input = payload.get("prompt")

    mcp_client = create_mcp_client()
    with mcp_client:
        # Collect MCP tools inside the session context
        mcp_tools = mcp_client.list_tools_sync()
        logging.info(f"Collected {len(mcp_tools)} MCP tools")

        # Create agent with all tools (built-in + MCP)
        agent = Agent(
            tools=all_tools + list(mcp_tools),
            model=model,
            system_prompt=prompt
        )

        response = agent(f"""
                        1. Process the feed for the following topic: {user_input} and generate the output for topics published today or yerturday or two days ago only. 
                        2. Set relevant http headers for http_request tool to fetch RSS XML content. 
                        3. After generating the output, format it as well formatted and well syled MARKUP .
                        4. Done ask any follow up questions.

                        """)
        return response.message['content'][0]['text']

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AWS RSS Feed Agent")
    parser.add_argument("--prompt", type=str, help="Run standalone with this prompt (no AgentCore)")
    args = parser.parse_args()

    if args.prompt:
        # Standalone mode — run directly without AgentCore
        result = strands_agent_bedrock({"prompt": args.prompt})
        print(result)
    else:
        # AgentCore mode — start the HTTP server
        app.run()
