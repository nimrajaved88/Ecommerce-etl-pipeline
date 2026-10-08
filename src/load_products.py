import os
import pandas as pd
import mysql.connector

# Read cleaned CSV
file_path = r"C:\Users\NJ\PycharmProjects\Subscription_Box_ETL\data\staging\cleaned_data.csv"

print("Reading CSV...")
df = pd.read_csv(file_path, low_memory=False)

# Select product information
products = df[["sku", "category_name_1"]].drop_duplicates()

print("Products found:", len(products))

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

for _, row in products.iterrows():
    data.append((
        row["sku"],
        row["category_name_1"]
    ))

print("Data prepared. Loading into MySQL...")

# Insert products
sql = """
INSERT INTO products (sku, category)
VALUES (%s, %s)
"""

cursor.executemany(sql, data)

connection.commit()

print("Products loaded successfully!")

cursor.close()
connection.close()