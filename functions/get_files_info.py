import os

def get_files_info(working_directory, directory="."):
    try:
        abs_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_path, directory))
        valid_target_dir = os.path.commonpath([abs_path, target_dir]) == abs_path
        if valid_target_dir == False:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        
        contents = os.listdir(target_dir)
        result = ""
        for content in contents:
            content_path = os.path.join(target_dir, content)
            result += f"- {content}: file_size={os.path.getsize(content_path)} bytes, is_dir={"True" if os.path.isdir(content_path) else "False"}\n"
        return result
    except Exception as error:
        return f"Error: {error}"
