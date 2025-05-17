import cv2

def load_gray_image(image_path):
    """Load image in grayscale."""
    return cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

def resize_image(image, width=None, height=None):
    """Resize image keeping aspect ratio."""
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    return cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
