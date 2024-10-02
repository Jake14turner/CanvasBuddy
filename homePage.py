import streamlit as st
import sqlite3 as sqlite3
import hashlib
from loginPage import isLoggedIn

st.session_state.bool1 = False


if 'token_saved' not in st.session_state:
    st.session_state.token_saved = False


connection = sqlite3.connect('streamlitBase')
connect = connection.cursor()

def homePageView():
    username = st.session_state.username
    #if the token has already been saved 
    if st.session_state.token_saved:
        st.success("Token saved.")
        

        connect.execute('''SELECT key FROM users WHERE username = ?''', (username,))
        testToken = connect.fetchone()
        #The users token is stored in userToken
        userToken = testToken[0]
        
















    else:
        #the first thing we need to do is make the user enter their key and then write that to their name in the database
        st.text("Lets start off by connecting your canvas account. Please input your canvas token:")
        #put the users token into token
        token = ""
        token = st.text_input("Please enter your token")
        testToken = ""

        
        if st.button("Submit token"):

            if token and username:
                    testToken = ""

                    #connect to the sqlite database and put the users token in
                    
                    connect.execute('''UPDATE users SET key = ? WHERE username = ? ''', (token, username))
                    connection.commit()
                    connect.execute('''SELECT key FROM users WHERE username = ?''', (username,))
                    testToken = connect.fetchone()
                    if testToken and testToken[0] == token:
                        st.success(f"Token saved for {username}.")
                        
                        st.session_state.bool1 = True
                        st.session_state.token_saved = True
                    else:
                        st.error(f"Failed to save or retrieve the token for user {username}.")




#This is the code to retreive a specific users token
    #connect.execute('''SELECT key FROM users WHERE username = ?''', (username,))
    #testToken = connect.fetchone()



    



if 'isLoggedIn' not in st.session_state:
    st.session_state.isLoggedIn = False






#Check if the user is logged in, if they are display the homePage
if st.session_state.isLoggedIn and st.session_state.bool1 == False:
    homePageView()
else:
    st.text("Please log in to view home page.")

