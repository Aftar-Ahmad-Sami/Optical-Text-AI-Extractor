import pytesseract
from config.enum import ErrorMessages

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
    try:
        custom_config = r'-l eng --oem 3 --psm 6'
        return pytesseract.image_to_string(file, config=custom_config)
    except Exception:
        return ErrorMessages.OCR_ERROR.value
