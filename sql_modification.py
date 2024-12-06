import pandas as pd
import sqlite3

# Step 1: Load the CSV into a pandas DataFrame
csv_file = "/kaggle/input/students/students_dataset.csv"  # Replace with your CSV file path
students_df = pd.read_csv(csv_file)

# Step 2: Create an SQLite database and connect to it
conn = sqlite3.connect("students.db")  # Creates a local SQLite database
cursor = conn.cursor()

# Step 3: Convert the pandas DataFrame into an SQLite table
students_df.to_sql("students", conn, if_exists="replace", index=False)

'''go to cell below'''

cursor.execute('''query you want to run''')
cursor.execute('''query you want to run''')
conn.commit()

'''go to cell below'''

query = pd.read_sql("SELECT * FROM students", conn)

query # display result of updated query