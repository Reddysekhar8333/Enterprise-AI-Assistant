import json
import boto3

bedrock_runtime = boto3.client(
    "bedrock-runtime",
    region_name="us-east-1"
)

MODEL_ID = "amazon.titan-embed-text-v2:0"


def generate_embedding(text: str):
    response = bedrock_runtime.invoke_model(
        modelId=MODEL_ID,
        body=json.dumps({
            "inputText": text
        })
    )
    response_body = json.loads(
        response["body"].read()
    )
    return response_body["embedding"]
