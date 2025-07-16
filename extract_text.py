# extract_text.py

from pypdf import PdfReader

def extract_text_from_pdf(file_path: str) -> str:
    """Extract all text from a PDF as a string."""
    reader = PdfReader(file_path)
    extracted_text = ""
    for i, page in enumerate(reader.pages):
        text = page.extract_text(extraction_mode="layout")
        if text:
            extracted_text += f"\n--- Page {i+1} ---\n{text}"
        else:
            extracted_text += f"\n--- Page {i+1} ---\n[No text found]"
    return extracted_text

def extract_and_save_to_txt(file_path: str, output_txt_path: str) -> None:
    """Extracts text and saves it to a .txt file."""
    text = extract_text_from_pdf(file_path)
    with open(output_txt_path, "w", encoding="utf-8") as f:
        f.write(text)
