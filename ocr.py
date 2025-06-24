import sys
from PIL import Image
import pytesseract
from transformers import BlipProcessor, BlipForConditionalGeneration


def main():
    if len(sys.argv) != 2:
        print("Usage: python ocr.py <image_file>")
        sys.exit(1)

    image_path = sys.argv[1]
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Error opening {image_path}: {e}")
        sys.exit(1)

    text = pytesseract.image_to_string(image).strip()
    if text:
        print(text)
        return

    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    inputs = processor(image, return_tensors="pt")
    output = model.generate(**inputs)
    caption = processor.decode(output[0], skip_special_tokens=True)
    print(caption)


if __name__ == "__main__":
    main()
