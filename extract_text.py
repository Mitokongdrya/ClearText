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


# from pypdf import PdfReader

# # Load the PDF
# reader = PdfReader("example.pdf")  # Change to your file name

# # Set the output filename
# output_filename = "extracted_text.txt"

# # Extract text from all pages
# all_text = ""
# for i, page in enumerate(reader.pages):
#     print(f"Extracting Page {i+1}...")
#     text = page.extract_text(extraction_mode="layout")  # You can tweak this if needed
#     if text:
#         all_text += f"\n--- Page {i+1} ---\n{text}"
#     else:
#         all_text += f"\n--- Page {i+1} ---\n[No text found]"

# # Write to .txt file
# with open(output_filename, "w", encoding="utf-8") as f:
#     f.write(all_text)

# print(f"\n✅ Extraction complete. Text saved to {output_filename}")

# ______________________________________________________________________________________
# from pypdf import PdfReader

# # Load the PDF
# reader = PdfReader("example.pdf")

# # Choose the page
# page = reader.pages[0]  # first page

# # Extract basic text
# print("\n--- Basic Text ---")
# print(page.extract_text())

# # Extract text preserving layout
# print("\n--- Layout Mode ---")
# print(page.extract_text(extraction_mode="layout"))

# # Extract text with additional layout tuning
# print("\n--- Tuned Layout ---")
# text = page.extract_text(
#     extraction_mode="layout",
#     layout_mode_space_vertically=False,
#     layout_mode_scale_weight=1.0,
#     layout_mode_strip_rotated=False
# )
# print(text)
