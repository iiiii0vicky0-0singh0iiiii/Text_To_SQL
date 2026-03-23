import streamlit as st
import os
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain_openai import OpenAI
from utils import setup_database

# --- PATH RESOLUTION FIX ---
# Get the absolute path of the current directory (src)
current_dir = os.path.dirname(os.path.abspath(__file__))

parent_dir = os.path.dirname(current_dir)

# 1. Load environment variables (gets your API Key from the .env file)
load_dotenv(os.path.join(parent_dir, '.env'))

# 2. Page Configuration
st.set_page_config(page_title="Text-to-SQL Assistant", page_icon="")
st.title(" Text-to-SQL Assistant")
st.write("Ask questions about the employee database in plain English!")

# 3. Database Initialization
# Define the path to the database in the data/ folder
DB_PATH = os.path.join(parent_dir, "data", "employee.db")

# If the database doesn't exist, build it using our utils file
if not os.path.exists(DB_PATH):
    setup_database(DB_PATH)

# 4. Check for API Key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key or api_key == "your_openai_api_key_here":
    st.warning("Please add your OpenAI API key to the .env file in the root directory to continue.")
    st.stop()

# 5. Set up LangChain Engine (Cached so it doesn't reload on every button click)
@st.cache_resource
def get_db_chain():
    # Connect to the SQLite database
    db = SQLDatabase.from_uri(f"sqlite:///{DB_PATH}")
    
    # Initialize the LLM (temperature=0 ensures factual, non-creative answers)
    llm = OpenAI(temperature=0, openai_api_key=api_key)
    
    # Create the text-to-SQL chain
    # verbose=True will print the generated SQL query to your terminal for debugging
    db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True, use_query_checker=True)
    return db_chain

try:
    db_chain = get_db_chain()
except Exception as e:
    st.error(f"Error connecting to database or LLM: {e}")
    st.stop()

# 6. User Interface
user_question = st.text_input("Enter your question:", placeholder="e.g., Who earns the most in Engineering?")

if st.button("Generate Answer"):
    if user_question:
        with st.spinner("Translating to SQL and querying database..."):
            try:
                # Run the chain
                response = db_chain.run(user_question)
                st.success("Query Successful!")
                st.subheader("Answer:")
                st.write(response)
            except Exception as e:
                st.error(f"An error occurred. The model might have generated invalid SQL. Details: {e}")
    else:
        st.warning("Please enter a question first.")