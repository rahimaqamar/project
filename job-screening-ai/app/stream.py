import streamlit as st
import requests

# -----------------------------
# FastAPI URL
# -----------------------------
API_URL = "http://127.0.0.1:8000"

# -----------------------------
# Page Title

st.title("TalentMatch")
st.subheader("Resume tracing System")


# Upload Resume
st.header("Upload Resume")

candidate_name = st.text_input("Candidate Name")
education = st.text_input("Education")
skills = st.text_input("Skills (Comma Separated)")
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
            "experience_year": experience
        }
    )

    if response.status_code == 200:

        data = response.json()

        st.success("Resume Uploaded Successfully")

        st.write("### Resume ID")
        st.write(data["resume_id"])

    else:
        st.error(response.text)

# =====================================================
# Upload Job Description
# =====================================================

st.header("Upload Job Description")

job_title = st.text_input("Job Title")

required_skills = st.text_input(
    "Required Skills (Comma Separated)"
)

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

        data = response.json()

        st.success("Job Uploaded Successfully")

        st.write("### Job ID")
        st.write(data["job_id"])

    else:
        st.error(response.text)

# =====================================================
# Match Resume
# =====================================================

st.header("Match Resume With Job")

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

        st.success("Matching Completed Successfully")

        st.divider()

        st.subheader("Matched Skills")

        if result["matched_skills"]:
            for skill in result["matched_skills"]:
                st.write("✅", skill)
        else:
            st.write("No matched skills")

        st.divider()

        st.subheader("Missing Skills")

        if result["missing_skills"]:
            for skill in result["missing_skills"]:
                st.write("❌", skill)
        else:
            st.write("No missing skills")

        st.divider()

        st.subheader("Match Score")

        st.metric(
            label="Score",
            value=f'{result["match_score"]}%'
        )

        st.divider()

        st.subheader("Resume Verdict")

        if result["verdict"] == "Accepted":
            st.success("✅ Resume Accepted")
        else:
            st.error("❌ Resume Rejected")

        st.divider()

        st.subheader("Status")

        st.info(result["status"])

        st.divider()

        st.subheader("Reason")

        st.write(result["reason"])

    else:
        st.error(response.text)

# =====================================================
# View Candidates
# =====================================================

st.header("View Candidates")

candidate_job_id = st.number_input(
    "Enter Job ID",
    min_value=1,
    step=1,
    key="candidate"
)

if st.button("Show Candidates"):

    response = requests.get(
        f"{API_URL}/jobs/{candidate_job_id}/candidates"
    )

    if response.status_code == 200:

        data = response.json()

        st.subheader("Candidates")

        st.table(data["candidates"])

    else:
        st.error(response.text)