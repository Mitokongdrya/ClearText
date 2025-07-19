from pypdf import PdfReader
from typing import Union
from io import BytesIO

def extract_text_from_pdf(file_stream: Union[str, BytesIO]) -> str:
    """Extract all text from a PDF file path or file-like object."""
    reader = PdfReader(file_stream)
    extracted_text = ""
    for i, page in enumerate(reader.pages):
        text = page.extract_text(extraction_mode="layout")
        if text:
            extracted_text += f"\n--- Page {i+1} ---\n{text}"
        else:
            extracted_text += f"\n--- Page {i+1} ---\n[No text found]"
    return extracted_text