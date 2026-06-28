import boto3
import os

s3_client = boto3.client(
    "s3",
    region_name=os.getenv("AWS_REGION")
)
BUCKET_NAME = os.getenv(
    "S3_BUCKET_NAME"
)


def upload_file_to_s3(
    local_path,
    s3_key
    ):
    s3_client.upload_file(
        local_path,
        BUCKET_NAME,
        s3_key
    )
    return (
        f"s3://{BUCKET_NAME}/{s3_key}"
    )