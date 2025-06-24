# OCR-ai

This repository provides a minimal OCR example using Python. If no text is found in the image, the program uses the [Salesforce/blip-image-captioning-base](https://huggingface.co/Salesforce/blip-image-captioning-base) model to describe the image.

## Requirements
- Python 3
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed on your system
- The Python packages `pytesseract`, `Pillow`, `transformers`, `torch`, and `openai`

Install the Python dependencies with:

```bash
pip install pytesseract Pillow transformers torch openai
```

## Usage

Run the script with the path to a PNG or JPG image:

```bash
python read_image.py path/to/image.png
```

The program extracts text from the image and falls back to a BLIP-generated caption if no text is detected. The combined result is sent to an LLM if the ``OPENAI_API_KEY`` environment variable is set, and the model's response is printed. If the API key is missing, the program simply prints the combined text and caption.
