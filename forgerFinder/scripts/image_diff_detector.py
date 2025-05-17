import cv2
import numpy as np

def calculate_image_difference(img_path1, img_path2, diff_output_path=None):
    """Compute and optionally save the difference image highlighting discrepancies."""
    img1 = cv2.imread(img_path1)
    img2 = cv2.imread(img_path2)

    if img1.shape != img2.shape:
        print("[ERROR] Images have different sizes or channels.")
        return False

    diff = cv2.absdiff(img1, img2)
    gray_diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray_diff, 30, 255, cv2.THRESH_BINARY)

    if diff_output_path:
        cv2.imwrite(diff_output_path, thresh)
        print(f"[INFO] Difference image saved at: {diff_output_path}")

    diff_score = np.sum(thresh) / 255
    print(f"[DEBUG] Number of different pixels: {diff_score}")

    return diff_score > 0

if __name__ == "__main__":
    original_img = '../data/originals/legit_certificate_page1.jpg'
    suspect_img = '../data/suspicious/images/page_1.jpg'
    diff_img = '../data/suspicious/diff_page1.jpg'

    difference_found = calculate_image_difference(original_img, suspect_img, diff_img)
    if difference_found:
        print("[RESULT] Differences detected between images.")
    else:
        print("[RESULT] Images appear identical.")
