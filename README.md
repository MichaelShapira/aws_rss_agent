# AWS RSS Feed Agent

An AI agent that fetches the [AWS "What's New" RSS feed](https://aws.amazon.com/about-aws/whats-new/recent/feed/), filters announcements by topic and date, and enriches them with content from AWS Documentation. Built with [Strands Agents SDK](https://github.com/strands-agents/sdk-python) and deployable to [Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/).

## What It Does

Given a topic (e.g., "Amazon Bedrock"), the agent:

1. Fetches the AWS What's New RSS feed
2. Filters items published in the last few days
3. Matches items related to the requested topic
4. Looks up related AWS Documentation for additional context
5. Returns a well-formatted Markdown summary with links

## Tools

The agent uses the following tools:

| Tool | Source | Purpose |
|------|--------|---------|
| `http_request` | [strands-agents-tools](https://github.com/strands-agents/tools-python) | Fetch the RSS feed XML |
| `current_time` | [strands-agents-tools](https://github.com/strands-agents/tools-python) | Determine today's date for filtering |
| `aws-documentation-mcp-server` | [MCP Server](https://github.com/awslabs/aws-documentation-mcp-server) | Search and retrieve AWS documentation |

## Model

The agent uses **Claude Sonnet 4** (`us.anthropic.claude-sonnet-4-6`) via Amazon Bedrock.

## Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/getting-started/installation/) (for running the MCP server via `uvx`)
- AWS credentials configured with access to Amazon Bedrock
- [Finch](https://runfinch.com/) or Docker (for container builds and AgentCore deployment)

## Setup

```bash
# Clone the repository
git clone https://github.com/MichaelShapira/aws_rss_agent.git
cd aws_rss_agent

# Create a virtual environment and install dependencies
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running Locally

### As a standalone Python script

Run the agent directly without AgentCore:

```bash
python rss.py --prompt "Amazon Bedrock"
```

This creates the agent, connects to the MCP server, processes the request, and prints the Markdown output to stdout. You can redirect it to a file:

```bash
python rss.py --prompt "Amazon S3" > output.md
```

### With AgentCore local dev server

You can also run it as an AgentCore-compatible service with hot reloading:

```bash
agentcore dev
```

This starts a local HTTP server at `http://localhost:8080/invocations` with hot reloading.

In a separate terminal, invoke it:

```bash
agentcore invoke --dev '{"prompt": "Amazon Bedrock"}'
```

## Deploying to Amazon Bedrock AgentCore

### AWS Credentials

Before deploying or invoking the agent on AgentCore, you need valid AWS credentials configured. The credentials must have permissions for:

- **Amazon Bedrock** — to invoke the foundation model
- **Amazon ECR** — to push the container image
- **Amazon Bedrock AgentCore** — to create/update the runtime and invoke the agent

Make sure your credentials are set via one of:

```bash
# Option 1: AWS CLI profile
aws configure

# Option 2: Environment variables
export AWS_ACCESS_KEY_ID=<your-key>
export AWS_SECRET_ACCESS_KEY=<your-secret>
export AWS_DEFAULT_REGION=us-east-1

# Option 3: AWS SSO
aws sso login --profile <your-profile>
```

### Deploy

The `deploy.py` script handles the full deployment lifecycle — configuring the agent, building the container, pushing to ECR, and creating/updating the AgentCore runtime endpoint:

```bash
python deploy.py
```

This will:
1. Configure the agent with the AgentCore starter toolkit
2. Build the Docker container image
3. Push it to Amazon ECR
4. Create or update the AgentCore runtime
5. Wait until the endpoint is `READY`

### Invoke the deployed agent

Once the endpoint is ready, use `execute_agent.py` to call it:

```bash
python execute_agent.py --arn "arn:aws:bedrock-agentcore:us-east-1:123456789012:runtime/my-agent-id"
```

You can also customize the prompt and region:

```bash
python execute_agent.py \
  --arn "arn:aws:bedrock-agentcore:us-east-1:123456789012:runtime/my-agent-id" \
  --prompt "Amazon S3" \
  --region us-west-2
```

## Example Output

See [sample.md](sample.md) for an example of the agent's output when prompted with "Amazon Bedrock". The agent found recent announcements, enriched them with AWS Documentation summaries, and formatted everything as Markdown.

## Project Structure

```
├── rss.py              # Agent implementation (entrypoint)
├── deploy.py           # Deployment script for AgentCore
├── execute_agent.py    # Client script to invoke the deployed agent
├── sample.md           # Example agent output
├── requirements.txt    # Python dependencies
├── Dockerfile          # Container image for AgentCore runtime
├── .dockerignore       # Files excluded from the container build
└── .bedrock_agentcore.yaml  # AgentCore configuration (generated, git-ignored)
```

## How It Works

The agent is wrapped with `BedrockAgentCoreApp` which provides the HTTP server interface that AgentCore expects. On each invocation:

1. A fresh MCP client is created to connect to the AWS Documentation MCP server (via `uvx`)
2. MCP tools are collected and combined with the built-in tools (`http_request`, `current_time`)
3. A Strands `Agent` is created with all tools and the system prompt
4. The agent processes the user's topic request and returns formatted Markdown
