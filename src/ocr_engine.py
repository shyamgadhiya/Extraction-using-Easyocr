import easyocr
import numpy as np

# Initialize once (important for performance)
reader = easyocr.Reader(['en'], gpu=False)

def perform_ocr(image):
    """
    Returns OCR text as multiline string
    """
    results = reader.readtext(image, detail=1, paragraph=True)

    lines = []
    for (_, text, confidence) in results:
        if confidence > 0.3:  # filter noisy detections
            lines.append(text)

    return "\n".join(lines)
