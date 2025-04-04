import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

def generate_sql_query(question, schema):
    """
    Uses Gemini AI to generate an SQL query based on a natural language question.
    """
    prompt = f"""
You are an AI SQL assistant. Convert the following English question into a MySQL query.
Database Schema:
{schema}
User's question: {question}
Generate only the SQL query without explanation and without ```sql```
"""

    model = genai.GenerativeModel("gemini-1.5-pro-001")
    response = model.generate_content(prompt)
    

    return response.text.strip()
