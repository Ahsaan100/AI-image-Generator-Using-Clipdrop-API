import requests
from PIL import Image
import random
import io
import os
import traceback


text_input_val = input("Enter your Prompt: ")

r = requests.post('https://clipdrop-api.co/text-to-image/v1',
  files = {
      'prompt': (None, str(text_input_val), 'text/plain')
  },
  headers = { 'x-api-key': KEY}
)
if (r.ok):
    image = Image.open(io.BytesIO(r.content))
    filename_depth = f"{random.randint(0, 1000)}_Depth.jpg"
    image.save(filename_depth)
else:
    r.raise_for_status()
