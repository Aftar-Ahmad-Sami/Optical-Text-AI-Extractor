# enum.py
from enum import Enum

class ErrorMessages(Enum):
    """Enum class for error messages."""
    PDF_CONVERSION_ERROR = "Error in converting PDF to image"
    TESSERACT_NOT_FOUND = "Tesseract is not installed or it's not in your PATH"
    NO_FILE_FOUND = "No file found in request"
    OCR_ERROR = "Error in performing OCR"
    IMAGE_PROCESSING_ERROR = "Error in processing image"
    API_IS_NOT_RUNNING = "API is not running"
    SERVER_IS_NOT_RUNNING = "Server is not running"

class SuccessMessages(Enum):
    API_IS_RUNNING = "API is running!!!"
    SERVER_IS_RUNNING = "Server is running!!!"