import requests
from PIL import Image
import random
import io
import os
import traceback
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
KEY = os.getenv('CLIPDROP_API_KEY')
if not KEY:
    print("API key is missing. Please set the CLIPDROP_API_KEY environment variable.")
else:
    print("API key loaded successfully.")

text_input_val = input("Enter your Prompt: ")

try:
    r = requests.post('https://clipdrop-api.co/text-to-image/v1',
      files = {
          'prompt': (None, str(text_input_val), 'text/plain')
      },
      headers = { 'x-api-key': KEY }
    )
    r.raise_for_status()
    if r.ok:
        image = Image.open(io.BytesIO(r.content))
        filename_depth = f"{random.randint(0, 1000)}_Depth.jpg"
        image.save(filename_depth)
        print(f"Image saved as {filename_depth}")
    else:
        r.raise_for_status()
except Exception as e:
    print("An error occurred:", e)
    traceback.print_exc()
