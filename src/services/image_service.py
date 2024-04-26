from base64 import b64decode
import cv2
import numpy as np
from config.enum import ErrorMessages

def image_processing(base64_image):
    """
    Process the base64 encoded image.

    Args:
        base64_image (str): The base64 encoded image.

    Returns:
        numpy.ndarray: The processed image as a numpy array.

    Raises:
        str: If there is an error during image processing.
    """
    try:
        # Decode the base64 image
        image_data = b64decode(base64_image)
        
        # Convert the decoded image data into a numpy array
        nparr = np.frombuffer(image_data, np.uint8)

        # Convert numpy array to image
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        return img_np
    except Exception:
        return ErrorMessages.IMAGE_PROCESSING_ERROR.value
