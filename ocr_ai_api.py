from functools import wraps
from flask_cors import CORS
from flask import Flask, request, jsonify, abort
import cv2
import pytesseract
from pdf2image import convert_from_path
import os
import uuid
from dotenv import load_dotenv

# Define the base directory and the path of the environment file
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
ENV_PATH = os.path.join(BASE_DIR, '.env')

# Load the environment variables from the .env file
load_dotenv(ENV_PATH)

# Initialize the Flask application and enable CORS
app = Flask(__name__)
CORS(app)

# Get the API key from the environment variables
API_KEY = os.getenv("API_KEY")




@app.route('/')
def check_api():
    """
    Check if the API is running.

    Returns:
        str: A message indicating that the API is running.
    """
    return 'API is running!!!'





def require_api_key(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        """
        Decorator function to require API key for accessing a view function.

        Args:
            view_function (function): The view function to be decorated.

        Returns:
            The decorated view function.

        Raises:
            HTTPException: If the API key is missing or incorrect.
        """
        if request.headers.get('x-api-key') != API_KEY:
            abort(401, description="Unauthorized access")
        return view_function(*args, **kwargs)
    return decorated_function





def pdf_to_img(pdf_file):
    """
    Convert a PDF file to a list of images.

    Args:
        pdf_file (str): The path to the PDF file.

    Returns:
        list: A list of images converted from the PDF file.

    Raises:
        HTTPException: If there is an error in converting the PDF to image.
    """
    try:
        return convert_from_path(pdf_file)
    except Exception:
        abort(500, description="Error in converting PDF to image")





def ocr_core(file):
    """
    Perform OCR (Optical Character Recognition) on an image file.

    Args:
        file: The image file to perform OCR on.

    Returns:
        str: The extracted text from the image.

    Raises:
        Exception: If there is an error in performing OCR.
    """
    custom_config = r'--oem 3 --psm 6'
    return pytesseract.image_to_string(file, config=custom_config)





@app.route('/pdf', methods=['POST'])
@require_api_key
def ocr_pdf():
    """
    Extracts text from a PDF file uploaded via POST request.

    Returns:
        dict: A JSON response containing the extracted text for each page of the PDF.
    """
    pdf_file = request.files.get('file')
    if not pdf_file:
        abort(400, description="No file found in request")
    unique_filename = str(uuid.uuid4())
    pdf_path = os.path.join(BASE_DIR, 'uploads', 'pdf', f'{unique_filename}.pdf')
    pdf_file.save(pdf_path)
    images = pdf_to_img(pdf_path)
    response = {pg+1: ocr_core(img) for pg, img in enumerate(images)}
    os.remove(pdf_path)
    return jsonify(response)




@app.route('/image', methods=['POST'])
@require_api_key
def ocr_image():
    """
    Extracts text from an image file uploaded via POST request.

    Returns:
        str: The extracted text from the image.
    """
    image_file = request.files.get('file')
    if not image_file:
        abort(400, description="No file found in request")
    unique_filename = str(uuid.uuid4())
    image_path = os.path.join(BASE_DIR, 'uploads', 'image', f'{unique_filename}.jpg')
    image_file.save(image_path)
    img = cv2.imread(image_path)
    text = ocr_core(img)
    os.remove(image_path)
    return text