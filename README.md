# OCR-ai

This repository provides a minimal OCR example using Python. If no text is found in the image, the program uses the [Salesforce/blip-image-captioning-base](https://huggingface.co/Salesforce/blip-image-captioning-base) model to describe the image. The combined result is then optionally sent to an LLM (e.g., OpenAI GPT) if the `OPENAI_API_KEY` environment variable is set.

## Requirements
- Python 3
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed on your system
- The Python packages: `pytesseract`, `Pillow`, `transformers`, `torch`, and `openai`

Install the Python dependencies with:

```bash
pip install pytesseract Pillow transformers torch openai
