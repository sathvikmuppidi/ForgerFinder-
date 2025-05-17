import os

def ensure_folder_exists(path):
    """Create folder if it doesn't exist."""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"[INFO] Created directory: {path}")

def list_pdf_files(directory):
    """Return list of PDF files in directory."""
    return [f for f in os.listdir(directory) if f.lower().endswith('.pdf')]
