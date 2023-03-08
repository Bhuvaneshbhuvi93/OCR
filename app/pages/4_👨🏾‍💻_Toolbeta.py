import streamlit as st
import easyocr
import pandas as pd
import io
import numpy as np
from PIL import Image
import re
import cv2
from PIL import Image

st.set_page_config(
    layout="wide",
    page_title = 'OCR-Tool',
    page_icon = '',
)

# Load the OCR reader
reader = easyocr.Reader(['en'], gpu = False)

extracted_data = None

# Function to extract information from the business card image
def extract_info(uploaded_file):
    # Read the text from the image using OCR
    image = Image.open(io.BytesIO(uploaded_file.read()))

    # Convert PIL Image object to numpy array
    img_array = np.array(image)

    # Pass numpy array to EasyOCR's readtext() method
    results = reader.readtext(img_array)

    return results
    
    # Extract the relevant information from the OCR results
 
def extract_fields(extracted_info):
    company_name = ''
    name = ''
    title = ''
    mobile_number = ''
    email = ''
    website = ''
    area = ''
    city = ''
    state = ''
    pin_code = ''
    
    for info in extracted_info:
        text = info[1]
        if re.search(r'\b(Inc\.?|Ltd\.?|LLC|Corp\.?)\b', text, re.IGNORECASE):
            company_name = text
        elif re.search(r'\b([A-Z][a-z]+\s[A-Z][a-z]+)\b', text):
            name = text
        elif re.search(r'\b([A-Za-z]+(\s|\.)){1,4}(Manager|Director|CEO|CTO|CFO|COO|VP)\b', text, re.IGNORECASE):
            title = text
        elif re.search(r'(\+\d{1,2}\s)?(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})', text):
            mobile_number = text
        elif re.search(r'[\w\.-]+@[\w\.-]+\.[\w\.]+', text):
            email = text
        elif re.search(r'((https?://)?(www\.)?[A-Za-z0-9]+(\.[A-Za-z]{2,})+)', text):
            website = text
        elif re.search(r'\b(\d{6})\b', text):
            pin_code = text
        elif re.search(r'\b(\w+)\b', text):
            if not area:
                area = text
            elif not city:
                city = text
            elif not state:
                state = text
                
    return {
        "company_name": company_name,
        "card_holder_name": name,
        "designation": title,
        "mobile_number": mobile_number,
        "email_address": email,
        "website_url": website,
        "area": area,
        "city": city,
        "state": state,
        "pin_code": pin_code
    }


st.title(":blue[O]ptical :blue[C]harater :blue[R]ecognition (:blue[OCR])")

st.subheader("Upload a business card image")
uploaded_file = st.file_uploader("Choose a image file",type=["jpg", "jpeg", "png"])


# Check if a file was uploaded
if uploaded_file is not None:
    # Do something with the uploaded file
    col1, col2 = st.columns([1,1])
    col1.subheader("Uploaded File")
    col1.image(uploaded_file, caption='Uploaded business card image', use_column_width=True)
    
if st.sidebar.button("Extract Data"):
    col2.subheader("Data Extracted")
    info = extract_info(uploaded_file)
    data = extract_fields(info)
    # Display the extracted information in a DataFrame
    df = pd.DataFrame.from_dict(data, orient="index")
    df = df.rename(columns={0: "Value"})
    col2.write(df, caption='Extracted Data from Image')


