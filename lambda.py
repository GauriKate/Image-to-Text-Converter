import json
import boto3

s3_client = boto3.client("s3")
textract_client = boto3.client("textract")

def lambda_handler(event, context):
    try:
        print("EVENT:", json.dumps(event))  # Debugging output

        # Handle both direct and proxy integrations
        if "body" in event:
            body = json.loads(event["body"]) if isinstance(event["body"], str) else event["body"]
        else:
            body = event  # In case it's directly passed

        bucket_name = body["bucket"]
        file_name = body["filename"]

        response = textract_client.detect_document_text(
            Document={"S3Object": {"Bucket": bucket_name, "Name": file_name}}
        )

        extracted_text = "\n".join(
            [item["Text"] for item in response["Blocks"] if item["BlockType"] == "LINE"]
        )

        return {
            "statusCode": 200,
            "body": json.dumps({"text": extracted_text})
        }

    except Exception as e:
        print("ERROR:", str(e))
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
