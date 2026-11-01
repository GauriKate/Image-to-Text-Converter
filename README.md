
# Image-to-Text Converter | AWS-Based Text Extraction

A web-based OCR application that allows users to upload images and extract the text contained in them. The application uses Amazon Textract for text extraction and integrates AWS services for image storage and processing.

**Key Features**
- Upload images through a Flask-based web interface.
- Store uploaded images in an Amazon S3 bucket.
- Extract text from images using Amazon Textract.
- Use Python and Boto3 to interact with AWS services.
- Integrate AWS Lambda and Amazon API Gateway into the processing workflow.
- Display the extracted text through the application.

**Technologies Used**
- Backend: Python, Flask
- Cloud Storage: Amazon S3
- OCR: Amazon Textract
- AWS Integration: Boto3, AWS Lambda, Amazon API Gateway

**How It Works**
1. The user uploads an image through the Flask web interface.
2. The application uploads the image to the configured Amazon S3 bucket.
3. Amazon Textract processes the image and extracts its text.
4. AWS Lambda and API Gateway handle the configured backend workflow.
5. The extracted text is returned to the application and displayed to the user.

**Getting Started**

**Prerequisites**
- Python installed
- Git
- An AWS account
- AWS credentials with the required permissions
- Configured S3 bucket and AWS services

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/GauriKate/Image-to-Text-Converter.git
```

### 2. Navigate to the Project Folder

```bash
cd Image-to-Text-Converter
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```powershell
venv\Scripts\activate
```

### 5. Install Dependencies

If a requirements.txt file is available:

```bash
pip install -r requirements.txt
```

### 6. Configure AWS

Configure your AWS credentials securely using the AWS CLI or environment variables.

Make sure your AWS account has the required permissions for S3 and Textract, along with Lambda and API Gateway if used in your workflow.

**Important:** Never upload AWS access keys, secret keys, or other credentials to GitHub.

## Running the Application

If your Flask entry-point file is app.py, run:

```bash
python app.py
```

Open the local URL shown in the terminal.

**My Contribution**

Worked on image uploading and storage using Amazon S3, integrating Amazon Textract for text extraction, using Boto3 to interact with AWS services, and connecting AWS Lambda and API Gateway within the application workflow. Also worked on the Flask interface for uploading images and displaying extracted text.

**Future Improvements**
- Support additional image formats.
- Improve error handling for unclear or unsupported images.
- Add options to download or copy extracted text.
- Add authentication and secure upload controls.
