import csv
import datetime
import os

# Define filename
LOG_FILE = "test_log.csv"

# Current timestamp in UTC
timestamp = datetime.datetime.utcnow().isoformat()

# Does the log file already exist?
file_exists = os.path.isfile(LOG_FILE)

# Append to CSV
with open(LOG_FILE, "a", newline="") as f:
    writer = csv.writer(f)

    # Write header only once
    if not file_exists:
        writer.writerow(["timestamp", "message"])

    writer.writerow([timestamp, "GitHub Action run successful"])

print("==========================================")
print("🔥 CSV LOGGING TEST SUCCESSFUL 🔥")
print(f"Wrote entry at {timestamp}")
print("==========================================")
