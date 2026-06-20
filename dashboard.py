import streamlit as st
import sqlite3
import pandas as pd

st.title("Smart CI/CD Pipeline Analyzer")

conn = sqlite3.connect("database/build_logs.db")

# Metrics
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM build_results")
total = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM build_results WHERE category='Success'")
success = cursor.fetchone()[0]

failed = total - success

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Builds", total)

with col2:
    st.metric("Success Builds", success)

with col3:
    st.metric("Failed Builds", failed)

# Table
st.subheader("Build Records")

df = pd.read_sql_query(
    "SELECT * FROM build_results",
    conn
)

st.dataframe(df)
st.subheader("Build Summary Chart")

chart_data = {
    "Status": ["Success", "Failed"],
    "Count": [success, failed]
}

chart_df = pd.DataFrame(chart_data)

st.bar_chart(
    chart_df.set_index("Status")
)
conn.close()
