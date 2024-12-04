import pandas as pd
import sqlite3

conn = sqlite3.connect(":memory:")
# Step 1: Read the CSV file into a Pandas DataFrame
df = pd.read_csv(r'/kaggle/input/position-salary-dataset/position_salary.csv', encoding='ISO-8859-1')  # Replace with your CSV file path

df = df.rename(columns={
    'Experience (Years)': 'Experience'})

# Drop rows with NaN values
df = df.dropna()

# Split the DataFrame by Gender
male_df = df[df['Gender'] == 'Male']
female_df = df[df['Gender'] == 'Female']

# Convert the DataFrame to SQL tables
male_df.to_sql("male", conn, index=False, if_exists="replace")
female_df.to_sql("female", conn, index=False, if_exists="replace")

# Define a helper function to execute SQL and display results
def execute_sql(query):
    return pd.read_sql(query, conn)