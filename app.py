import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(page_title="Image Upload and Display", layout="centered")

# Title
st.title("Upload Two Images and Display Output Text")

# Upload Two Images
st.subheader("Upload Images")
image1 = st.file_uploader("Upload first image", type=["jpg", "jpeg", "png"])
image2 = st.file_uploader("Upload second image", type=["jpg", "jpeg", "png"])

# Display Images if Uploaded
if image1:
    st.image(Image.open(image1), caption="First Image", use_column_width=True)

if image2:
    st.image(Image.open(image2), caption="Second Image", use_column_width=True)

# Placeholder for output text
output_text_placeholder = st.empty()

# Function to mock backend processing (replace with your actual backend call)
def process_images(img1, img2):
    # Here, include code to send images to the backend and receive text output
    # For this example, let's assume it returns a dummy text
    return "Processed output texts from backend."

# Process Images and Display Output
if image1 and image2:
    if st.button("Process Images"):
        with st.spinner("Processing images..."):
            output_text = process_images(image1, image2)
            output_text_placeholder.subheader("Output Text")
            output_text_placeholder.write(output_text)
else:
    st.info("Please upload both images to proceed.")
