# Step 1: Import libraries
import pandas as pd
import sqlite3
import random

# Step 2: Load the dataset
file_path = '/kaggle/input/student-alcohol-consumption/student-mat.csv'
math_data = pd.read_csv(file_path)

# Step 3: Generate reproducible random names
# Seed for reproducibility
random.seed(42)

# Example first and last names
first_names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ian', 'Julia']
last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Miller', 'Davis', 'Garcia', 'Martinez', 'Wilson']

# Generate names for all students
n = len(math_data)
names = [f"{random.choice(first_names)} {random.choice(last_names)}" for _ in range(n)]

# Step 4: Add names to the DataFrame
math_data['names'] = names

# Step 5: Add a unique student_id column
math_data.insert(0, 'student_id', range(1, n + 1))

# Step 6: Create SQLite in-memory database
conn = sqlite3.connect(':memory:')

# Step 7: Save the DataFrame to SQL table
math_data.to_sql('math_students', conn, index=False, if_exists='replace')


