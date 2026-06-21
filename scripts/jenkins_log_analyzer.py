import subprocess

job_name = "hello-devops"

command = f"docker exec jenkins cat /var/jenkins_home/jobs/{job_name}/builds/1/log"

result = subprocess.run(
    command,
    shell=True,
    capture_output=True,
    text=True
)

log_data = result.stdout

print("===== JENKINS LOG =====")
print(log_data)

if "SUCCESS" in log_data:
    print("\nBuild Status: SUCCESS")
else:
    print("\nBuild Status: FAILED")
