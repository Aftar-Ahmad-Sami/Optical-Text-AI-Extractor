from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import pytesseract
from pdf2image import convert_from_path

app = Flask(__name__)
CORS(app)

@app.route('/')
def check_api():
    """
    Check if the API is running.

    Returns:
        str: A message indicating that the API is running.
    """
    return 'API is running!!!'

def pdf_to_images(pdf_file):
    """
    Convert a PDF file to a list of images.

    Args:
        pdf_file (str): The path to the PDF file.

    Returns:
        list: A list of images extracted from the PDF file.

    Raises:
        Exception: If an error occurs during the conversion process.
    """
    try:
        return convert_from_path(pdf_file)
    except Exception as e:
        return f"Error: {e}"

def perform_ocr(image):
    """
    Perform OCR (Optical Character Recognition) on an image.

    Args:
        image: The image to perform OCR on.

    Returns:
        str: The extracted text from the image.
    """
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(image, config=custom_config)
    return text

@app.route('/pdf', methods=['POST'])
def ocr_pdf():
    """
    Extracts text from a PDF file using OCR (Optical Character Recognition).

    This function receives a PDF file through a POST request and saves it to a local path.
    It then converts the PDF into a list of images and performs OCR on each image to extract the text.
    The extracted text is returned as a JSON response.

    Returns:
        dict: A JSON response containing the extracted text from each page of the PDF.

    Raises:
        Exception: If an error occurs during the OCR process.
    """
    try:
        pdf_file = request.files['file']
        pdf_path = '/home/input_pdf.pdf'
        pdf_file.save(pdf_path)
        images = pdf_to_images(pdf_path)
        response = {}
        for i, image in enumerate(images, start=1):
            response[i] = perform_ocr(image)
        return jsonify(response)
    except Exception as e:
        return f"Error: {e}"

@app.route('/image', methods=['POST'])
def ocr_image():
    """
    Perform OCR on an image file uploaded via POST request.

    Returns:
        str: The extracted text from the image.

    Raises:
        Exception: If an error occurs during the OCR process.
    """
    try:
        image_file = request.files['file']
        image_path = '/home/input_img.jpg'
        image_file.save(image_path)
        img = cv2.imread(image_path)
        text = perform_ocr(img)
        return text
    except Exception as e:
        return f"Error: {e}"
