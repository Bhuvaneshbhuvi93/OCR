import cv2
import os
import matplotlib.pyplot as plt
import numpy as np
import easyocr
import streamlit as st
from streamlit_player import st_player

st.set_page_config(
    layout="wide",
    page_title = 'OCR-Tool',
    page_icon = '',
)

st.title(":blue[O]ptical :blue[C]harater :blue[R]ecognition (:blue[OCR])")

st.subheader("About OCR")

st.write(""""OCR (_Optical Character Recognition_) is a technology that converts scanned or printed text images into 
         editable digital formats. OCR can recognise and extract text from images such as photos, PDFs, and scanned documents,
         and then convert that text into a format that can be edited, searched, and stored electronically. OCR technology is used in a variety of fields, 
         including document management, data entry, and image processing, to automate the process of digitising large amounts of text data. 
         OCR can save time and improve accuracy in tasks involving manual data entry and transcription, making it a valuable tool in the digital age.""")
st_player("https://www.youtube.com/watch?v=zrUbRvAHEf8")

st.subheader("About this App")

st.write("""This is a Streamlit application that allows users to upload an image of a business card and use easyOCR(Python Package) to extract relevant information from it.
The information extracted would include the company name, card holder name, designation, mobile number, email address, website URL, area, city, state, and pin code. The extracted data would then be displayed in the graphical user interface of the application (GUI).
The application would also allow users to save the extracted information, along with the uploaded business card image, to a database. The database could hold multiple entries, each with its own business card image and extracted data.""")

st.subheader("Tools & Technologies Used")

st.write("**Python** - *Programming*")

st.write("**Streamlit** - *GUI*")

st.write("**MySQL** - *Database Managment*")

st.write("**easyOCR** - *Data Ectraction*")



