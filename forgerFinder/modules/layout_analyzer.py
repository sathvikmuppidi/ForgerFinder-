import cv2
import numpy as np

def compare_layout(template_path, suspect_path, output_path):
    img1 = cv2.imread(template_path, 0)
    img2 = cv2.imread(suspect_path, 0)

    diff = cv2.absdiff(img1, img2)
    _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

    heatmap = cv2.applyColorMap(thresh, cv2.COLORMAP_JET)
    cv2.imwrite(output_path, heatmap)

    mismatch_ratio = np.count_nonzero(thresh) / thresh.size
    return mismatch_ratio
