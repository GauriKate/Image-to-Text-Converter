from flask import Flask, request, render_template
import requests
import os
import boto3
import json

app = Flask(__name__)

# AWS clients
textract_client = boto3.client("textract", region_name="us-east-1")
s3_client = boto3.client("s3")

bucket_name = "image-to-textbucket"
API_URL = "https://iclai77foc.execute-api.us-east-1.amazonaws.com/prod/extract-text"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            return render_template("index.html", text="No file uploaded.")

        file = request.files["file"]

        if file.filename == "":
            return render_template("index.html", text="No selected file.")

        file_name = file.filename  # Keep the original filename

        try:
            # Reset file pointer before uploading
            file.seek(0)

            # Upload file to S3
            s3_client.upload_fileobj(file, bucket_name, file_name)
            print(f"Uploaded '{file_name}' to S3 bucket '{bucket_name}'.")

            # Option 1: Using AWS Textract directly
            textract_response = textract_client.detect_document_text(
                Document={"S3Object": {"Bucket": bucket_name, "Name": file_name}}
            )
            textract_text = "\n".join(
                [item["Text"] for item in textract_response["Blocks"] if item["BlockType"] == "LINE"]
            )

            # Option 2: Using External API Gateway for text extraction
            headers = {"Content-Type": "application/json"}
            payload = json.dumps({"bucket": bucket_name, "filename": file_name})
            api_response = requests.post(API_URL, data=payload, headers=headers)

            # Initialize the final text data
            final_text = "No text extracted from both sources."

            # Handle response from the external API
            if api_response.status_code == 200:
                try:
                    # Print the raw response content for debugging
                    print("Raw API Response:", api_response.text)

                    # Ensure it's JSON
                    if 'application/json' in api_response.headers.get('Content-Type', ''):
                        json_data = api_response.json()
                        if isinstance(json_data, dict):
                            api_text = json_data.get("text", "No text extracted.")
                            final_text = api_text
                        else:
                            final_text = "Error: API response is not in the expected JSON format."
                    else:
                        final_text = "Error: API response is not JSON (wrong Content-Type)."
                except ValueError:
                    final_text = "Error: API response is not valid JSON."
            else:
                final_text = f"Error: API call failed with status code {api_response.status_code}"

            # If Textract (Option 1) succeeded, prioritize its result
            if textract_text.strip():
                final_text = textract_text

            return render_template("index.html", text=final_text)

        except Exception as e:
            return render_template("index.html", text=f"Error: {str(e)}")

    return render_template("index.html", text="")

if __name__ == "__main__":
    app.run(debug=True)
