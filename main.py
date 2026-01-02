import cv2
import easyocr
import joblib
from feature_engineering import extract_features

# Load model & OCR
model = joblib.load("model.pkl")
reader = easyocr.Reader(['en'], gpu=False)

def rotate_image(image, angle):
    if angle == 90:
        return cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    elif angle == 180:
        return cv2.rotate(image, cv2.ROTATE_180)
    elif angle == 270:
        return cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    return image

def predict_target_line(lines):
    best_score = 0
    best_line = None

    for line in lines:
        features = extract_features(line)
        prob = model.predict_proba([features])[0][1]  # confidence

        if prob > best_score:
            best_score = prob
            best_line = line

    return best_line, best_score

def run_pipeline(image_path):
    image = cv2.imread(image_path)

    for angle in [0, 90, 180, 270]:
        rotated = rotate_image(image, angle)

        results = reader.readtext(rotated)
        lines = [res[1] for res in results]

        target, confidence = predict_target_line(lines)

        if confidence > 0.6:
            return target, angle, confidence

    return None, None, None

# ---------------- RUN ----------------
image_path = "sample.jpg"
target, angle, confidence = run_pipeline(image_path)

if target:
    print(f"✅ FOUND TARGET (rotation={angle}°, confidence={confidence:.2f})")
    print(target)
else:
    print("❌ Target not found")
