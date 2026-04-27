import re
import io
import spacy
from pdfminer.high_level import extract_text as pdf_extract_text
from docx import Document

# -------------------- LOAD MODEL --------------------
nlp = spacy.load("en_core_web_sm")

# -------------------- SKILLS --------------------
TECH_SKILLS = [
    "python", "java", "c++", "javascript", "react", "node.js",
    "django", "flask", "sql", "mysql", "mongodb",
    "aws", "azure", "docker", "git",
    "machine learning", "data science", "nlp",
    "pandas", "numpy", "tensorflow","Keras","SQLite"
]

# -------------------- TEXT EXTRACTION --------------------
def extract_text(uploaded_file):
    if uploaded_file.type == "application/pdf":
        file_bytes = uploaded_file.read()
        return pdf_extract_text(io.BytesIO(file_bytes))

    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = Document(uploaded_file)
        return "\n".join([p.text for p in doc.paragraphs])

    return ""

# -------------------- NAME --------------------
def extract_name(text):
    doc = nlp(text[:5000])
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return "Not Found"

# -------------------- EMAIL --------------------
def extract_email(text):
    match = re.search(r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}", text)
    return match.group(0) if match else "Not Found"

# -------------------- PHONE --------------------
def extract_phone(text):
    match = re.search(r"(\+?\d[\d\s\-]{8,15})", text)
    return match.group(0) if match else "Not Found"

# -------------------- SKILLS --------------------
def extract_skills(text):
    text = text.lower()
    found = [skill for skill in TECH_SKILLS if skill in text]
    return list(set(found))

# -------------------- EDUCATION --------------------
def extract_education(text):
    degrees = re.findall(r"(B\.Tech|M\.Tech|BSc|MSc|MBA|PhD)", text, re.I)
    return list(set(degrees))
    

# -------------------- EXPERIENCE --------------------
def extract_experience(text):
    years = re.findall(r"\b(20\d{2}|19\d{2})\b", text)
    if len(years) >= 2:
        return str(max(map(int, years)) - min(map(int, years))) + " years"
    return "0 years"

# -------------------- SCORE --------------------
def calculate_score(skills, experience, education):
    score = 0

    score += len(skills) * 5

    try:
        exp = int(experience.split()[0])
        score += exp * 10
    except:
        pass

    score += len(education) * 5

    return min(score, 100)