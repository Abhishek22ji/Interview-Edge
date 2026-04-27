import streamlit as st

def show_about():
 st.title("📃 Interview Edge System")
 st.markdown("""
<style>
.curve-outline {
    border: 2px solid #00c6ff;
    border-radius: 30px;
    padding: 25px;
    margin-top: 20px;
    background-color: rgba(255,255,255,0.02);
    box-shadow: 0 0 15px rgba(0,198,255,0.2);

    max-height: 500px;       /* 👈 FIX HEIGHT */
    overflow-y: auto;        /* 👈 ENABLE SCROLL */
}

/* Text styling */
.curve-text {
    color: #e0e0e0;
    font-size: 16px;
    line-height: 1.7;
    word-wrap: break-word;
}
</style>
""", unsafe_allow_html=True)

 st.markdown("""
<div class="curve-outline">

<h2 style="color:#00c6ff;">Interview Edge 🚀</h2>

<p class="curve-text">
<b>Interview Edge – AI-Based Intelligent Candidate Screening & Hiring Prediction System</b>
</p>

<p class="curve-text">
Interview Edge – AI-Based Intelligent Candidate Screening & Hiring Prediction System is a
modern web-based application developed to simplify and enhance the recruitment process using
Artificial Intelligence and Machine Learning.
</p>

<p class="curve-text">
In today’s competitive environment, organizations receive a large number of job applications,
making it difficult and time-consuming for recruiters to manually screen resumes and evaluate
candidates effectively. This system addresses that challenge by automating the entire initial
hiring process, ensuring faster, more accurate, and unbiased decision-making. The application
allows candidates to upload their resumes in formats such as PDF and DOCX, which are then analyzed
using Natural Language Processing techniques to extract important information including skills,
education, experience, and contact details.
</p>

<p class="curve-text">
This extracted data is structured and used as the foundation for further evaluation, enabling the
system to understand the candidate’s profile in depth.
Based on the identified skills and qualifications, the platform intelligently generates personalized
interview questions tailored to each candidate.
</p>

<p class="curve-text">
For example, if a candidate has expertise in programming languages like Python or web technologies,
the system creates relevant questions aligned with those skills. This ensures that each candidate
is assessed in a way that reflects their actual knowledge and capabilities rather than a generic
evaluation approach. Along with question generation, the system also includes an interactive MCQ-based
test module where candidates can answer dynamically generated questions. The test adapts to the candidate
skill set, making the evaluation more meaningful and targeted. After the test is completed, the system 
automatically calculates the score and analyzes the performance, identifying strengths and weaknesses in
different areas.
</p>                  

</div>
""", unsafe_allow_html=True)