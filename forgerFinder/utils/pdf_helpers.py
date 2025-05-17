from PyPDF2 import PdfReader

def get_pdf_author(pdf_path):
    reader = PdfReader(pdf_path)
    metadata = reader.metadata
    return metadata.get('/Author', 'Unknown')

def get_pdf_creation_date(pdf_path):
    reader = PdfReader(pdf_path)
    metadata = reader.metadata
    return metadata.get('/CreationDate', 'Unknown')
