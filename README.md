# Optical-Text-AI-Extractor

This Python application is a RESTful API built using Flask. It provides Optical Character Recognition (OCR) services, allowing users to extract text from PDF files and images. The OCR functionality is implemented using the pytesseract library, which is a Python wrapper for Google's Tesseract-OCR Engine, and OpenCV (cv2) for image processing.

OpenCV (Open Source Computer Vision Library) is an open-source computer vision and machine learning software library. OpenCV was built to provide a common infrastructure for computer vision applications and to accelerate the use of machine perception in commercial products. It has C++, Python, Java and MATLAB interfaces and supports Windows, Linux, Android and Mac OS.

Tesseract is an open-source OCR engine that uses machine learning to recognize and read text in various languages from images and PDF files. It was initially developed by HP and then open-sourced in 2005. Google has been sponsoring the project since 2006, and it's currently considered one of the most accurate open-source OCR engines available. Tesseract supports a wide variety of image formats and can recognize more than 100 languages out of the box.

The pdf2image library is used to convert PDF files into images for OCR processing.

## Getting Started

### Prerequisites

To run this application, you will need to have the following installed:

- Python 3
- Flask
- Flask-CORS
- OpenCV (cv2)
- pytesseract
- pdf2image

You can install these using pip:

```bash
pip install flask flask_cors opencv-python pytesseract pdf2image
```

### Running the Application

To run the application, navigate to the directory containing the Python script and run the following command:

```bash
python ocr_ai_api.py
```

The application will start and listen for HTTP requests on port 5000.

## Key Functions

- `check_api()`: This function is mapped to the root URL ("/") and returns a message indicating that the API is running.

- `require_api_key(view_function)`: This function is a decorator that checks if the API key in the request header matches the one stored in the environment variables. If not, it aborts the request with a 401 error.

- `pdf_to_img(pdf_file)`: This function takes a path to a PDF file as input and returns a list of images extracted from the PDF file.

- `ocr_core(file)`: This function takes an image as input and uses the Tesseract-OCR Engine to extract and return the text from the image.

- `ocr_pdf()`: This function is mapped to the "/pdf" URL and handles POST requests. It receives a PDF file, saves it to a local path, converts the PDF into a list of images, performs OCR on each image using the Tesseract-OCR Engine, and returns the extracted text as a JSON response.

- `ocr_image()`: This function is mapped to the "/image" URL and handles POST requests. It receives an image file, saves it to a local path, performs OCR on the image using the Tesseract-OCR Engine, and returns the extracted text.

## Example Usage

To extract text from a PDF file, send a POST request to the "/pdf" URL with the PDF file attached. The response will be a JSON object containing the extracted text from each page of the PDF.

To extract text from an image, send a POST request to the "/image" URL with the image file attached. The response will be the extracted text from the image.

## Security

The application uses an API key for authentication. The API key is stored in an environment variable and is required in the header of every request. Unauthorized requests will be rejected with a 401 error.
