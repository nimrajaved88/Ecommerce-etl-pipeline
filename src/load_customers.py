import os
import pandas as pd
import mysql.connector

# 1. Read cleaned CSV
file_path = r"C:\Users\NJ\PycharmProjects\Subscription_Box_ETL\data\staging\cleaned_data.csv"

print("Reading CSV...")
df = pd.read_csv(file_path, low_memory=False)

# 2. Get customer data
customers = df[["Customer ID", "Customer Since"]].drop_duplicates()

print("Customers found:", len(customers))

# 3. Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD"),
    database="subscription_box"
)

cursor = connection.cursor()

# 4. Prepare data
data = []

for _, row in customers.iterrows():
    data.append((
        int(row["Customer ID"]),
        row["Customer Since"]
    ))

print("Data prepared. Loading into MySQL...")

# 5. Insert data
sql = """
INSERT IGNORE INTO customers (customer_id, customer_since)
VALUES (%s, %s)
"""

cursor.executemany(sql, data)

# 6. Save changes
connection.commit()

print("Customers loaded successfully!")

# 7. Close connection
cursor.close()
connection.close()