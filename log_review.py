# Simple log review tool for basic security monitoring practice

keywords = ["failed", "error", "denied", "unauthorized", "alert"]

log_file = "sample-log.txt"

print("Flagged log entries:\n")

try:
    with open(log_file, "r") as file:
        for line in file:
            lower_line = line.lower()
            if any(keyword in lower_line for keyword in keywords):
                print(line.strip())
except FileNotFoundError:
    print(f"Could not find log file: {log_file}")
