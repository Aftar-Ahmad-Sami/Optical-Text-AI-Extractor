import traceback
from flask import Blueprint, request, jsonify, abort
from .decorators import require_api_key
from services import ocr_service, pdf_service, image_service
from config.enum import ErrorMessages, SuccessMessages



bp = Blueprint('routes', __name__)

@bp.route('/')
def check_api():
    """
    Check if the API is running.

    Returns:
        str: A message indicating that the API is running.
    """
    try:
        return SuccessMessages.API_IS_RUNNING.value
    except Exception:
        return jsonify(ErrorMessages.API_IS_NOT_RUNNING.value)

@bp.route('/pdf-base64', methods=['POST'])
@require_api_key
def ocr_pdf_base64():
    """
    Extracts text from a PDF file uploaded via POST request.

    Returns:
        dict: A JSON response containing the extracted text for each page of the PDF.
    """
    try:
        pdf_base64 = request.json.get('file')
        if not pdf_base64:
            abort(400, description="No file found in request")
        images = pdf_service.pdf_to_img_base64(pdf_base64)
        response = {pg+1: ocr_service.ocr_core(img) for pg, img in enumerate(images)}
        print(response)
        return jsonify(response)
    except Exception as e:
        error_traceback = traceback.format_exc()
        return jsonify({'error': str(e), 'traceback': error_traceback})

@bp.route('/image', methods=['POST'])
@require_api_key
def ocr_image():
    """
    Extracts text from an image file uploaded via POST request.

    Returns:
        str: The extracted text from the image.
    """
    try:
        base64_image = request.json.get('file')
        if not base64_image:
            abort(400, description=ErrorMessages.NO_FILE_FOUND.value)
        image = image_service.image_processing(base64_image)
        text = ocr_service.ocr_core(image)
        return jsonify(text)
    except Exception as e:
        error_traceback = traceback.format_exc()
        return jsonify({'error': str(e), 'traceback': error_traceback})