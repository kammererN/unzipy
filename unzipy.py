
import zipfile

# CONSTANTS
path_to_zip_file = ""
output_directory = "./"


with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
    zip_ref.extractall(output_directory)

