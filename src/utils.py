import sqlite3
import os

def setup_database(db_path="../data/employee.db"):
    """Creates a sample SQLite database for the project."""
    
    # Ensure the data directory exists
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Employees (
        ID INTEGER PRIMARY KEY,
        Name TEXT,
        Department TEXT,
        Salary INTEGER,
        Hire_Date TEXT
    )
    ''')

    # Clear existing data to prevent duplicates if run multiple times
    cursor.execute("DELETE FROM Employees")

    # Insert sample data
    sample_data = [
        (1, 'Alice Smith', 'Engineering', 120000, '2021-01-15'),
        (2, 'Bob Johnson', 'Sales', 85000, '2022-03-10'),
        (3, 'Charlie Brown', 'Engineering', 95000, '2023-06-01'),
        (4, 'Diana Prince', 'HR', 75000, '2020-11-20'),
        (5, 'Evan Wright', 'Sales', 90000, '2021-08-05')
    ]
    
    cursor.executemany("INSERT INTO Employees VALUES (?, ?, ?, ?, ?)", sample_data)
    conn.commit()
    conn.close()
    print(f"Database successfully created at {db_path}")

if __name__ == "__main__":
    # You can run this file directly to test the database creation
    setup_database()