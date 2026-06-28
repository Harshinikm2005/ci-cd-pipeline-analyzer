import sqlite3

conn = sqlite3.connect("database/build_logs.db")
cursor = conn.cursor()

cursor.execute("""
SELECT category, COUNT(*)
FROM build_results
GROUP BY category
ORDER BY COUNT(*) DESC
""")

results = cursor.fetchall()

print("=" * 35)
print("      BUILD ANALYTICS REPORT")
print("=" * 35)

for category, count in results:
    print(f"{category}: {count}")

conn.close()
