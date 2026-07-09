# use pyadnatic model what data api expect and what data it return
# create a pydantic model for validation
# FastAPI needs to know the structure of the data that users send in API requests. These schema classes define that structure.
from pydantic import BaseModel
# This schema is used when a user submits a resume.
# resume schema
class resume_schema(BaseModel):
    candidate_name:str
    education: str
    skills: str
    experience_year:int
# this schema is use when recuiter create a new job
# job schema
class job_schema(BaseModel):
    job_title: str
    required_education: str
    required_skills: str
    required_experience: int
    required_education: str
    # this schema is use 
# Match Request Schema
# Used when the client asks the API to compare a resume with a job.
class MatchRequest(BaseModel):
    resume_id: int
    job_id: int
# match respond schema
# This schema describes what your API sends back after comparing the resume and job.
class MatchRespond(BaseModel):
    match_score: float
    verdict: str
    matched_skills: list[str]
    missing_skills: list[str]
    status: str
    reason: str


