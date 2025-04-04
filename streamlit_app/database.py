import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get MySQL credentials
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DB = os.getenv("MYSQL_DB")

def get_database_schema(host, user, password, database):
    """
    Fetches MySQL database schema dynamically based on user input.
    Returns a formatted string containing table structures.
    """
    schema = ""
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        cursor = conn.cursor()

        cursor.execute("SHOW TABLES")
        tables = [table[0] for table in cursor.fetchall()]

        for table in tables:
            cursor.execute(f"DESCRIBE {table}")
            schema += f"🔹 **{table}**\n"
            for row in cursor.fetchall():
                schema += f"   - {row[0]} ({row[1]})\n"
            schema += "\n"

        cursor.close()
        conn.close()

    except mysql.connector.Error as e:
        schema = f"❌ Error fetching schema: {e}"
    
    return schema


def execute_query(host, user, password, database, sql_query):
    """
    Executes the given SQL query on the specified MySQL database.
    Returns column names and rows as a list.
    """
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        cursor = conn.cursor()

        cursor.execute(sql_query)
        rows = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description] if cursor.description else []

        cursor.close()
        conn.close()

        return column_names, rows

    except mysql.connector.Error as e:
        return [], [f"❌ Database Error: {e}"]