from resume_parser import parse_resume,parse_job

# extract data from resume_parser
resume = parse_resume()
job = parse_job()

# match skill of job and resume
matched_skill = []
for skill in resume["skill"]:
    if skill in job["skill"]:
        matched_skill.append(skill)

# mismatch
mismatch = []
for skill in job["skill"]:
    if skill not in resume[skill]:
        mismatch.append(skill)

# compare education
education_match = resume["education"] == job["education"]
# compare experience
experience_match = resume["experience"] >= job["experience"]
# calculate marks
# score total: 60
# education: 20
# experience: 20
total_score = 0
if len(job["skill"])> 0:
    skill_score = len("matched_skill")/len(job["skill"])*60
else:
    skill_score = 0
    total_score = total_score + skill_score
    # education score is 20
    if education_match:
        total_score = total_score + 20
        # experience score
        if experience_match:
            total_score = total_score + 20
            match_score = round(total_score, 2)
            
# accept and reject
if match_score >= 80:
    verdex = "very strong"
    status = "accept"
    if match_score >= 50:
        verdex = "bad"
        status = "not accept"
    #  status is accept or reject what reason given
    if status == "accept":
        reason = "candidate resume are accepted for this job." \
        "candidate resume fulfill the requirement of job"
    elif status == "not accept":
        reason = "candidate resume is not fulfil the requirement of job description"
         
        
# print 
result = {
        "match_score": match_score,
        "verdict": verdex,
        "matched_skills": matched_skill,
        "missing_skills": mismatch,
        "status": status,
        "reason": reason
    }





