from pyzbar.pyzbar import decode
from PIL import Image,ImageGrab


def extract_qr_from_image(image):
    """
    Extracts QR code data from an image.
    
    Args:
        image (PIL.Image): The image containing the QR code.
    
    Returns:
        dict: Decoded QR code data as a dictionary.
    """
    try:
        decoded_objects = decode(image)
        if decoded_objects:
            qr_data = decoded_objects[0].data.decode('utf-8')
            return qr_data
    except Exception as e:
        print(f"Error al procesar la imagen: {e}")
    return None
def open_image(path_image):
    """
    Opens an image file and returns it as a PIL Image object.
    
    Args:
        path_image (str): Path to the image file.
    
    Returns:
        PIL.Image: The opened image.
    """
    try:
        image = Image.open(path_image)
        return image
    except Exception as e:
        print(f"Error al abrir la imagen: {e}")
def get_image_from_clipboard():
    try:
        image = ImageGrab.grabclipboard()
        if isinstance(image, Image.Image):
            return image
        else:
            print("No image found in clipboard.")
    except Exception as e:
        print(f"Error al obtener la imagen del portapapeles: {e}")
if __name__ == "__main__":
    # Example usage:
    image_path = "./images/test2.jpg"  # Replace with your image path
    image = Image.open(image_path)
    qr_data = extract_qr_from_image(image)
    
    if qr_data:
        print("QR Code Data:", qr_data)
    else:
        print("No QR code found or unable to decode.")
