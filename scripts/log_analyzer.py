log_file = input("Enter log file path: ")

with open(log_file, "r") as file:
    log = file.read()

if "Finished: SUCCESS" in log:
    print("\nBuild Status : SUCCESS")

elif "python: not found" in log:
    print("\nCategory : Environment Error")
    print("Severity : High")
    print("Suggestion : Install Python or fix PATH")

elif "ModuleNotFoundError" in log:
    print("\nCategory : Dependency Error")
    print("Severity : High")
    print("Suggestion : Install missing package")

elif "can't open file" in log:
    print("\nCategory : File Not Found")
    print("Severity : Medium")
    print("Suggestion : Verify filename")

else:
    print("\nCategory : Unknown Error")
    print("Suggestion : Manual investigation required")
