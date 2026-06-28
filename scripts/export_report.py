import sqlite3
import pandas as pd

conn = sqlite3.connect("database/build_logs.db")

df = pd.read_sql_query(
    "SELECT * FROM build_results",
    conn
)

df.to_csv("build_report.csv", index=False)

conn.close()

print("Report exported successfully!")
