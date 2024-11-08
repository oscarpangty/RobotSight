import streamlit as st
from PIL import Image
from image_processor import process_images
from image_processor import garbage_items
# Page Configuration
st.set_page_config(page_title="Image Upload and Analysis Display", layout="centered")

# Title
st.title("Cleaning Robot Sight")

# Upload Two Images
st.subheader("Upload Images")
image1 = st.file_uploader("Upload room after being used", type=["jpg", "jpeg", "png"])
image2 = st.file_uploader("Upload room's original condition", type=["jpg", "jpeg", "png"])

# Display Images if Uploaded
if image1:
    st.image(Image.open(image1), caption="Used Room", use_column_width=True)

if image2:
    st.image(Image.open(image2), caption="Original Room", use_column_width=True)

# Placeholder for output text
output_text_placeholder1 = st.empty()
output_text_placeholder2 = st.empty()

# Process Images and Display Output
if image1 and image2:
    if st.button("Generate Insights"):
        with st.spinner("Processing images..."):
            output_text = process_images(image1, image2)
            output_text_placeholder1.subheader("Output Text")
            output_text_placeholder1.write(output_text)
            
    if st.button("Garbage to be thrown away"):
        with st.spinner("Processing images..."):
            output_text = garbage_items(image1, image2)
            output_text_placeholder2.subheader("Output Text")
            output_text_placeholder2.write(output_text)
else:
    st.info("Please upload both images to proceed.")
    
data = {
  "dirty_items": [
    {
      "item": "towels",
      "status": "crumpled"
    }
  ],
  "garbage": [
    {
      "item": "water bottle",
      "type": "plastic"
    }
  ]
}
