import qrcode
from PIL import Image

def generate_qr(text:str, filename="qrcode.png"):
    """"
    Generate a QR code from a given text and save it as an image file.
    
    Args:
        text (str): The text to encode into the QR code.
        filename (str): The name of the image file to save (e.g., "qrcode.png").
        
    Returns:
        None
    """
    qr = qrcode.QRCode(
        box_size=5,
        version=1,  
        error_correction=qrcode.constants.ERROR_CORRECT_H,  
        border=4,  
    )

    qr.add_data(text)

    #Generate image
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR code généré et sauvegardé dans {filename}")
    

