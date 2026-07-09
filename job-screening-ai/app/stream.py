# st is use to call streamlit function
import streamlit as st
# request libarary use to communicate with fast api
import requests
# fastapi server request
API_URL = "http://127.0.0.1:8000"

st.title("TalentMatch — Resume Upload")

tab1, tab2, tab3 = st.tabs(["Upload Resume", "Create Job", "Match"])

# ---------- Tab 1: Resume Form ----------
with tab1:
    name = st.text_input("Candidate Name")
    education = st.text_input("Education")
    skills = st.text_input("Skills (comma separated)")
    experience = st.number_input("Experience (years)", min_value=0, step=1)

    if st.button("Submit Resume"):
        payload = {
            "candidate_name": name,
            "education": education,
            "skills": skills,
            "experience_year": experience
        }
        response = requests.post(f"{API_URL}/resume", json=payload)
        if response.status_code == 200:
            result = response.json()
            st.success(result)
            st.info(f"📌 Resume ID: {result['resume_id']}")
        else:
            st.error(f"Error: {response.text}")

# ---------- Tab 2: Job Form ----------
with tab2:
    job_title = st.text_input("Job Title")
    req_education = st.text_input("Required Education")
    req_skills = st.text_input("Required Skills (comma separated)")
    req_experience = st.number_input("Required Experience", min_value=0, step=1)

    if st.button("Submit Job"):
        payload = {
            "job_title": job_title,
            "required_education": req_education,
            "required_skills": req_skills,
            "required_experience": req_experience
        }
        response = requests.post(f"{API_URL}/jobs", json=payload)
        if response.status_code == 200:
            result = response.json()
            st.success(result)
            st.info(f"📌 Job ID: {result['job_id']}")
        else:
            st.error(f"Error: {response.text}")

# ---------- Tab 3: Match ----------
with tab3:
    resumes = requests.get(f"{API_URL}/resumes").json()
    jobs = requests.get(f"{API_URL}/jobs").json()

    if not resumes or not jobs:
        st.warning("Pehle kam se kam ek resume aur ek job submit karo")
    else:
        resume_options = {
            f"ID {r['id']} — {r['candidate_name']}": r['id']
            for r in resumes
        }
        job_options = {
            f"ID {j['id']} — {j['job_title']}": j['id']
            for j in jobs
        }

        selected_resume = st.selectbox("Select Resume", list(resume_options.keys()))
        selected_job = st.selectbox("Select Job", list(job_options.keys()))

        resume_id = resume_options[selected_resume]
        job_id = job_options[selected_job]

        if st.button("Run Match"):
            payload = {"resume_id": resume_id, "job_id": job_id}
            response = requests.post(f"{API_URL}/match", json=payload)
            if response.status_code == 200:
                st.json(response.json())
            else:
                st.error(f"Error: {response.text}")