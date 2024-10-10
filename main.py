import streamlit as st
import sqlite3 as sq




st.title("3444 project")



registerPage = st.Page("registerPage.py", title="Register Page", icon=":material/add_circle:")
loginPage = st.Page("loginPage.py", title="Login Page", icon=":material/delete:")
homePage = st.Page("homePage.py", title="Home Page", icon=":material/add_circle:")
todopage = st.Page("todopage.py", title = "To do page")




pg = st.navigation([registerPage, loginPage, homePage, todopage])

pg.run()




    

