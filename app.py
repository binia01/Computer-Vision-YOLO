import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

# Title
st.title("🚧 PPE Safety Detection App")
st.write("Upload an image to detect Hard Hats.")

model_path = './data/best.pt' 

try:
    model = YOLO(model_path)
except Exception as e:
    st.error(f"Could not load model. Make sure '{model_path}' is in the directory.")
    st.stop()

# File Uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Display original image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write("Detecting...")

    # Perform Inference
    results = model(image)

    # Visualize results
    # Plot returns a numpy array representing the image with boxes
    res_plotted = results[0].plot() 
    
    # Convert back to PIL image for Streamlit
    res_image = Image.fromarray(res_plotted[..., ::-1]) # RGB conversion

    # Display Result
    st.subheader("Detection Result:")
    st.image(res_image, caption='Detected Safety Gear', use_column_width=True)

    # specific class counts (optional detail)
    boxes = results[0].boxes
    if boxes:
        st.success(f"Detected {len(boxes)} objects.")
    else:
        st.warning("No safety equipment detected.")