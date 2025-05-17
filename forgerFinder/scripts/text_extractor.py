import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    """Extracts all text from the PDF file."""
    doc = fitz.open(pdf_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    return full_text

def save_text_to_file(text, output_file):
    """Save extracted text to a .txt file."""
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"[INFO] Text saved to {output_file}")

if __name__ == "__main__":
    pdf_file = '../data/suspicious/fake_certificate.pdf'
    output_txt = '../data/suspicious/fake_text.txt'
    
    text_content = extract_text_from_pdf(pdf_file)
    save_text_to_file(text_content, output_txt)
