log_file = input("Enter log file path: ")

with open(log_file, "r") as f:
    log = f.read()

if "Finished: SUCCESS" in log:
    print("\nBuild Status : SUCCESS")

elif "python: not found" in log:
    print("\nCategory : Environment Error")
    print("Severity : High")
    print("Suggestion : Install Python or fix PATH")

elif "can't open file" in log:
    print("\nCategory : File Not Found")
    print("Severity : Medium")
    print("Suggestion : Verify filename and path")

elif "ModuleNotFoundError" in log:
    print("\nCategory : Dependency Error")
    print("Severity : High")
    print("Suggestion : Install missing Python package")

elif "docker: command not found" in log:
    print("\nCategory : Docker Error")
    print("Severity : High")
    print("Suggestion : Install Docker")

else:
    print("\nCategory : Unknown Error")
    print("Suggestion : Check build logs manually")
