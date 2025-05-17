import pytesseract
import cv2
import difflib

def extract_text(image_path):
    img = cv2.imread(image_path)
    return pytesseract.image_to_string(img)

def compare_texts(text1, text2):
    diff = difflib.ndiff(text1.splitlines(), text2.splitlines())
    changes = "\n".join(line for line in diff if line.startswith('+ ') or line.startswith('- '))
    return changes
