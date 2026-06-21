import subprocess
import sqlite3

job_name = "hello-devops"

conn = sqlite3.connect("database/build_logs.db")
cursor = conn.cursor()

# Get all Jenkins builds
result = subprocess.run(
    f"docker exec jenkins ls /var/jenkins_home/jobs/{job_name}/builds",
    shell=True,
    capture_output=True,
    text=True
)

builds = [int(x) for x in result.stdout.split() if x.isdigit()]

for build in builds:

    cursor.execute(
        "SELECT * FROM processed_builds WHERE build_number=?",
        (build,)
    )

    if cursor.fetchone():
        continue

    log_result = subprocess.run(
        f"docker exec jenkins cat /var/jenkins_home/jobs/{job_name}/builds/{build}/log",
        shell=True,
        capture_output=True,
        text=True
    )

    log_data = log_result.stdout

    status = "Success" if "SUCCESS" in log_data else "Failed"

    cursor.execute(
        """
        INSERT INTO build_results
        (category, severity, suggestion)
        VALUES (?, ?, ?)
        """,
        (
            status,
            "Low",
            f"Build #{build} processed automatically"
        )
    )

    cursor.execute(
        "INSERT INTO processed_builds VALUES (?)",
        (build,)
    )

    print(f"Processed Build #{build}")

conn.commit()
conn.close()
