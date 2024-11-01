import zipfile
import os


# Print the current working directory
print("Current Working Directory:", os.getcwd())

def unzip_file(zip_file_path, extract_to_folder):
    """Unzips a given zip file into the specified directory."""
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to_folder)
    print(f"Extracted {zip_file_path} to {extract_to_folder}")

# Use an absolute path to the zip file
zip_file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw', 'Handwriting.zip')
extract_to_folder = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed')  # Adjust accordingly

unzip_file(zip_file_path, extract_to_folder)


