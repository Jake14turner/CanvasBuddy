import streamlit as st
import sqlite3 as sqlite3
import hashlib
from loginPage import isLoggedIn




def homePageView():
    st.title("Home Page")
    st.write("Welcome! You are logged in.")
#    username = st.session_state.username

    



if 'isLoggedIn' not in st.session_state:
    st.session_state.isLoggedIn = False






#Check if the user is logged in, if they are display the homePage
if st.session_state.isLoggedIn:
    homePageView()
else:
    st.text("Please log in to view home page.")

