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
Developing Streamlit application that allows users to upload an image of a business card and extract relevant information from it using
easyOCR. The extracted information should include the company name, card holder
name, designation, mobile number, email address, website URL, area, city, state,
and pin code. 
The extracted information should then be displayed in the application's
graphical user interface (GUI).

In addition, the application should allow users to save the extracted information into
a database along with the uploaded business card image. The database should be
able to store multiple entries, each with its own business card image and extracted
information.

The application should have a simple and intuitive user interface that guides users through the process of uploading the
business card image and extracting its information. The extracted information should
be displayed in a clean and organized manner, and users should be able to easily
add it to the database with the click of a button. And Allow the user to Read the data,Update the data and Allow the user to delete the data through the streamlit UI

## App

The app is designed with a streamlit GUI and multipage access. There will be a complete explanation of this tool on the homepage, along with a YouTube video about the OCR package.
The following page will be the OCR Tool page, where the user can upload an image file of a business card and extract data from it. Once the image has been uploaded, there will be two outputs: an image with bounding boxes and an editable dataframe in which you can edit the extracted data.

After editing, the edited data will be loaded into a new dataframe with column names specified by the user, which the user can then upload to a database such as MySQL, Postgres, or Sqlite.

The following page is Database management, where you can connect to the database and view the data stored in it. This page includes the ability to update previously existing data as well as delete previously existing data in the database.

## Beta Tool

 OCR Tool Beta is the tool in development. This tool offers more benefits than the deployed tool, but it is still in development. This programme is designed to automatically detect the mail, name, company name, and other information on a business card. Whereas in the deployed tool, data is extracted and then assigned to a specific entity by the user.
 
 
