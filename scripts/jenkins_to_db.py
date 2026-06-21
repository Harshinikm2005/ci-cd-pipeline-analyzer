import subprocess
import sqlite3

job_name = "hello-devops"

command = f"docker exec jenkins cat /var/jenkins_home/jobs/{job_name}/builds/1/log"

result = subprocess.run(
    command,
    shell=True,
    capture_output=True,
    text=True
)

log_data = result.stdout

status = "Success" if "SUCCESS" in log_data else "Failed"

conn = sqlite3.connect("database/build_logs.db")
cursor = conn.cursor()

cursor.execute(
    """
    INSERT INTO build_results
    (category, severity, suggestion)
    VALUES (?, ?, ?)
    """,
    (
        status,
        "Low",
        "Jenkins build processed automatically"
    )
)

conn.commit()
conn.close()

print("Build result stored successfully.")
