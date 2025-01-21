import base64
import io
from PIL import Image

import numpy as np

def encode_image(pil_image):
    # Create a BytesIO object to hold the image data in memory
    buffer = io.BytesIO()
    
    # Save the image to the buffer in PNG format (you can choose JPEG or others)
    pil_image.save(buffer, format="PNG")
    
    # Get the binary image data
    buffer.seek(0)
    encoded_string = base64.b64encode(buffer.read()).decode("utf-8")
    
    return encoded_string

def capture_frame(camera, save_image=False):
    data = camera.poll()
    color_image = data["color"].convert("RGB")
    annotation_image = data["annotation"].convert("RGB")

    if save_image:
        color_image.save("color_image.png")
        annotation_image.save("annotation_image.png")

    color_image_encoded = encode_image(color_image)
    annotation_image_encoded = encode_image(annotation_image)

    return color_image_encoded, annotation_image_encoded


