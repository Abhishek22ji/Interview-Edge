
import streamlit as st
from streamlit_option_menu import option_menu
from MyPages.AboutUs import show_about
from MyPages.upload import show_upload
from MyPages.home import show_home
from MyPages.helpbot import show_helpbot
st.set_page_config(page_title="Interview Edge", layout="centered",page_icon="📄")


# st.markdown("""
# <style>
# section[data-testid="stSidebar"] {
#     height: 100vh;   /* full screen height */
# }
# </style>
# """, unsafe_allow_html=True)

st.markdown("""
<style>
.css-1d391kg {   /* sidebar content */
    padding-top: 20px;
    padding-bottom: 50px;
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
 selected=option_menu(
  menu_title="Interview Edge Menu :",
  options=("Home","Upload Resume","Test","Visualization","HelpBot","AboutUs"),
  icons=("house","file-text","clipboard-check","bar-chart","robot","info-circle"),
  menu_icon="menu-button-wide",
  default_index=0,
 )
if selected == "Home":
    show_home()

elif selected=="Upload Resume":
    show_upload()

elif selected == "Test":
    st.header("📝 MCQ Test")      

elif selected == "Visualization":
    st.header("🤖 AI Help Bot") 

elif selected == "HelpBot":
    show_helpbot()        

elif selected == "AboutUs":
   show_about()
    
    
