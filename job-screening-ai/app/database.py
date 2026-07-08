# import 
import sqlite3
# create a connection with sqlite database
connection = sqlite3.connect('match.db')
# cursor execute sql queries
cursor = connection.cursor()

# write down the queries
cursor.execute("""
CREATE TABLE IF NOT EXISTS resume(
    id INTEGAR PRIMARY KEY,
    candidate_name TEXT,
    education TEXT,
    Skills TEXT,
    experience_year INT
   )
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS job(
    id INTEGAR PRIMARY KEY,
    job_title TEXT,
    required_skills TEXT,
    required_education TEXT,
    required_experience INT
   )
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS match(
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
# save create table
connection.commit()
# close connection
connection.close()
# print if database tables created
print("database tables are created successfully")