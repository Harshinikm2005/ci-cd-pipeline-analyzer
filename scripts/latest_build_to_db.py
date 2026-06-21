import subprocess
import sqlite3

job_name = "hello-devops"

# Find latest build number
command = f"docker exec jenkins ls /var/jenkins_home/jobs/{job_name}/builds"

result = subprocess.run(
    command,
    shell=True,
    capture_output=True,
    text=True
)

builds = []

for item in result.stdout.split():
    if item.isdigit():
        builds.append(int(item))

latest_build = max(builds)

print("Latest Build:", latest_build)

# Read latest build log
log_command = f"docker exec jenkins cat /var/jenkins_home/jobs/{job_name}/builds/{latest_build}/log"

log_result = subprocess.run(
    log_command,
    shell=True,
    capture_output=True,
    text=True
)

log_data = log_result.stdout

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
        f"Build #{latest_build} processed"
    )
)

conn.commit()
conn.close()

print("Stored latest build successfully.")
