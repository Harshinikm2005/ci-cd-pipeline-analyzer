log_path = input("Enter Jenkins log path: ")

try:
    with open(log_path, "r") as file:
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
        print("Suggestion : Check filename and path")

    else:
        print("\nCategory : Unknown Error")

except FileNotFoundError:
    print("Error: Log file not found")
