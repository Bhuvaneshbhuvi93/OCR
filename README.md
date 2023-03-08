# BizCardX: OCR Data Extraction from Business Cards
This project is a Streamlit application that allows users to upload an image of a business card and extract relevant information from it using easyOCR.
The company name, card holder name, designation, mobile number, email address, website URL, area, city, state, and pin code are all extracted.
The extracted data could be edited in the app before being saved in the MySQL database. The app also has a dedicated database management page where you can see the uploaded data of the business card and perform CRUD operations on those data.

## Technologies Used
* Python 3

* Streamlit

* easyOCR

* MySQL

## Problem Statement
You have been tasked with developing a Streamlit application that allows users to
upload an image of a business card and extract relevant information from it using
easyOCR. The extracted information should include the company name, card holder
name, designation, mobile number, email address, website URL, area, city, state,
and pin code. The extracted information should then be displayed in the application's
graphical user interface (GUI).
In addition, the application should allow users to save the extracted information into
a database along with the uploaded business card image. The database should be
able to store multiple entries, each with its own business card image and extracted
information.
To achieve this, you will need to use Python, Streamlit, easyOCR, and a database
management system like SQLite or MySQL. The application should have a simple
and intuitive user interface that guides users through the process of uploading the
business card image and extracting its information. The extracted information should
be displayed in a clean and organized manner, and users should be able to easily
add it to the database with the click of a button. And Allow the user to Read the data,
Update the data and Allow the user to delete the data through the streamlit UI
This project will require skills in image processing, OCR, GUI development, and
database management. It will also require you to carefully design and plan the
application architecture to ensure that it is scalable, maintainable, and extensible.
Good documentation and code organization will also be important for this project.

## Approach

Install the required packages: You will need to install Python, Streamlit,
easyOCR, and a database management system like SQLite or MySQL.
