import pandas as pd

# -----------------------------------------
# 1. LOAD CLEANED DATA
# -----------------------------------------

input_file = r"C:\Users\NJ\PycharmProjects\Subscription_Box_ETL\data\staging\cleaned_data.csv"

df = pd.read_csv(input_file, low_memory=False)

print("CLEANED DATA VALIDATION")
print("=" * 50)

# -----------------------------------------
# 2. BASIC CHECKS
# -----------------------------------------

print("\n1. BASIC INFORMATION")
print("Rows:", len(df))
print("Columns:", len(df.columns))

# -----------------------------------------
# 3. PRIMARY KEY CHECK
# -----------------------------------------

print("\n2. ITEM ID CHECK")

duplicate_item_ids = df["item_id"].duplicated().sum()

print("Duplicate item IDs:", duplicate_item_ids)

# -----------------------------------------
# 4. REQUIRED FIELD CHECK
# -----------------------------------------

print("\n3. REQUIRED FIELD CHECK")

required_columns = [
    "item_id",
    "increment_id",
    "created_at",
    "sku",
    "price",
    "qty_ordered"
]

for column in required_columns:
    missing = df[column].isna().sum()
    print(f"{column}: {missing} missing values")

# -----------------------------------------
# 5. NUMERIC VALIDATION
# -----------------------------------------

print("\n4. NUMERIC VALIDATION")

print("Negative prices:", (df["price"] < 0).sum())
print("Zero quantities:", (df["qty_ordered"] == 0).sum())
print("Negative quantities:", (df["qty_ordered"] < 0).sum())

# -----------------------------------------
# 6. DATE VALIDATION
# -----------------------------------------

print("\n5. DATE VALIDATION")

df["created_at"] = pd.to_datetime(
    df["created_at"],
    errors="coerce"
)

print("Invalid dates:", df["created_at"].isna().sum())

print("Minimum date:", df["created_at"].min())
print("Maximum date:", df["created_at"].max())

# -----------------------------------------
# 7. CATEGORY CHECK
# -----------------------------------------

print("\n6. CATEGORY CHECK")

print("Number of categories:", df["category_name_1"].nunique())

# -----------------------------------------
# 8. PAYMENT CHECK
# -----------------------------------------

print("\n7. PAYMENT METHOD CHECK")

print("Number of payment methods:", df["payment_method"].nunique())

# -----------------------------------------
# 9. FINAL RESULT
# -----------------------------------------

print("\n" + "=" * 50)
print("VALIDATION COMPLETED")
print("=" * 50)