import os
from pdf2image import convert_from_path

def pdf_to_images(pdf_file, output_dir='data/suspicious/images', dpi=200):
    """Convert PDF pages to JPEG images."""
    os.makedirs(output_dir, exist_ok=True)
    pages = convert_from_path(pdf_file, dpi=dpi)
    
    saved_files = []
    for idx, page in enumerate(pages, start=1):
        image_path = os.path.join(output_dir, f'page_{idx}.jpg')
        page.save(image_path, 'JPEG')
        saved_files.append(image_path)
        print(f"[INFO] Saved page {idx} as image: {image_path}")
    return saved_files

if __name__ == "__main__":
    pdf_path = '../data/suspicious/fake_certificate.pdf'
    pdf_to_images(pdf_path)
