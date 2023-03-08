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


st.subheader("Database")
mycursor.execute("SELECT * FROM business_cards")
myresult = mycursor.fetchall()
df = pd.read_sql("SELECT * FROM business_cards", mydb)
st.dataframe(df)

# if st.button('Update Data'):
st.subheader("Update Data")
with st.form("update-form"):
        id = st.text_input("Enter the id you want to update")
        name = st.text_input("Enter the new name")
        email = st.text_input("Enter the new email")
        submitted = st.form_submit_button("Update")

        if submitted:
            mycursor = mydb.cursor()
            sql = "UPDATE business_cards SET name = %s, email = %s WHERE id = %s"
            val = (name, email, id)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record updated successfully")

            df = pd.read_sql("SELECT * FROM business_cards", mydb)
            st.dataframe(df)

# if st.button('Delete Data'):
# Allow the user to delete a record
    # update_msg = st.empty()
st.subheader("Delete Data")
with st.form("delete-form"):
        id = st.text_input("Enter the record id you want to delete")
        submitted = st.form_submit_button("Delete")

        if submitted:
            mycursor = mydb.cursor()
            sql = "DELETE FROM business_cards WHERE id = %s"
            val = (id,)
            mycursor.execute(sql, val)
            mydb.commit()
            st.warning("Record deleted successfully")

            df = pd.read_sql("SELECT * FROM business_cards", mydb)
            st.dataframe(df)