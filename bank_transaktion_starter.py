import pandas as pd
import sqlite3

# Load the original dataset
df = pd.read_csv('/kaggle/input/bank-transaction-dataset-for-fraud-detection/bank_transactions_data_2.csv')

# 1. Accounts Table
accounts = df[['AccountID', 'CustomerAge', 'CustomerOccupation']].drop_duplicates()

# 2. Merchants Table
merchants = df[['MerchantID', 'Location']].drop_duplicates()

# 3. Transactions Table
transactions = df[['TransactionID', 'AccountID', 'TransactionAmount', 'TransactionDate',
                   'TransactionType', 'Location', 'DeviceID', 'IP Address', 'MerchantID',
                   'AccountBalance', 'PreviousTransactionDate', 'Channel',
                   'TransactionDuration', 'LoginAttempts']]

# Ensure uniqueness
accounts = accounts.drop_duplicates(subset='AccountID')
merchants = merchants.drop_duplicates(subset='MerchantID')

# Connect to SQLite
conn = sqlite3.connect(':memory:')

# Load tables
merchants.to_sql('merchants', conn, index=False, if_exists='replace')
transactions.to_sql('transactions', conn, index=False, if_exists='replace')
accounts.to_sql('accounts', conn, index=False, if_exists='replace')
