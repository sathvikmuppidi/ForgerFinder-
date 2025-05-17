# Certificate Tampering Detection System

This project is a lightweight prototype to detect tampered or fake PDF certificates using techniques like:
- PDF metadata analysis
- Layout/image-based comparison
- Textual anomaly detection

---

## 📁 Project Structure

certificate_checker/
│
├── data/
│ ├── originals/
│ │ ├── legit_certificate.pdf
│ │ ├── legit_certificate_page1.jpg
│ │ └── legit_text.txt
│ └── suspicious/
│ ├── fake_certificate.pdf
│ ├── images/
│ │ └── page_1.jpg
│ ├── fake_text.txt
│ └── diff_page1.jpg
│
├── scripts/
│ ├── metadata_checker.py
│ ├── layout_matcher.py
│ ├── image_diff_detector.py
│ ├── text_extractor.py
│ └── textual_diff_analyzer.py
│
├── utils/
│ ├── file_ops.py
│ ├── img_processing.py
│ └── pdf_helpers.py
│
├── requirements.txt
└── README.md



## ⚙️ How to Run

1. **Install Dependencies**  
   Run this in the terminal:
   ```bash
   pip install -r requirements.txt


2.Extract and Compare PDF Metadata

    python scripts/metadata_checker.py
Extract Text from Suspicious PDF

3.Extract Text from Suspicious PDF
    ```bash 
    
    python scripts/text_extractor.py


4.Compare Textual Content
            
    python scripts/textual_diff_analyzer.py

    
Run Image Layout Matching
(You must convert PDFs to images before this step.)

5.Run Image Layout Matching
(You must convert PDFs to images before this step.)
   
   
    python scripts/layout_matcher.py
Detect Image Differences

6.Detect Image Differences

    python scripts/image_diff_detector.py


💡 Suggestions
Add more known templates to the originals/ folder for improved layout verification.

Integrate OCR (Tesseract) for full image-to-text tampering detection (bonus).

Export all results into a single JSON or PDF report.
