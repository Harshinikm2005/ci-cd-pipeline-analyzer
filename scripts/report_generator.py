import sqlite3

conn = sqlite3.connect("database/build_logs.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM build_results")
total_builds = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM build_results WHERE category='Success'")
success_builds = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM build_results WHERE category!='Success'")
failed_builds = cursor.fetchone()[0]

print("\n===== BUILD REPORT =====")
print("Total Builds      :", total_builds)
print("Successful Builds :", success_builds)
print("Failed Builds     :", failed_builds)

conn.close()
