import os
import sys

from dotenv import load_dotenv
from google import genai


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    if len(sys.argv) < 2:
        print("I need a prompt")
        sys.exit(1)
    prompt = sys.argv[1]

    response = client.models.generate_content(model="gemma-4-31b-it", contents=prompt)

    print(response.text)
    if response.usage_metadata:
        print(f"Prompt tokens : {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens : {response.usage_metadata.candidates_token_count}")
    else:
        print("Usage metadata not available")


if __name__ == "__main__":
    main()
