import pandas as pd
import psycopg2

# Load CSV
df = pd.read_csv('data/data.csv')  # change to your actual file name

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="data_db",
    user="postgres",
    password="Suhaas@2278"
)

cur = conn.cursor()

# Insert data
from psycopg2.extras import execute_values

# Convert dataframe to list of tuples
data_tuples = list(df.itertuples(index=False, name=None))

# Bulk insert
execute_values(
    cur,
    "INSERT INTO data (month, invoices, amount) VALUES %s",
    data_tuples
)

conn.commit()
cur.close()
conn.close()

print("Data loaded successfully")