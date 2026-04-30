import os  

def get_files_info(working_directory : str , directory = ".") : 
    abs_working_dir =  os.path.abspath(working_directory)  
    abs_directory = " " ; 
    if directory is None : 
        abs_directory = os.path.abspath(working_directory)  
    else : 
        abs_directory = os.path.abspath(os.path.join(working_directory , directory)) 
    
    if not abs_directory.startswith(abs_working_dir) : 
        return f"Error : {directory} is not in the working directory" 

    contents = os.listdir(abs_directory) 
    final_response = " " ; 

    for content in contents :  
        content_path = os.path.join(abs_directory , content) 
        is_dir = os.path.isdir(os.path.join(content_path))
        size = os.path.getsize(content_path) 
        final_response += f"{content} : file_size = {size} bytes, is_dir = {is_dir}\n"

    return final_response 