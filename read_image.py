import argparse
import os
from PIL import Image
import pytesseract
from transformers import BlipProcessor, BlipForConditionalGeneration
import openai


def ask_llm(prompt: str) -> str | None:
    """Send a prompt to an LLM and return the response text.

    The function expects an OpenAI API key in the OPENAI_API_KEY environment
    variable. If the key is not set or the request fails, ``None`` is returned.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return None

    openai.api_key = api_key
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message["content"].strip()
    except Exception:
        return None


def extract_text(image: Image.Image) -> str:
    """Return OCR text from the image (may be empty)."""
    return pytesseract.image_to_string(image).strip()


def generate_caption(image: Image.Image) -> str:
    """Generate a caption describing the image."""
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    inputs = processor(image, return_tensors="pt")
    output = model.generate(**inputs)
    return processor.decode(output[0], skip_special_tokens=True).strip()


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract text from an image and optionally summarize it with an LLM")
    parser.add_argument("image", help="Path to an image file")
    args = parser.parse_args()

    try:
        image = Image.open(args.image)
    except Exception as e:
        raise SystemExit(f"Error opening {args.image}: {e}")

    text = extract_text(image)
    caption = generate_caption(image)

    if text and caption:
        prompt = f"{text}\n{caption}"
    else:
        prompt = text or caption

    llm_answer = ask_llm(prompt)
    if llm_answer:
        print(llm_answer)
    else:
        print(prompt)


if __name__ == "__main__":
    main()
