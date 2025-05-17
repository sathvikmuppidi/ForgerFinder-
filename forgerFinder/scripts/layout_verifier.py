import cv2
import numpy as np

def is_layout_matching(template_img_path, target_img_path, similarity_threshold=0.85):
    """Use template matching to check layout similarity."""
    template_img = cv2.imread(template_img_path, cv2.IMREAD_GRAYSCALE)
    target_img = cv2.imread(target_img_path, cv2.IMREAD_GRAYSCALE)

    match_result = cv2.matchTemplate(target_img, template_img, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(match_result)

    print(f"[DEBUG] Layout similarity score: {max_val:.2f}")

    if max_val >= similarity_threshold:
        print("[RESULT] Layout matches the trusted template.")
        return True
    else:
        print("[RESULT] Layout does NOT match the trusted template.")
        return False

if __name__ == "__main__":
    template = '../data/templates/valid_layout.png'
    suspicious = '../data/suspicious/images/page_1.jpg'
    is_layout_matching(template, suspicious)
