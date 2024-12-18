import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate a sample dataset
np.random.seed(42)

# Creating sample data
n_rows = 1000
data = {
    'price': np.append(np.random.randint(500, 100000, n_rows - 3), [1000000, 1200000, 1500000]),  # Adding outliers
    'mileage': np.random.randint(1000, 200000, n_rows),
    'engineSize': np.random.choice([1.0, 1.6, 2.0, 3.0, 4.0, 5.0], n_rows),
    'car_id': np.random.choice(np.arange(1, 1200, dtype=float), n_rows),
    'year': np.random.randint(1990, 2024, n_rows),
    'brand': np.random.choice(['Toyota', 'Ford', 'BMW', 'Honda', 'Mercedes'], n_rows),
    'condition': np.random.choice(['new', 'used', 'salvage'], n_rows),
    'location': np.random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami'], n_rows),
    'seller_contact': np.random.choice([None, 'available'], n_rows, p=[0.3, 0.7])
}

df = pd.DataFrame(data)
'-----------------------------------------------------------------------------------------------------'

import numpy as np
import pandas as pd

# Number of rows for the second table
n_rows = 300

# Generating data for the second table
data_attributes = {
    'car_id': np.random.choice(np.arange(1, 1200, dtype=int), n_rows, replace=False),  # Unique car IDs
    'is_new': np.random.choice([True, False], n_rows, p=[0.2, 0.8]),  # 20% chance the car is new
    'is_for_auction': np.random.choice([True, False], n_rows, p=[0.1, 0.9]),  # 10% chance listed for auction
    'condition': np.random.choice(['new', 'used', 'salvage'], n_rows, p=[0.2, 0.7, 0.1]),  # Condition probabilities
    'price_per_mile': np.round(np.random.uniform(0.05, 2.5, n_rows), 2)  # Price per mile between 0.05 and 2.5
}

# Creating a DataFrame
df_attributes = pd.DataFrame(data_attributes)

# Display the first few rows
(df_attributes.head())
df_attributes.to_csv('attributes.csv' ,index = False)