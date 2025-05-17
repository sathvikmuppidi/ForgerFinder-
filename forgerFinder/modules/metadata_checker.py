import fitz  # PyMuPDF
from datetime import datetime

def analyze_metadata(pdf_path):
    doc = fitz.open(pdf_path)
    metadata = doc.metadata
    issues = []

    creation = metadata.get("creationDate", "")
    mod = metadata.get("modDate", "")

    if creation and mod:
        try:
            c_time = datetime.strptime(creation[2:16], "%Y%m%d%H%M%S")
            m_time = datetime.strptime(mod[2:16], "%Y%m%d%H%M%S")
            if m_time > c_time:
                issues.append("⚠️ Modification date is later than creation date.")
        except Exception as e:
            issues.append(f"⚠️ Could not parse metadata time: {e}")

    if not metadata.get("author"):
        issues.append("⚠️ Missing author field.")

    return metadata, issues
