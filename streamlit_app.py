import streamlit as st
from PIL import Image

st.set_page_config(page_title="Ball Finder - AI Based")

st.title("Ball Finder - AI Based")
st.write("Upload an image of the match (ball removed)")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.success("تصویر با موفقیت آپلود شد.")
