from PIL import Image
from pyzbar.pyzbar import decode
from typing import Union

def scan_qr(image: Union[str, Image.Image]) -> str:
    """
    Scan a QR code from an image and return the encoded text.
    
    Args:
        image (str or PIL.Image.Image): Path to the image file or a PIL Image object.
        
    Returns:
        str: The text encoded in the QR code. Returns an empty string if no QR code is found.
    """
    # Open the image if a file path is provided
    if isinstance(image, str):
        img = Image.open(image)
    else:
        img = image

    # Decode the QR code(s) in the image
    decoded_objects = decode(img)

    # If at least one QR code is found, return the first one
    if decoded_objects:
        return decoded_objects[0].data.decode('utf-8')
    else:
        return ""  # No QR code found

