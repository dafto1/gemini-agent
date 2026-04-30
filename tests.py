from functions.get_files_info import get_files_info 
from functions.get_file_content import get_file_content 
def main() : 
    working_dir = "calculator" 
    print(get_file_content(working_dir ,"lorem.txt")) 

main()