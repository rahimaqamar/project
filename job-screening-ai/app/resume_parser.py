# regular expression use for pattern matching
import re
# pathlib Python ka module hai file aur folder paths handle karne ke liye.
from pathlib import Path

# Project Folder
# __file__ build in variable .py automatically available. current file ka path store hota han
BASE_DIR = Path(__file__).resolve().parent.parent

# File Paths
RESUME_FILE = BASE_DIR / "uploads" / "resume.txt"
JOB_FILE = BASE_DIR / "uploads" / "job_description.txt"

# -----------------------------
# Skills List
# -----------------------------
# reference list just like dict
SKILLS = [
    "Python",
    "FastAPI",
    "SQL",
    "PostgreSQL",
    "Docker",
    "REST API",
    "Git",
    "Java",
    "C++"
]

# -----------------------------
# Education List
# -----------------------------
EDUCATION = [
    "BS Computer Science",
    "BSc Computer Science",
    "Bachelor",
    "Master",
    "MS Computer Science"
]

# -----------------------------
# Read Resume File
# -----------------------------
def read_resume():
    with open(RESUME_FILE, "r", encoding="utf-8") as file:
        return file.read()

# -----------------------------
# Read Job Description File
# -----------------------------
def read_job():
    with open(JOB_FILE, "r", encoding="utf-8") as file:
        return file.read()

# -----------------------------
# Extract Skills
# -----------------------------
# membership check value exsist inside list tuple
# in or not in
# text is usually complete resume and job description
def extract_skills(text):
    skills = []

    for skill in SKILLS:
        if skill.lower() in text.lower():
            skills.append(skill)

    return skills

# -----------------------------
# Extract Education
# -----------------------------
def extract_education(text):

    for education in EDUCATION:
        if education.lower() in text.lower():
            return education

    return "Not Found"

# -----------------------------
# Extract Experience
# -----------------------------
def extract_experience(text):

    match = re.search(r"(\d+)\s+years?", text.lower())

    if match:
        return int(match.group(1))

    return 0

# -----------------------------
# Parse Resume
# -----------------------------
def parse_resume():

    resume_text = read_resume()

    return {
        "skills": extract_skills(resume_text),
        "education": extract_education(resume_text),
        "experience": extract_experience(resume_text)
    }

# -----------------------------
# Parse Job Description
# -----------------------------
def parse_job():

    job_text = read_job()

    return {
        "skills": extract_skills(job_text),
        "education": extract_education(job_text),
        "experience": extract_experience(job_text)
    }

# -----------------------------
# Test
# -----------------------------
# every python file has build in variable 
# Python automatically gives it a value.
# The value depends on how the file is used
if __name__ == "__main__":

    print("Resume Data")
    print(parse_resume())

    print("\nJob Description Data")
    print(parse_job())