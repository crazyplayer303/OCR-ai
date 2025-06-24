# OCR-ai

This repository provides a minimal OCR example using Python.

## Requirements
- Python 3
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed on your system
- The Python packages `pytesseract` and `Pillow`

Install the Python dependencies with:

```bash
pip install pytesseract Pillow
```

## Usage

Run the script with the path to a PNG or JPG image:

```bash
python ocr.py path/to/image.png
```

The program will output the text recognized from the image.
