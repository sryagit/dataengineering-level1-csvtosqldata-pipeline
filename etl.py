import pandas as pd
import sqlite3
import os

# Load CSV
csv_file = os.path.join('..', 'data', 'sales_data.csv')
df = pd.read_csv(csv_file)

# Clean data (basic)
df.dropna(inplace=True)

# Connect to SQLite (creates DB if not exists)
conn = sqlite3.connect('sales.db')
cursor = conn.cursor()

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        OrderID INTEGER,
        Date TEXT,
        Customer TEXT,
        Amount REAL
    )
""")

# Insert data
df.to_sql('sales', conn, if_exists='replace', index=False)

# Verify
print(pd.read_sql("SELECT * FROM sales", conn))

conn.close()
