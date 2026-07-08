import sqlite3

connection = sqlite3.connect("match.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM resume")

rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()