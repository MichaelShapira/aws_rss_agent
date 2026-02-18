import boto3
import json
import uuid
import argparse
from botocore.config import Config


def main():
    parser = argparse.ArgumentParser(description="Invoke an AgentCore runtime agent")
    parser.add_argument("--arn", required=True, help="Agent runtime ARN")
    parser.add_argument("--prompt", default="Amazon Bedrock", help="Prompt to send (default: 'Amazon Bedrock')")
    parser.add_argument("--region", default="us-east-1", help="AWS region (default: us-east-1)")
    parser.add_argument("--session-id", default=None, help="Session ID (default: auto-generated)")
    args = parser.parse_args()

    client = boto3.client(
        'bedrock-agentcore',
        region_name=args.region,
        config=Config(
            read_timeout=600,
            connect_timeout=60,
            retries={'max_attempts': 0}
        )
    )

    payload = json.dumps({"prompt": args.prompt}).encode()
    session_id = args.session_id or (str(uuid.uuid4()) + "-" + str(uuid.uuid4())[:8])

    response = client.invoke_agent_runtime(
        agentRuntimeArn=args.arn,
        runtimeSessionId=session_id,
        payload=payload
    )

    content_type = response.get("contentType", "")

    if "text/event-stream" in content_type:
        content = []
        for line in response["response"].iter_lines(chunk_size=10):
            if line:
                line = line.decode("utf-8")
                if line.startswith("data: "):
                    line = line[6:]
                    print(line)
                    content.append(line)
        print("\nComplete response:", "\n".join(content))

    elif content_type == "application/json":
        raw_bytes = b""
        for chunk in response.get("response", []):
            raw_bytes += chunk
        print(json.loads(raw_bytes.decode('utf-8')))

    else:
        print("Response:", response)


if __name__ == "__main__":
    main()
