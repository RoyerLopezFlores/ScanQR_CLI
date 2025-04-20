import argparse
from utils import extract_qr_from_image,open_image,get_image_from_clipboard


def main():
    parser = argparse.ArgumentParser(description="Extract QR code data from an image.")
    parser.add_argument("-i","--image_path", type=str, help="Path to the image file containing the QR code.",required=False)
    args = parser.parse_args()
    
    #------ Processing the arguments ------
    image = None
    if args.image_path is None or args.image_path == "":
        # If no image path is provided, try to get the image from the clipboard
        image = get_image_from_clipboard()
    else:    
        image = open_image(args.image_path)
        if image is None:
            print("Error: Unable to open the image.")
            return
    if image is None:
        print("Error: No image found in clipboard or unable to open the image.")
        return
    #------ Extracting QR code data ------
    qr_data = extract_qr_from_image(image)
    if qr_data:
        print("*"*10,"QR Code Data","*"*10)
        print(qr_data)
    else:
        print("No QR code found or unable to decode.")
if __name__ == "__main__":
    main()