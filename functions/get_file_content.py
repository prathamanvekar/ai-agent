import os
from functions.config import MAX_CHARS

def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_file_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:

        with open(target_file_path, "r") as f:
            full_content = f.read()
            file_content_string = full_content[:MAX_CHARS]
            if len(full_content) > MAX_CHARS:
                file_content_string += f"[...File {file_path} truncated at {MAX_CHARS} characters]"
        return file_content_string
    except Exception as e:
        return f"Error reading files: {e}"

