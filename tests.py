from functions.get_files_info import get_files_info 
from functions.get_file_content import get_file_content 
from functions.write_file import write_file
def main() : 
    working_dir = "calculator" 
   
    write_file("calculator", "lorem.txt", "wait, this is not lorem ipsum")  
    print(get_file_content(working_dir ,"lorem.txt")) 
    write_file("calculator", "pkg/tmp/new.txt", "wait this is a new lorem ipsum") 
main()