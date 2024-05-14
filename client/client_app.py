import requests

def upload_file(api_endpoint: str, file_path: str, api_key: str) -> None:
    """
    Uploads a file to a specified API endpoint.

    Parameters:
    api_endpoint (str): The API endpoint to which the file will be uploaded.
    file_path (str): The path of the file to be uploaded.
    api_key (str): The API key for authenticating the request.

    Returns:
    None
    """
    try:
        with open(file_path, "rb") as file:
            files = {"file": file}
            headers = {"x-api-key": api_key}
            response = requests.post(api_endpoint, files=files, headers=headers)
            response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        break
    except Exception as err:
        print(f'Other error occurred: {err}')
        break
    print("File uploaded successfully. Response:", response.text)

# Usage
api_endpoint = "YOUR_API_ENDPOINT"
file_path = "PATH_OF_THE_FILE"
api_key = 'API_KEY'
upload_file(api_endpoint, file_path, api_key)
