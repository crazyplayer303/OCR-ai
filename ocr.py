import sys
from PIL import Image
import pytesseract
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch

def main():
    if len(sys.argv) != 2:
        print("Usage: python ocr.py <image_file>")
        sys.exit(1)

    image_path = sys.argv[1]
    try:
        image = Image.open(image_path).convert("RGB")
    except Exception as e:
        print(f"Error opening {image_path}: {e}")
        sys.exit(1)

    # Run OCR
    try:
        text = pytesseract.image_to_string(image).strip()
    except Exception as e:
        print(f"OCR failed: {e}")
        text = ""

    # Run BLIP captioning
    try:
        processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
        inputs = processor(images=image, return_tensors="pt")
        output = model.generate(**inputs)
        caption = processor.decode(output[0], skip_special_tokens=True).strip()
    except Exception as e:
        print(f"BLIP captioning failed: {e}")
        caption = ""

    # Combine results
    if text and caption:
        text_output = f"{text}\n\nCaption: {caption}"
    elif text:
        text_output = text
    elif caption:
        text_output = f"Caption: {caption}"
    else:
        text_output = "No readable content found."

    print("\n--- Combined Output ---\n")
    print(text_output)

if __name__ == "__main__":
    main()
