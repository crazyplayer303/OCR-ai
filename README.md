# OCR-ai

This repository provides a minimal OCR example using Python. If no text is found in the image, the program uses the [Salesforce/blip-image-captioning-base](https://huggingface.co/Salesforce/blip-image-captioning-base) model to describe the image.

## Requirements
- Python 3
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed on your system
- The Python packages `pytesseract`, `Pillow`, `transformers`, and `torch`

Install the Python dependencies with:

```bash
pip install pytesseract Pillow transformers torch
```

## Usage

Run the script with the path to a PNG or JPG image:

```bash
python ocr.py path/to/image.png
```

The program extracts text from the image and also generates a caption using the BLIP model. Both pieces of information are combined and printed. If only one is available, just that result is shown.
