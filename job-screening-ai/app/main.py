from fastapi import FastAPI
from schemas import (
    job_schema,
    resume_schema,
    MatchRequest,
    MatchRespond,
)
from database import (
    insert_resume,
    insert_job,
    get_resume,
    get_job,
    insert_match
)

app = FastAPI(title="TalentMatch API", version="1.0")


@app.get("/")
def home():
    return {"message": "Welcome to TalentMatch API"}


# ---------- Upload Resume ----------
@app.post("/resume")
def create_resume(resume: resume_schema):
    resume_id = insert_resume(
        resume.candidate_name,
        resume.education,
        resume.skills,
        resume.experience_year
    )
    return {
        "message": "Resume uploaded successfully",
        "resume_id": resume_id,
        "data": resume
    }


# ---------- Create Job ----------
@app.post('/jobs')
def create_job(job: job_schema):
    job_id = insert_job(
        job.job_title,
        job.required_skills,
        job.required_education,
        job.required_experience
    )
    return {
        "message": "Job created successfully",
        "job_id": job_id,
        "data": job
    }


# ---------- Match Resume and Job ----------
@app.post("/match", response_model=MatchRespond)
def match_resume(request: MatchRequest):

    resume = get_resume(request.resume_id)   # DB se fetch (tuple return hota hai)
    job = get_job(request.job_id)

    if resume is None or job is None:
        return MatchRespond(
            match_score=0,
            verdict="Rejected",
            matched_skills=[],
            missing_skills=[],
            status="Failed",
            reason="Resume or Job not found"
        )

    # tuple index se columns nikalna: (id, candidate_name, education, skills, experience_year)
    resume_skills_str = resume[3]
    # job tuple: (id, job_title, required_skills, required_education, required_experience)
    job_skills_str = job[2]

    resume_skills = [s.strip().lower() for s in resume_skills_str.split(",")]
    job_skills = [s.strip().lower() for s in job_skills_str.split(",")]

    matched = [s for s in resume_skills if s in job_skills]
    missing = [s for s in job_skills if s not in resume_skills]

    score = (len(matched) / len(job_skills)) * 100 if job_skills else 0
    verdict = "Accepted" if score >= 60 else "Rejected"

    # ---- Match result ko bhi DB mein save karo ----
    insert_match(
        request.resume_id,
        request.job_id,
        round(score, 2),
        verdict,
        ",".join(matched),
        ",".join(missing),
        "Success",
        "Matching completed successfully"
    )

    return MatchRespond(
        match_score=round(score, 2),
        verdict=verdict,
        matched_skills=matched,
        missing_skills=missing,
        status="Success",
        reason="Matching completed successfully"
    )