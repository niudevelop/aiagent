import os
MAX_CHARS=10000
def get_file_content(working_directory, file_path):
    try:
        abs_path = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_path, file_path))
        valid_target_file = os.path.commonpath([abs_path, target_file]) == abs_path
        if valid_target_file == False:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if os.path.isfile(target_file) == False:
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(target_file, "r") as f:
            file_content_string = f.read(MAX_CHARS)
        if len(file_content_string) >= MAX_CHARS:
            file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'
        return file_content_string
    except Exception as error:
        return f"Error: {error}"