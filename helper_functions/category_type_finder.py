import os
import magic
import requests

def get_file_category_and_type(file_path):
    if not os.path.exists(file_path):
        return "File not found."

    # Use python-magic to identify the file's MIME type based on content
    file_mime_type = magic.from_file(file_path, mime=True)

    # Use file.io API to get a more detailed file type description
    response = requests.get(f"https://file.io/{file_mime_type}")
    if response.status_code == 200:
        file_info = response.json()
        return f"{file_info['category']}/{file_info['type']}"

    return "Unknown file type."

# Example usage:
file_path = "/path/to/your/file"
result = get_file_category_and_type(file_path)
print(result)

