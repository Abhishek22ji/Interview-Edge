import streamlit as st


from resume_parser import (
    extract_text,
    extract_name,
    extract_email,
    extract_phone,
    extract_skills,
    extract_education,
    extract_experience,
    calculate_score
)

def show_upload():
 st.markdown("""
    <style>

    .card {
        background-color: #1e1e2f;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 15px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.3);
        color: white;
    }

    .label {
        font-size: 14px;
        color: #aaa;
        margin-top: 10px;
    }

    .value {
        font-size: 16px;
        margin-bottom: 8px;
    }

    .skill {
        display: inline-block;
        background-color: #00ADB5;
        color: white;
        padding: 5px 10px;
        margin: 5px;
        border-radius: 20px;
        font-size: 13px;
    }

    h2 {
        color: #00ADB5;
    }

    </style>
    """, unsafe_allow_html=True)
 st.title("📃 Interview Edge System")
 st.header("📁 Upload Resume and get instant analysis :")

 uploaded_file = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf", "docx"])

 if uploaded_file:
    text = extract_text(uploaded_file)

    if not text.strip():
        st.error("❌ Could not read file properly")
    else:
        name = extract_name(text)
        email = extract_email(text)
        phone = extract_phone(text)
        skills = extract_skills(text)
        education = extract_education(text)
        experience = extract_experience(text)

        score = calculate_score(skills, experience, education)

        st.success("✅ Resume Processed Successfully!")

        # -------- OUTPUT --------
        
     
        st.markdown("## 👤 Candidate Info")

        st.markdown(f"""
        <div class="card">

        <div class="label">Name</div>
        <div class="value" style="font-size:22px; color:#00ADB5;">👤 {name}</div>

        <div class="label">Email</div>
        <div class="value">
        <a href="mailto:{email}" style="color:#00ADB5; text-decoration:none;">
            📧 {email}
        </a>
        </div>

        <div class="label">Phone</div>
        <div class="value">
        📞 {phone}
        </div>

        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("## 💻 Skills")

        skill_html = "".join([f'<span class="skill">{s}</span>' for s in skills])

        st.markdown(f"""
        <div class="card">
       {skill_html}
       </div>
       """, unsafe_allow_html=True)

        st.markdown("## 🎓 Education")

        education_text = ", ".join(education) if education else "Not Found"

        st.markdown(f"""
       <div class="card">
       {education_text}
       </div>
       """, unsafe_allow_html=True)
       
        st.markdown("## 📅 Experience")

        st.markdown(f"""
        <div class="card">
        {experience}
        </div>
        """, unsafe_allow_html=True)

        
        st.markdown("## 📊 Resume Score")

        st.progress(score / 100)

        st.markdown(f"""
       <div class="card">
       <h2 style="color:#00ADB5;">{score}/100</h2>
       </div>
       """, unsafe_allow_html=True)

        if score >= 70:
            st.success("🔥 Strong Candidate")
        elif score >= 40:
            st.warning("⚠️ Average Candidate")
        else:
            st.error("❌ Weak Candidate")
