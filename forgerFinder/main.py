from modules.metadata_checker import analyze_metadata
from modules.layout_analyzer import compare_layout
from modules.ocr_text_checker import extract_text, compare_texts

# Step 1: Metadata Analysis
meta, issues = analyze_metadata("samples/suspect.pdf")
with open("output/metadata_report.txt", "w") as f:
    f.write(str(meta) + "\n\n" + "\n".join(issues))

# Step 2: Layout Comparison
ratio = compare_layout("templates/valid_template.jpg", "samples/suspect.jpg", "output/layout_diff.jpg")
print(f"Layout mismatch ratio: {ratio:.2f}")

# Step 3: OCR Text Diff (Optional)
original_text = extract_text("templates/valid_template.jpg")
suspect_text = extract_text("samples/suspect.jpg")
diffs = compare_texts(original_text, suspect_text)
with open("output/text_differences.txt", "w") as f:
    f.write(diffs)
