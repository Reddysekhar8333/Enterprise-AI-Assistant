import json
import boto3

client = boto3.client(
    "bedrock-runtime",
    region_name="us-east-1"
)

response = client.invoke_model(
    modelId="amazon.titan-embed-text-v2:0",
    body=json.dumps({
        "inputText": "What is MongoDB?"
    })
)

body = json.loads(
    response["body"].read()
)

embedding = body["embedding"]

print(type(embedding))
print(len(embedding))
