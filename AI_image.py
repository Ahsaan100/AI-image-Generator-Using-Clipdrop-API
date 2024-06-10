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
  headers = { 'x-api-key': "5b595a43bed99e94a779fe681176ca93631c0bb3ae4a4a689c148f8762adc29bc9b0aa7a8dc60f93382998550747682f"}
)
if (r.ok):
    image = Image.open(io.BytesIO(r.content))
    filename_depth = f"{random.randint(0, 1000)}_Depth.jpg"
    image.save(filename_depth)
else:
    r.raise_for_status()