import os
import pandas as pd
import mysql.connector

# Read cleaned CSV
file_path = r"C:\Users\NJ\PycharmProjects\Subscription_Box_ETL\data\staging\cleaned_data.csv"

print("Reading CSV...")
df = pd.read_csv(file_path, low_memory=False)

# Get unique payment methods
payments = df[["payment_method"]].drop_duplicates()

print("Payment methods found:", len(payments))

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD"),
    database="subscription_box"
)

cursor = connection.cursor()

# Prepare data
data = []

for _, row in payments.iterrows():
    data.append((row["payment_method"],))

print("Data prepared. Loading into MySQL...")

# Insert payment methods
sql = """
INSERT INTO payments (payment_method)
VALUES (%s)
"""

cursor.executemany(sql, data)

connection.commit()

print("Payments loaded successfully!")

cursor.close()
connection.close()