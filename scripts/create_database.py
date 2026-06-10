import sqlite3

conn = sqlite3.connect("database/build_logs.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS build_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_name TEXT,
    build_number INTEGER,
    status TEXT,
    category TEXT,
    severity TEXT,
    suggestion TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()

print("Database Created Successfully")

conn.close()
