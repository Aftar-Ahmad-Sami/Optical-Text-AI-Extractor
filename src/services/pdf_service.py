from pdf2image import convert_from_bytes
from flask import abort
import base64
import io
from config.settings import poppler_path
from config.enum import ErrorMessages

def pdf_to_img_base64(pdf_base64):
    """
    Convert a PDF file to a list of images.

    Args:
        pdf_base64 (str): The base64 encoded string representation of the PDF file.

    Returns:
        list: A list of images converted from the PDF file.

    Raises:
        HTTPException: If there is an error in converting the PDF to image.
    """
    try:
        pdf_bytes = base64.b64decode(pdf_base64)
        pdf_file = io.BytesIO(pdf_bytes)
        return convert_from_bytes(pdf_file.read(), poppler_path=poppler_path)
    except Exception:
        abort(500, description=ErrorMessages.PDF_CONVERSION_ERROR.value)