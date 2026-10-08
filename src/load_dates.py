import os
import pandas as pd
import mysql.connector

# Read cleaned CSV
file_path = r"C:\Users\NJ\PycharmProjects\Subscription_Box_ETL\data\staging\cleaned_data.csv"

print("Reading CSV...")
df = pd.read_csv(file_path, low_memory=False)

# Get unique dates
df["created_at"] = pd.to_datetime(df["created_at"])

dates = df[["created_at", "FY"]].drop_duplicates()

# Create date information
dates["sale_date"] = dates["created_at"].dt.date
dates["day"] = dates["created_at"].dt.day
dates["month"] = dates["created_at"].dt.month
dates["year"] = dates["created_at"].dt.year
dates["quarter"] = dates["created_at"].dt.quarter
dates["financial_year"] = dates["FY"]

# Keep required columns
dates = dates[
    ["sale_date", "day", "month", "year", "quarter", "financial_year"]
].drop_duplicates()

print("Dates found:", len(dates))

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

for _, row in dates.iterrows():
    data.append((
        row["sale_date"],
        int(row["day"]),
        int(row["month"]),
        int(row["year"]),
        int(row["quarter"]),
        row["financial_year"]
    ))

print("Data prepared. Loading into MySQL...")

# Insert dates
sql = """
INSERT INTO dates
(sale_date, day, month, year, quarter, financial_year)
VALUES (%s, %s, %s, %s, %s, %s)
"""

cursor.executemany(sql, data)

connection.commit()

print("Dates loaded successfully!")

cursor.close()
connection.close()