import streamlit as st
from PIL import Image

st.set_page_config(page_title="Ball Finder - AI Based", layout="centered")

st.title("Ball Finder - AI Based")
st.write("Upload an image of the match (ball removed)")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", width=800)
    st.success(f"Image uploaded successfully! Size: {image.size[0]} x {image.size[1]}")
