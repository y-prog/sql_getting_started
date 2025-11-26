import pandas as pd
import sqlite3
# Load the dataset
file_path = '/kaggle/input/real-estate-dataset/data.csv'
df = pd.read_csv(file_path)
# Connect to a SQLite database (or create one in memory)
conn = sqlite3.connect(':memory:')
# Save the DataFrame to a SQL table
df.to_sql('real_estate', conn, index=False, if_exists='replace')