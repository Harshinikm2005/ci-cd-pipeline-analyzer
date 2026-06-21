def get_suggestion(log_text):

    log_text = log_text.lower()

    if "syntaxerror" in log_text:
        return "Check Python syntax and indentation."

    elif "modulenotfounderror" in log_text:
        return "Install missing package using pip."

    elif "permission denied" in log_text:
        return "Check file permissions."

    elif "connection refused" in log_text:
        return "Verify service availability and network settings."

    elif "command not found" in log_text:
        return "Install the required command or add it to PATH."

    elif "success" in log_text:
        return "No action required."

    else:
        return "Manual investigation required."
