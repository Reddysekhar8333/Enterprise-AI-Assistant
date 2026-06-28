import json
import boto3

client = boto3.client(
    "bedrock-runtime",
    region_name="us-east-1"
)

MODEL_ID = "openai.gpt-oss-120b-1:0"


def generate_answer(question, context):

    prompt = f"""
        You are an enterprise knowledge assistant.

        Answer ONLY from the provided context.

        If the answer is not available in the context,
        say "I could not find the answer in the provided documents."

        Context:
        {context}

        Question:
        {question}
        """

    body = {
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "max_completion_tokens": 1000
    }
    response = client.invoke_model(
        modelId=MODEL_ID,
        body=json.dumps(body)
    )
    response_body = json.loads(
        response["body"].read()
    )
    print(response_body)

    content = response_body["choices"][0]["message"]["content"]
    if "</reasoning>" in content:
        content = content.split(
            "</reasoning>"
        )[-1].strip()

    return content
