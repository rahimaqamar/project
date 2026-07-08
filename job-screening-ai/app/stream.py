import streamlit as st
import requests

# FastAPI URL
API_URL = "http://127.0.0.1:8000"

st.title("TalentMatch")
st.subheader("Resume Screening System")

# -----------------------------
# Upload Resume
# -----------------------------

st.header("Upload Resume")

candidate_name = st.text_input("Candidate Name")
education = st.text_input("Education")
skills = st.text_input("Skills (comma separated)")
experience = st.number_input(
    "Experience (Years)",
    min_value=0,
    step=1
)

if st.button("Upload Resume"):

    response = requests.post(
        f"{API_URL}/resume",
        json={
            "candidate_name": candidate_name,
            "education": education,
            "skills": skills,
            "experience_years": experience
        }
    )

    if response.status_code == 200:
        st.success("Resume Uploaded Successfully")
        st.json(response.json())
    else:
        st.error(response.text)

# -----------------------------
# Upload Job
# -----------------------------

st.header("Upload Job")

job_title = st.text_input("Job Title")
required_skills = st.text_input("Required Skills")
required_experience = st.number_input(
    "Required Experience",
    min_value=0,
    step=1,
    key="job"
)

if st.button("Upload Job"):

    response = requests.post(
        f"{API_URL}/jobs",
        json={
            "job_title": job_title,
            "required_skills": required_skills,
            "required_experience": required_experience
        }
    )

    if response.status_code == 200:
        st.success("Job Uploaded Successfully")
        st.json(response.json())
    else:
        st.error(response.text)

# -----------------------------
# Match Resume
# -----------------------------

st.header("Match Resume")

resume_id = st.number_input(
    "Resume ID",
    min_value=1,
    step=1
)

job_id = st.number_input(
    "Job ID",
    min_value=1,
    step=1
)

if st.button("Match Resume"):

    response = requests.post(
        f"{API_URL}/match",
        json={
            "resume_id": resume_id,
            "job_id": job_id
        }
    )

    if response.status_code == 200:

        result = response.json()

        st.success("Matching Completed")

        st.write("### Match Score")
        st.write(result["match_score"])

        st.write("### Verdict")
        st.write(result["verdict"])

        st.write("### Matched Skills")
        st.write(result["matched_skills"])

        st.write("### Missing Skills")
        st.write(result["missing_skills"])

    else:
        st.error(response.text)

# -----------------------------
# View Candidates
# -----------------------------

st.header("View Candidates")

candidate_job_id = st.number_input(
    "Job ID",
    min_value=1,
    step=1,
    key="candidate"
)

if st.button("Show Candidates"):

    response = requests.get(
        f"{API_URL}/jobs/{candidate_job_id}/candidates"
    )

    if response.status_code == 200:
        st.json(response.json())
    else:
        st.error(response.text)