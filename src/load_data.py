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
for _, row in df.iterrows():
    cur.execute(
        "INSERT INTO data (month, invoices, amount) VALUES (%s, %s, %s)",
        (row['Month'], row['Invoices'], row['Amount'])
    )

conn.commit()
cur.close()
conn.close()

print("Data loaded successfully")