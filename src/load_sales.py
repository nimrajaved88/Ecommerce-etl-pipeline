import os
import pandas as pd
import mysql.connector

# Read cleaned CSV
file_path = r"C:\Users\NJ\PycharmProjects\Subscription_Box_ETL\data\staging\cleaned_data.csv"

print("Reading CSV...")

df = pd.read_csv(file_path, low_memory=False)

# Select required columns
sales = df[
    [
        "item_id",
        "increment_id",
        "Customer ID",
        "sku",
        "created_at",
        "payment_method",
        "price",
        "qty_ordered",
        "discount_amount",
        "grand_total",
        "status"
    ]
].copy()

# Convert date
sales["created_at"] = pd.to_datetime(sales["created_at"])
print("Sales records found:", len(sales))

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD"),
    database="subscription_box"
)

cursor = connection.cursor()

print("Connected to MySQL.")

# Product lookup
cursor.execute("SELECT product_id, sku FROM products")

product_lookup = {}

for product_id, sku in cursor.fetchall():
    product_lookup[sku] = product_id

# Payment lookup
cursor.execute("SELECT payment_id, payment_method FROM payments")

payment_lookup = {}

for payment_id, payment_method in cursor.fetchall():
    payment_lookup[payment_method] = payment_id

# Date lookup
cursor.execute("SELECT date_id, sale_date FROM dates")

date_lookup = {}

for date_id, sale_date in cursor.fetchall():
    date_lookup[str(sale_date)] = date_id

print("Lookup tables prepared.")

# Prepare sales data
data = []

for _, row in sales.iterrows():

    product_id = product_lookup.get(row["sku"])
    payment_id = payment_lookup.get(row["payment_method"])
    sale_date = str(row["created_at"].date())
    date_id = date_lookup.get(sale_date)

    data.append(
        (
            int(row["item_id"]),
            str(row["increment_id"]),
            int(row["Customer ID"]),
            product_id,
            date_id,
            payment_id,
            float(row["price"]),
            int(row["qty_ordered"]),
            float(row["discount_amount"]),
            float(row["grand_total"]),
            row["status"]
        )
    )

print("Sales data prepared:", len(data))

# SQL statement
sql = """
INSERT INTO sales
(
    item_id,
    order_id,
    customer_id,
    product_id,
    date_id,
    payment_id,
    price,
    quantity,
    discount,
    grand_total,
    status
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# Load data in batches
batch_size = 5000

for i in range(0, len(data), batch_size):

    batch = data[i:i + batch_size]

    cursor.executemany(sql, batch)

    connection.commit()

    loaded = min(i + batch_size, len(data))

    print(f"Loaded {loaded} / {len(data)}")

print("Sales loaded successfully!")

cursor.close()
connection.close()