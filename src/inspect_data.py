import pandas as pd

file_path = r"C:\Users\NJ\PycharmProjects\Subscription_Box_ETL\data\raw\data project.csv"

df = pd.read_csv(file_path, low_memory=False)

print("DATASET PROFILE")
print("=" * 50)

print("\n1. BASIC INFORMATION")
print("Total rows:", len(df))
print("Total columns:", len(df.columns))

print("\n2. UNIQUE VALUES")
print("Unique item IDs:", df["item_id"].nunique())
print("Unique orders:", df["increment_id"].nunique())
print("Unique customers:", df["Customer ID"].nunique())
print("Unique SKUs:", df["sku"].nunique())
print("Unique categories:", df["category_name_1"].nunique())

print("\n3. ORDER STATUS")
print(df["status"].value_counts(dropna=False))

print("\n4. PAYMENT METHODS")
print(df["payment_method"].value_counts(dropna=False))

print("\n5. TOP CATEGORIES")
print(df["category_name_1"].value_counts(dropna=False).head(20))

print("\n6. MISSING VALUES")
missing = df.isnull().sum()
print(missing[missing > 0].sort_values(ascending=False))

print("\n7. DUPLICATE ROWS")
print("Duplicate rows:", df.duplicated().sum())

print("\n8. INVALID VALUES")
print("Negative prices:", (df["price"] < 0).sum())
print("Zero quantities:", (df["qty_ordered"] == 0).sum())
print("Negative quantities:", (df["qty_ordered"] < 0).sum())

print("\n9. ORDERS WITH MULTIPLE ITEMS")
items_per_order = df.groupby("increment_id")["item_id"].count()

print("Orders with 1 item:", (items_per_order == 1).sum())
print("Orders with more than 1 item:", (items_per_order > 1).sum())

print("\n10. ORDERS PER CUSTOMER")
orders_per_customer = df.groupby("Customer ID")["increment_id"].nunique()
print(orders_per_customer.describe())
print("\n11. DATE INFORMATION")
print("=" * 50)

print("\nCreated At:")
print(df["created_at"].head(10))

print("\nWorking Date:")
print(df["Working Date"].head(10))

print("\nCustomer Since:")
print(df["Customer Since"].head(10))

print("\nYear:")
print(df["Year"].value_counts().sort_index())

print("\nMonth:")
print(df["Month"].value_counts().sort_index())

print("\nFinancial Year:")
print(df["FY"].value_counts())

print("\nDate range:")

created_dates = pd.to_datetime(
    df["created_at"],
    errors="coerce"
)

print("Minimum date:", created_dates.min())
print("Maximum date:", created_dates.max())
print("Invalid dates:", created_dates.isna().sum())