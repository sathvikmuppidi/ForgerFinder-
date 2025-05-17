from PyPDF2 import PdfReader

def get_pdf_metadata(pdf_path):
    """Extract metadata dictionary from PDF file."""
    reader = PdfReader(pdf_path)
    return reader.metadata

def print_metadata_report(metadata):
    """Nicely print the metadata content."""
    print("=== PDF Metadata Overview ===")
    for key, val in metadata.items():
        print(f"{key}: {val}")

def check_for_suspicious_metadata(metadata):
    """Flag suspicious or missing metadata fields."""
    required_fields = ['/CreationDate', '/ModDate', '/Author']
    for field in required_fields:
        if field not in metadata or metadata[field] is None:
            print(f"Warning: Missing important metadata field {field}")

if __name__ == "__main__":
    file_path = '../data/suspicious/fake_certificate.pdf'
    meta = get_pdf_metadata(file_path)
    print_metadata_report(meta)
    check_for_suspicious_metadata(meta)
