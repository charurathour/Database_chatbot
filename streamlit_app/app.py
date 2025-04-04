import streamlit as st
import mysql.connector
from database import get_database_schema, execute_query
from gemini import generate_sql_query

# Streamlit UI Configuration
st.set_page_config(page_title="Database Chatbot", layout="wide")
st.title("🔍 Database Chatbot")
st.write("Enter your database details and query MySQL with natural language.")

# User Inputs for Database Connection
st.sidebar.subheader("⚙️ Database Connection Settings")
host = st.sidebar.text_input("Host", value="localhost")
username = st.sidebar.text_input("Username", value="root")
password = st.sidebar.text_input("Password", type="password")

# Function to fetch available databases
def get_databases(host, username, password):
    try:
        conn = mysql.connector.connect(host=host, user=username, password=password)
        cursor = conn.cursor()
        cursor.execute("SHOW DATABASES")
        databases = [db[0] for db in cursor.fetchall()]
        conn.close()
        return databases
    except mysql.connector.Error as e:
        return [f"Error: {e}"]

# Fetch and select database
if username and password:
    databases = get_databases(host, username, password)
    
    if not databases or "Error" in databases[0]:
        st.sidebar.error(databases[0])
        database = None
    else:
        database = st.sidebar.selectbox("Select Database", databases, index=0)
else:
    database = None

# Proceed only if database is selected
if database:
    # Fetch database schema dynamically
    schema = get_database_schema(host, username, password, database)
    st.subheader("📌 Database Schema")
    st.text_area("Schema Details", schema, height=300)

    # User Query Input
    st.subheader("📝 Ask Your Query")
    user_question = st.text_input("Enter your question in English:")

    if user_question:
        sql_query = generate_sql_query(user_question, schema)
        st.subheader("🟢 Generated SQL Query")
        st.code(sql_query, language="sql")

        # Execute Query
        st.subheader("📌 Query Results")
        columns, data = execute_query(host, username, password, database, sql_query)

        if isinstance(data, list) and data and isinstance(data[0], str) and "Database Error" in data[0]:
            st.error(data[0])
        elif data:
            st.table([columns] + data)
        else:
            st.info("⚠️ No data found.")
