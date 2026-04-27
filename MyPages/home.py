import streamlit as st
import base64

def show_home():
    st.markdown("## 📄 Interview Edge")
    st.write("Interview Edge is an AI-based system that automates resume analysis and candidate evaluation.")


    st.markdown("<br>", unsafe_allow_html=True)


    with open("video.mp4", "rb") as f:
        video_bytes = f.read()

    video_base64 = base64.b64encode(video_bytes).decode()


    st.markdown(f"""
    <video width="100%" autoplay muted loop playsinline style="border-radius:15px;">
        <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
    </video>
    """, unsafe_allow_html=True)