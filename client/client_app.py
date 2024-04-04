import requests

def upload_file(api_endpoint: str, file_path: str) -> None:
    """
    Uploads a file to a specified API endpoint.

    Parameters:
    api_endpoint (str): The API endpoint to which the file will be uploaded.
    file_path (str): The path of the file to be uploaded.

    Returns:
    None
    """
    try:
        with open(file_path, "rb") as file:
            files = {"file": file}
            response = requests.post(api_endpoint, files=files)
            response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print("File uploaded successfully. Response:", response.text)

# Usage
api_endpoint = "YOUR_API_ENDPOINT"
file_path = "PATH_OF_THE_FILE"
upload_file(api_endpoint, file_path)