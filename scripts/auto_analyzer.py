import sqlite3

log_path = input("Enter Jenkins log path: ")

try:
    with open(log_path, "r") as file:
        log = file.read()

    category = "Unknown Error"
    severity = "Low"
    suggestion = "Manual Investigation"

    if "Finished: SUCCESS" in log:
        category = "Success"
        severity = "None"
        suggestion = "No action required"

    elif "python: not found" in log:
        category = "Environment Error"
        severity = "High"
        suggestion = "Install Python or fix PATH"

    elif "ModuleNotFoundError" in log:
        category = "Dependency Error"
        severity = "High"
        suggestion = "Install missing package"

    elif "can't open file" in log:
        category = "File Not Found"
        severity = "Medium"
        suggestion = "Check filename and path"

    conn = sqlite3.connect("database/build_logs.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS build_results(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT,
        severity TEXT,
        suggestion TEXT
    )
    """)

    cursor.execute("""
    INSERT INTO build_results(category,severity,suggestion)
    VALUES(?,?,?)
    """, (category, severity, suggestion))

    conn.commit()

    print("\nAnalysis Saved Successfully")
    print("Category :", category)
    print("Severity :", severity)

    conn.close()

except FileNotFoundError:
    print("Log file not found")
