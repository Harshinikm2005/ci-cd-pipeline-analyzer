import sqlite3

log_file = input("Enter log file path: ")

with open(log_file, "r") as f:
    log = f.read()

category = "Unknown Error"
severity = "Low"
suggestion = "Check logs manually"

if "Finished: SUCCESS" in log:
    category = "Success"
    severity = "None"
    suggestion = "No action required"

elif "python: not found" in log:
    category = "Environment Error"
    severity = "High"
    suggestion = "Install Python or fix PATH"

elif "can't open file" in log:
    category = "File Not Found"
    severity = "Medium"
    suggestion = "Verify filename and path"

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

cursor.execute("""
INSERT INTO build_results(category,severity,suggestion)
VALUES (?,?,?)
""", (category, severity, suggestion))

conn.commit()

print("\nAnalysis Complete")
print("Category :", category)
print("Severity :", severity)
print("Suggestion :", suggestion)
print("Path entered:", repr(log_path))
conn.close()
