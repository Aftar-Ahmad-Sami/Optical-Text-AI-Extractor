import os
from dotenv import load_dotenv
import pytesseract

def get_base_dir():
    """
    Get the absolute path of the base directory.

    Returns:
        str: The absolute path of the base directory.
    """
    return os.path.abspath(os.path.dirname(__file__))

def get_env_path():
    """
    Get the path of the environment file.

    Returns:
        str: The path of the environment file.
    """
    base_dir = get_base_dir()
    return os.path.join(base_dir, '.env')

def load_environment_variables():
    """
    Load the environment variables from the .env file.
    """
    env_path = get_env_path()
    load_dotenv(env_path)

# Define the base directory and the path of the environment file
BASE_DIR = get_base_dir()
ENV_PATH = get_env_path()

# Load the environment variables from the .env file
load_environment_variables()

# Get the API key from the environment variables
API_KEY = os.getenv("API_KEY")

poppler_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils','poppler-24.02.0', 'Library', 'bin'))
pytesseract.pytesseract.tesseract_cmd = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils','Tesseract-OCR','tesseract.exe'))