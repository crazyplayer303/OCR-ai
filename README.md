# OCR-ai

This repository provides a minimal OCR example using Python. If no text is found in the image, the program uses the [Salesforce/blip-image-captioning-base](https://huggingface.co/Salesforce/blip-image-captioning-base) model to describe the image.

## Requirements
- Python 3
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed on your system
- The Python packages `pytesseract`, `Pillow`, `transformers`, `torch`, and `openai`

Install the Python dependencies with:

```bash
pip install pytesseract Pillow transformers torch openai
The program extracts text from the image and also generates a caption using the BLIP model. Both pieces of information are combined and printed. If only one is available, just that result is shown. If you set the ``OPENAI_API_KEY`` environment variable, the script will also send the combined output to an LLM and display the response.
