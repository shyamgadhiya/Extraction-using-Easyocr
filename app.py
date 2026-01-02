import streamlit as st
import cv2
import numpy as np
from PIL import Image
#from src.ocr_engine import perform_ocr

from src.preprocessing import preprocess_image
from src.ocr_engine import perform_ocr
from src.text_extraction import extract_target_line
from src.utils import save_results

st.set_page_config(page_title="OCR _1_ Extractor", layout="centered")

st.title("📦 Shipping Label OCR Extractor")
st.write("Extracts full text line containing **_1_ / 1_ / _1**")

uploaded_file = st.file_uploader("Upload Shipping Label Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    image_np = np.array(image)

    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("Run OCR"):
        with st.spinner("Processing..."):
            processed = preprocess_image(image_np)
            ocr_text = perform_ocr(processed)
            target_lines = extract_target_line(ocr_text)

            st.subheader("📄 OCR Output")
            st.text(ocr_text)

            st.subheader("🎯 Extracted Target Line(s)")
            if target_lines:
                for line in target_lines:
                    st.success(line)
                save_results(uploaded_file.name, target_lines)
            else:
                st.warning("No target pattern found")

