import os 
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types 
from functions.get_files_info import get_files_info
def main()  :
    load_dotenv() 
    api_key = os.environ.get("GEMINI_API_KEY") 


    #create a client 
    client = genai.Client(api_key=api_key)
    
    if(len(sys.argv)< 2) : 
        print("Please provide a prompt") 
        sys.exit(1) 
    
    verbose_flag = False
    if(len(sys.argv) == 3 and sys.argv[2] == "--verbose") : 
         verbose_flag = True 
    prompt = sys.argv[1] 

    messages = [
        types.Content(role = "user" , parts = [types.Part(text=prompt  )])
    ]
    response = client.models.generate_content(
        model = "gemma-4-26b-a4b-it", 
        contents = prompt 
    )

    print(response.text)  ;

    if(verbose_flag) : 
        print(f"User prompt : ", {prompt})
        print(f"Prompt tokens : {response.usage_metadata.prompt_token_count} " ) 
        print(f"Response tokens : {response.usage_metadata.candidates_token_count}")
        
print(get_files_info("calculator", "pkg"))