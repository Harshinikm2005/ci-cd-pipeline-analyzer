import os

job_name = "hello-devops"

builds_path = f"/var/jenkins_home/jobs/{job_name}/builds"

if not os.path.exists(builds_path):
    print("Job not found")
    exit()

builds = [d for d in os.listdir(builds_path) if d.isdigit()]

if not builds:
    print("No builds found")
    exit()

latest_build = max(builds, key=int)

print("Latest Build:", latest_build)
