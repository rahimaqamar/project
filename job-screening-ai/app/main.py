from fastapi import FastAPI
from schemas import (
    job_schema,
    resume_schema,
    MatchRequest,
    MatchRespond,
)
app = FastAPI(
    title="TalentMatch API",
    version="1.0"
)

# Store data temporarily
resume_data = {}
job_data = {}


# Home API
@app.get("/")
def home():
    return {"message": "Welcome to TalentMatch API"}

# Upload Resume
@app.post("/resume")
# resume contain the requested body 
# resume_schema tells FastAPI to validate the incoming JSON.
# def → Defines a function.
# create_resume → Function name.
# resume → Parameter that receives data from the client.
# resume: resume_schema → Type hint telling FastAPI that resume must follow the resume_schema Pydantic model.
def create_resume(resume: resume_schema):
# id above
    resume_id = len(resume_data) + 1
    # store data in dict
    resume_data[resume_id] = resume

    return {
        "message": "Resume uploaded successfully",
        "resume_id": resume_id,
        "data": resume
    }

# Create Job
def create_job(job: job_schema):

    job_id = len(job_data) + 1
    job_data[job_id] = job

    return {
        "message": "Job created successfully",
        "job_id": job_id,
        "data": job
    }
# Match Resume and Job
@app.post("/match", response_model=MatchRespond)
def match_resume(request: MatchRequest):

    resume = resume_data.get(request.resume_id)
    job = job_data.get(request.job_id)

    if resume is None or job is None:
        return MatchRespond(
            match_score=0,
            verdict="Rejected",
            matched_skills=[],
            missing_skills=[],
            status="Failed",
            reason="Resume or Job not found"
        )

    # Convert skills into lists
    resume_skills = [
        skill.strip().lower()
        for skill in resume.skills.split(",")
    ]

    job_skills = [
        skill.strip().lower()
        for skill in job.required_skills.split(",")
    ]

    matched = [
        skill
        for skill in resume_skills
        if skill in job_skills
    ]

    missing = [
        skill
        for skill in job_skills
        if skill not in resume_skills
    ]

    score = (len(matched) / len(job_skills)) * 100

    verdict = "Accepted" if score >= 60 else "Rejected"

    return MatchRespond(
        match_score=round(score, 2),
        verdict=verdict,
        matched_skills=matched,
        missing_skills=missing,
        status="Success",
        reason="Matching completed successfully"
    )