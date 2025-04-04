🗄️ Database Chatbot – AI-Powered SQL Query Assistant (MySQL)

🚀 Overview
Database Chatbot is an AI-powered tool that converts natural language questions into SQL queries and executes them on a MySQL database. It allows users to interact with their database easily using a conversational interface.

🎯 Features
MySQL Support: Connects securely to any MySQL database.

Schema Extraction: Automatically retrieves the database schema for better query generation.

AI-Powered Query Generation: Uses Gemini AI to generate SQL queries from English questions.

Live Query Execution: Runs SQL queries directly on the database and displays results.

User Authentication: Securely connects using user-provided credentials.

Streamlit UI: Simple and interactive web-based interface.

🛠️ Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-repo/database-chatbot.git  
cd database-chatbot  
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt  
Set up environment variables:
Create a .env file with:

ini
Copy
Edit
GEMINI_API_KEY=your_gemini_api_key  
▶️ Usage
Run the chatbot:

bash
Copy
Edit
streamlit run app.py  
Enter your MySQL database credentials (host, username, password).

Select a database from the available list.

Ask a question in English, and the chatbot will generate and execute an SQL query.

📌 Example
User Input: "Show me all orders placed in the last 30 days."
Generated SQL Query:

sql
Copy
Edit
SELECT * FROM orders WHERE order_date >= NOW() - INTERVAL 30 DAY;
Displayed Output: Table of orders from the last 30 days.
