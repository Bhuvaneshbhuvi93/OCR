import streamlit as st
import easyocr
import pandas as pd
import io
import numpy as np
from PIL import Image
import re
import cv2
from PIL import Image
import mysql.connector

st.set_page_config(
    layout="wide",
    page_title = 'OCR-Tool',
    page_icon = '',
)

mydb = mysql.connector.connect(
  user = 'root',
  password = 'Bh#9900425184',
  host = '127.0.0.1',
  database = 'ocr',
)

mycursor = mydb.cursor()

st.title(":blue[O]ptical :blue[C]harater :blue[R]ecognition (:blue[OCR])")

uploaded_file = st.file_uploader("Choose a image file",type=["jpg", "jpeg", "png"])

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

    if results is not None:
        df = pd.DataFrame(columns=[])
        for r in results:
            df = df.append({'Data': r[1]}, ignore_index=True)
    
    

    # return results

    for res in results:
        pts = np.array(res[0]).astype(np.int32)
        pts = pts.reshape((-1,1,2))
        color = (0,0,255)
        isClosed = True
        thickness = 2
        cv2.polylines(img_array,[pts],isClosed,color,thickness)

        # cv2.imshow('image', image_with_boxes)
    
    image_with_boxes = Image.fromarray(img_array)

    return df, image_with_boxes


# Check if a file was uploaded
if uploaded_file is not None:
    # Do something with the uploaded file
    col1, col2 = st.columns([1,1])
    col1.subheader("Uploaded File")
    col1.image(uploaded_file, caption='Uploaded business card image', use_column_width=True)
    extracted_data, image_with_boxes = extract_info(uploaded_file)
    col2.subheader("Extracted Text with Bounding Boxes")
    col2.image(image_with_boxes, caption='Extracted text with bounding boxes', use_column_width=True)

if uploaded_file is not None:
    col1, col2 = st.columns([1,1])
    edited_df = col1.experimental_data_editor(extracted_data, num_rows="dynamic")
    col1.write(""" Arrange as follows:\n 
                Name in 0, Job Title in 1, Phone in 2, email in 3, Website in 4, Company in 5, Address in 6, Industry in 7.\n
                If any one field is not available leave it blank""")

if uploaded_file is not None:
    new_df = pd.DataFrame(columns=['Name', 'Job Title', 'Phone Number', 'Email', 'Website', 'Company Name', 'Address', 'Industry'])  
    new_df['Name'] = edited_df[edited_df.index == 0].Data.values
    new_df['Job Title'] = edited_df[edited_df.index == 1].Data.values
    new_df['Phone Number'] = edited_df[edited_df.index == 2].Data.values
    new_df['Email'] = edited_df[edited_df.index == 3].Data.values
    new_df['Website'] = edited_df[edited_df.index == 4].Data.values
    new_df['Company Name'] = edited_df[edited_df.index == 5].Data.values
    new_df['Address'] = edited_df[edited_df.index == 6].Data.values
    new_df['Industry'] = edited_df[edited_df.index == 7].Data.values
    col2.dataframe(new_df)

if st.sidebar.button("Upload to DB"):
    # mycursor.execute("DROP TABLE IF EXISTS business_cards")
    mycursor.execute("CREATE TABLE IF NOT EXISTS business_cards (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255), phone VARCHAR(255), company VARCHAR(255), title VARCHAR(255), address VARCHAR(255), industry VARCHAR(255), website VARCHAR(255), image LONGBLOB)")
    sql = "INSERT INTO business_cards (name, email, phone, company, title, address, industry, website, image) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    image_data = uploaded_file.read()
    val = (new_df['Name'][0], new_df['Email'][0], new_df['Phone Number'][0], new_df['Company Name'][0], new_df['Job Title'][0], new_df['Address'][0],new_df['Industry'][0],new_df['Website'][0], image_data)
    mycursor.execute(sql, val)
    mydb.commit()
    st.sidebar.success("Data uploaded successfully!")




