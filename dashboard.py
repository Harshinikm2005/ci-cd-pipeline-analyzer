import streamlit as st
import sqlite3
import pandas as pd

st.title("Smart CI/CD Pipeline Analyzer")

conn = sqlite3.connect("database/build_logs.db")

df = pd.read_sql_query(
    "SELECT * FROM build_results",
    conn
)

total = len(df)

success = len(df[df["category"] == "Success"])

failed = total - success

st.metric("Total Builds", total)
st.metric("Success Builds", success)
st.metric("Failed Builds", failed)

st.subheader("Build Records")

st.dataframe(df)

conn.close()
