import os
import shutil

UPLOAD_DIRECTORY = "./data/"
EXTRACTED_TEXT_STORAGE = {}

os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

def save_file(file):
    """Save the uploaded file to the local storage."""
    file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return file_path

def save_extracted_text(file_name, text):
    """Save extracted text in memory."""
    print(f"Saving extracted text for file: {file_name}")
    EXTRACTED_TEXT_STORAGE[file_name] = text

def get_extracted_text(file_name):
    """Retrieve extracted text for a file."""
    text = EXTRACTED_TEXT_STORAGE.get(file_name)
    if not text:
        print(f"No extracted text found for file: {file_name}")
    return text

