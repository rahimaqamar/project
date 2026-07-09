import sqlite3

DATABASE = "match.db"

# -----------------------------
# Create Database Tables
# -----------------------------
# The cursor is the tool that sends SQL queries to the database."
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
# this func insert one resume
def insert_resume(candidate_name, education, skills, experience_year):
#  open database
    connection = sqlite3.connect(DATABASE)
    # create cursor
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO resume
    (candidate_name, education, skills, experience_year)
                # these are paceholders This is called a parameterized query. It safely inserts data 
                # into the database, prevents SQL injection, and automatically handles data types."
                # ?:
    VALUES (?, ?, ?, ?)
                # actual value come from the tuple
    """, (
        candidate_name,
        education,
        skills,
        experience_year
    ))
#   save 
    connection.commit()
    # Insert hone ke turant baad, 
    # tumhe kaise pata chalega ki abhi jo resume daala, uski id kya bani? 1? 5? 10?
    # cursor.lastrowid ka kaam
# Ye ek command hai jo database se poochta hai: "Abhi jo maine last cheez insert ki, uski ID kya bani?"
# database jawab data han
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
    # placeholders
     VALUES (?, ?, ?, ?)
    # tuple han jis ma order wise value dala ghi
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
# Ye ek tuple hai jisme 8 values hain — aur ye tuple cursor.execute() 
# ko query ke saath diya jaata hai, taaki wo 8 ? placeholders ki jagah fill ho sake.
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