import sys
from PIL import Image
import pytesseract


def main():
    if len(sys.argv) != 2:
        print("Usage: python ocr.py <image_file>")
        sys.exit(1)

    image_path = sys.argv[1]
    try:
        text = pytesseract.image_to_string(Image.open(image_path))
        print(text)
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
