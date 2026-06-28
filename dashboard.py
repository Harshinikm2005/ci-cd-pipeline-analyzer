import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="Smart CI/CD Pipeline Analyzer")

st.title("🚀 Smart CI/CD Pipeline Analyzer")

conn = sqlite3.connect("database/build_logs.db")

df = pd.read_sql_query(
    "SELECT * FROM build_results",
    conn
)

# Metrics
total = len(df)
success = len(df[df["category"] == "Success"])
failed = total - success

col1, col2, col3 = st.columns(3)

col1.metric("Total Builds", total)
col2.metric("Successful Builds", success)
col3.metric("Failed Builds", failed)

st.divider()

# Table
st.subheader("Build Records")
st.dataframe(df, use_container_width=True)

st.divider()

# Chart
st.subheader("Build Category Distribution")
st.bar_chart(df["category"].value_counts())
st.subheader("Download Report")

with open("reports/build_report.csv", "rb") as file:
    st.download_button(
        label="Download CSV Report",
        data=file,
        file_name="build_report.csv",
        mime="text/csv"
    )
conn.close()
