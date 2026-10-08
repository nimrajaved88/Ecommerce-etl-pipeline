import pandas as pd

# -----------------------------------------
# 1. EXTRACT
# -----------------------------------------

input_file = r"C:\Users\NJ\PycharmProjects\Subscription_Box_ETL\data\raw\data project.csv"

df = pd.read_csv(input_file, low_memory=False)

print("Raw data loaded.")
print("Rows:", len(df))


# -----------------------------------------
# 2. CLEAN COLUMN NAMES
# -----------------------------------------

df.columns = df.columns.str.strip()

print("\nColumn names cleaned.")


# -----------------------------------------
# 3. CLEAN MISSING/INVALID TEXT VALUES
# -----------------------------------------

# Convert "\N" into missing values
df = df.replace(r"\N", pd.NA)


# -----------------------------------------
# 4. CONVERT DATA TYPES
# -----------------------------------------

df["created_at"] = pd.to_datetime(
    df["created_at"],
    errors="coerce"
)

df["Working Date"] = pd.to_datetime(
    df["Working Date"],
    errors="coerce"
)

df["Customer Since"] = pd.to_datetime(
    df["Customer Since"],
    format="%Y-%m",
    errors="coerce"
)

df["Customer ID"] = pd.to_numeric(
    df["Customer ID"],
    errors="coerce"
)

df["price"] = pd.to_numeric(
    df["price"],
    errors="coerce"
)

df["qty_ordered"] = pd.to_numeric(
    df["qty_ordered"],
    errors="coerce"
)

df["grand_total"] = pd.to_numeric(
    df["grand_total"],
    errors="coerce"
)

df["discount_amount"] = pd.to_numeric(
    df["discount_amount"],
    errors="coerce"
)


# -----------------------------------------
# 5. STANDARDIZE TEXT
# -----------------------------------------

text_columns = [
    "status",
    "sku",
    "category_name_1",
    "sales_commission_code",
    "payment_method",
    "BI Status"
]

for column in text_columns:
    df[column] = df[column].astype("string").str.strip()


# -----------------------------------------
# 6. HANDLE MISSING VALUES
# -----------------------------------------

df["status"] = df["status"].fillna("Unknown")

df["category_name_1"] = df["category_name_1"].fillna("Unknown")

df["sku"] = df["sku"].fillna("Unknown")

df["sales_commission_code"] = (
    df["sales_commission_code"].fillna("No Commission Code")
)

df["Customer ID"] = df["Customer ID"].fillna(-1)


# -----------------------------------------
# 7. VALIDATE DATA
# -----------------------------------------

print("\nAfter cleaning:")

print("Rows:", len(df))

print("Missing status:", df["status"].isna().sum())

print("Missing category:", df["category_name_1"].isna().sum())

print("Missing SKU:", df["sku"].isna().sum())

print("Missing Customer ID:", df["Customer ID"].isna().sum())

print("Invalid dates:", df["created_at"].isna().sum())

print("Negative prices:", (df["price"] < 0).sum())

print("Negative quantities:", (df["qty_ordered"] < 0).sum())


# -----------------------------------------
# 8. SAVE STAGING DATA
# -----------------------------------------

output_file = r"C:\Users\NJ\PycharmProjects\Subscription_Box_ETL\data\staging\cleaned_data.csv"

df.to_csv(output_file, index=False)

print("\nCleaned data saved successfully!")

print(output_file)