import streamlit as st
import sqlite3 as sqlite3
import hashlib
from loginPage import isLoggedIn




def homePageView():
    
    #the first thing we need to do is make the user enter their key and then write that to their name in the database
    st.text("Lets start off by connecting your canvas account. Please input your canvas token:")
    #put the users token into token
    token = ""
    token = st.text_input("Please enter your token")
    testToken = ""
    
    if st.button("Submit token"):

       
        testToken = ""
        username = st.session_state.username
        #connect to the sqlite database and put the users token in
        connection = sqlite3.connect('streamlitBase')
        connect = connection.cursor()
        connect.execute('''UPDATE users SET key = ? WHERE username = ? ''', (token, username))
        connection.commit()
        connect.execute('''SELECT key FROM users WHERE username = ?''', (username,))
        testToken = connect.fetchone()
    if testToken == token:
            st.success("Succesfully saved token")
        



#This is the code to retreive a specific users token
    #connect.execute('''SELECT key FROM users WHERE username = ?''', (username,))
    #testToken = connect.fetchone()



    



if 'isLoggedIn' not in st.session_state:
    st.session_state.isLoggedIn = False






#Check if the user is logged in, if they are display the homePage
if st.session_state.isLoggedIn:
    homePageView()
else:
    st.text("Please log in to view home page.")

