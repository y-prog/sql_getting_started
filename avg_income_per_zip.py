import numpy as np
import pandas as pd
import sqlite3

df_employees = pd.read_csv('/kaggle/input/employees/employees_dataset.csv')
df_contractors = pd.read_csv('/kaggle/input/contractor-1/contractor.csv')

# Connect to an in-memory SQLite database
conn = sqlite3.connect(":memory:")

# Convert the DataFrame to SQL tables
df_employees.to_sql("employees", conn, index=False, if_exists="replace")
df_contractors.to_sql("contractors", conn, index=False, if_exists="replace")

# Define a helper function to execute SQL and display results
def execute_sql(query):
    return pd.read_sql(query, conn)


