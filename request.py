import requests
import json

# API Gateway URL
url = "https://iclai77foc.execute-api.us-east-1.amazonaws.com/prod/extract-text"

# Data to send to Lambda
data = {
    "bucket": "image-to-textbucket",
    "filename": "img4.jpg"
}

# Headers
headers = {
    "Content-Type": "application/json"
}

# POST request
response = requests.post(url, data=json.dumps(data), headers=headers)

# Show status code
print(f"Status Code: {response.status_code}")

# Handle and pretty-print response
try:
    result = json.loads(response.text)

    # The body may still be a JSON string, so parse again
    if isinstance(result.get("body"), str):
        body = json.loads(result["body"])
    else:
        body = result["body"]

    # Print extracted text
    extracted_text = body.get("text", "")
    print("\n--- Extracted Text ---\n")
    print(extracted_text)

    # Optional: Save to file
    with open("output_text.txt", "w", encoding="utf-8") as file:
        file.write(extracted_text)

    print("\nText saved to output_text.txt ✅")

except Exception as e:
    print("Error parsing response:", e)
