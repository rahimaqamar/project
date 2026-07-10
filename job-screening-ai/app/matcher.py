from resume_parser import parse_resume, parse_job
def match_resume_to_job(resume_id, job_id):
    """
    Compares one resume with one job and returns a match result dict.
    IMPORTANT: parse_resume/parse_job ab resume_id/job_id maangte hain,
    taaki pata chale EXACTLY kaunsa resume aur kaunsa job compare karna hai.
    """

    # -----------------------------
    # Step 1: Extract data
    # -----------------------------
    resume = parse_resume(resume_id)
    job = parse_job(job_id)

    # ⚠️ NOTE: Agar tumhare resume_parser.py mein key "skills" hai
    # (na ki "skill"), to neeche har jagah resume["skill"] -> resume["skills"]
    # aur job["skill"] -> job["skills"] kar dena.

    # -----------------------------
    # Step 2: Match skills
    # -----------------------------
    matched_skill = []
    for skill in resume["skill"]:
        if skill in job["skill"]:
            matched_skill.append(skill)

    # -----------------------------
    # Step 3: Missing skills
    # -----------------------------
    mismatch = []
    for skill in job["skill"]:
        if skill not in resume["skill"]:
            mismatch.append(skill)

    # -----------------------------
    # Step 4: Compare education & experience
    # -----------------------------
    education_match = resume["education"] == job["education"]
    experience_match = resume["experience"] >= job["experience"]

    # -----------------------------
    # Step 5: Calculate score
    # Total = 100
    # skills: 60 | education: 20 | experience: 20
    # -----------------------------
    if len(job["skill"]) > 0:
        # BUG FIX: len(matched_skill) not len("matched_skill")
        skill_score = len(matched_skill) / len(job["skill"]) * 60
    else:
        skill_score = 0

    total_score = 0
    # BUG FIX: yeh sab lines pehle 'else' block ke andar trapped thi.
    # Ab yeh har case mein chalengi, sirf skill_score == 0 case mein nahi.
    total_score = total_score + skill_score

    if education_match:
        total_score = total_score + 20

    if experience_match:
        total_score = total_score + 20

    match_score = round(total_score, 2)

    # -----------------------------
    # Step 6: Verdict (accept / reject)
    # BUG FIX: elif use kiya hai, taaki ek hi condition lage,
    # dusri se overwrite na ho.
    # -----------------------------
    if match_score >= 80:
        verdict = "very strong"
        status = "accept"
    elif match_score >= 50:
        verdict = "moderate"
        status = "not accept"
    else:
        verdict = "weak"
        status = "not accept"

    # -----------------------------
    # Step 7: Reason
    # -----------------------------
    if status == "accept":
        reason = (
            "Candidate resume is accepted for this job. "
            "Candidate resume fulfills the requirement of job."
        )
    else:
        reason = "Candidate resume does not fulfill the requirement of job description."

    # -----------------------------
    # Step 8: Final result
    # -----------------------------
    result = {
        "match_score": match_score,
        "verdict": verdict,
        "matched_skills": matched_skill,
        "missing_skills": mismatch,
        "status": status,
        "reason": reason
    }

    return result