import sqlite3

conn = sqlite3.connect("database/build_logs.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS build_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT,
    severity TEXT,
    suggestion TEXT
)
""")

category = "Environment Error"
severity = "High"
suggestion = "Install Python or fix PATH"

cursor.execute("""
INSERT INTO build_results(category,severity,suggestion)
VALUES (?,?,?)
""", (category, severity, suggestion))

conn.commit()

print("Data inserted successfully!")

conn.close()
