import boto3
import os

# Initialize AWS Textract and S3 clients
textract_client = boto3.client("textract", region_name="us-east-1")
s3_client = boto3.client("s3")

bucket_name = "image-to-textbucket"
file_name = r"D:\image to text\img4.jpg"
s3_file_name = "img4.jpg"  # Use just the filename for S3

# Check if the file exists before uploading
if not os.path.exists(file_name):
    print(f"Error: File '{file_name}' not found.")
else:
    try:
        # Upload image to S3
        s3_client.upload_file(file_name, bucket_name, s3_file_name)
        print(f"File '{file_name}' uploaded successfully to S3.")

        # Process image with Textract
        response = textract_client.detect_document_text(
            Document={"S3Object": {"Bucket": bucket_name, "Name": s3_file_name}}
        )

        # Extract and print text
        extracted_text = "\n".join(
            [item["Text"] for item in response["Blocks"] if item["BlockType"] == "LINE"]
        )
        print("Extracted Text:\n", extracted_text)

    except Exception as e:
        print("Error:", str(e))
