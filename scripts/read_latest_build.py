import os

job_name = "python-error"

log_path = f"/var/jenkins_home/jobs/{job_name}/builds/lastSuccessfulBuild/log"

if os.path.exists(log_path):
    with open(log_path, "r") as file:
        print(file.read())
else:
    print("Log file not found")
