import cv2
import numpy as np

def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Increase contrast
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    contrast = clahe.apply(gray)

    # Gaussian blur
    blur = cv2.GaussianBlur(contrast, (5,5), 0)

    # Resize
    resized = cv2.resize(blur, None, fx=1.8, fy=1.8, interpolation=cv2.INTER_CUBIC)

    return resized
