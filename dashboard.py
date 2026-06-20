import streamlit as st
import sqlite3

st.title("Smart CI/CD Pipeline Analyzer")

conn = sqlite3.connect("database/build_logs.db")
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

conn.close()
