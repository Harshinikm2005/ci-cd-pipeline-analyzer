import streamlit as st
import sqlite3
import pandas as pd
import os

st.sidebar.title("⚙️ Dashboard Menu")

page = st.sidebar.selectbox(
    "Select View",
    ["Overview", "Build Records", "Analytics"]
)

st.title("🚀 Smart CI/CD Pipeline Analyzer")
st.caption("Automated Jenkins Build Monitoring & Analytics Dashboard")

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
st.subheader("Build Health")

if failed == 0:
    st.success("✅ All builds are successful.")
else:
    st.warning(f"⚠️ {failed} build(s) need attention.")
# Table
st.subheader("Build Records")

st.dataframe(
    df,
    width="stretch",
    hide_index=True
)
# Chart
st.subheader("Build Category Distribution")
category_counts = df["category"].value_counts()

st.bar_chart(category_counts)


st.subheader("Download Report")

report_path = "reports/build_report.csv"

if os.path.exists(report_path):
    with open(report_path, "rb") as file:
        st.download_button(
            label="Download CSV Report",
            data=file,
            file_name="build_report.csv",
            mime="text/csv"
        )
else:
    st.info("No report available yet. Run the export_report.py script to generate one.")
conn.close()
