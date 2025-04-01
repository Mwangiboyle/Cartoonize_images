import requests
import base64
from PIL import Image
from io import BytesIO
import os

# 1. Upload image via API
url = "http://localhost:8000/upload"
image_path = "image.png"  # Your input image
output_path = "cartoon_output.png"  # Output file name

with open(image_path, 'rb') as f:
    files = {'file': f}
    response = requests.post(url, files=files)

# 2. Save the processed image
if response.status_code == 200:
    data = response.json()
    base64_str = data['cartoon'].split(",")[0]  # Remove data URL prefix
    decoded = base64.b64decode(base64_str)
    
    # Save to file
    with open(output_path, 'wb') as f:
        f.write(decoded)
    print(f"Image saved to: {os.path.abspath(output_path)}")
else:
    print("Error:", response.text)