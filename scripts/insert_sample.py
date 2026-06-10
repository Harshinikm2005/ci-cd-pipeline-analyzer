import sqlite3

conn = sqlite3.connect("database/build_logs.db")
cursor = conn.cursor()

cursor.execute("""
INSERT INTO build_results
(job_name, build_number, status, category, severity, suggestion)
VALUES
('python-error',1,'FAILURE',
 'Environment Error',
 'High',
 'Install Python or fix PATH')
""")

conn.commit()

print("Record Inserted")

conn.close()
