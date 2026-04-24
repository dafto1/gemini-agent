import os 
# takes a working directory and a directory within the working directory 
# for e.g calculator working directory and inside calculator pkg directory 

def get_files_info(working_directory, directory=None) : 
    abs_working_dir = os.path.abspath(working_directory) ;  # converts relative path to absolute path 
    if directory is None : 
       # if no sub directory default to root directory     
        abs_directory = os.path.abspath(working_directory) ; 
    else : 
        abs_directory = os.path.abspath(os.path.join(working_directory, directory)) ; 
    if not abs_directory.startswith(abs_working_dir) : 
        return f'Error : {directory} is not a project directory'
    
    final_response = ""
    contents = os.listdir(abs_directory) ; 
    for content in contents:
        content_path = os.path.join(abs_directory, content)  # store once
        is_dir = os.path.isdir(content_path)
        size = os.path.getsize(content_path)
        final_response += f"- {content}: file_size={size} bytes, is_dir={is_dir}\n"  # += not =

    return final_response