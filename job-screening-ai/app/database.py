import sqlite3

DATABASE = "match.db"

# -----------------------------
# Create Database Tables
# -----------------------------
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS resume(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    candidate_name TEXT,
    education TEXT,
    skills TEXT,
    experience_year INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS job(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_title TEXT,
    required_skills TEXT,
    required_education TEXT,
    required_experience INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS match_result(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    resume_id INTEGER,
    job_id INTEGER,
    match_score REAL,
    verdict TEXT,
    matched_skills TEXT,
    missing_skills TEXT,
    status TEXT,
    reason TEXT
)
""")

connection.commit()
connection.close()

print("Database tables created successfully.")


# -----------------------------
# Insert Resume
# -----------------------------
def insert_resume(candidate_name, education, skills, experience_year):

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO resume
    (candidate_name, education, skills, experience_year)
    VALUES (?, ?, ?, ?)
    """, (
        candidate_name,
        education,
        skills,
        experience_year
    ))

    connection.commit()
    resume_id = cursor.lastrowid
    connection.close()

    return resume_id


# -----------------------------
# Insert Job
# -----------------------------
def insert_job(job_title,
               required_skills,
               required_education,
               required_experience):

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO job
    (job_title,
     required_skills,
     required_education,
     required_experience)

    VALUES (?, ?, ?, ?)
    """, (
        job_title,
        required_skills,
        required_education,
        required_experience
    ))

    connection.commit()
    job_id = cursor.lastrowid
    connection.close()

    return job_id


# -----------------------------
# Get Resume By ID
# -----------------------------
def get_resume(resume_id):

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM resume WHERE id=?",
        (resume_id,)
    )

    data = cursor.fetchone()
    connection.close()

    return data


# -----------------------------
# Get Job By ID
# -----------------------------
def get_job(job_id):

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM job WHERE id=?",
        (job_id,)
    )

    data = cursor.fetchone()
    connection.close()

    return data


# -----------------------------
# Get All Resumes
# -----------------------------
def get_all_resumes():

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM resume")
    data = cursor.fetchall()
    connection.close()

    return data


# -----------------------------
# Get All Jobs
# -----------------------------
def get_all_jobs():

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM job")
    data = cursor.fetchall()
    connection.close()

    return data


# -----------------------------
# Save Match Result
# -----------------------------
def insert_match(
    resume_id,
    job_id,
    match_score,
    verdict,
    matched_skills,
    missing_skills,
    status,
    reason
):

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO match_result
    (
        resume_id,
        job_id,
        match_score,
        verdict,
        matched_skills,
        missing_skills,
        status,
        reason
    )

    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        resume_id,
        job_id,
        match_score,
        verdict,
        matched_skills,
        missing_skills,
        status,
        reason
    ))

    connection.commit()
    connection.close()