import pandas as pd

# =========================================
# PRODUCT CHECK
# =========================================

file_path = "data/Nassau Candy Distributor.csv"

df = pd.read_csv(file_path)

# =========================================
# UNIQUE PRODUCTS
# =========================================

products = df["Product Name"].value_counts()

print("\nTotal Unique Products:")
print(len(products))

print("\nProduct List:")
print(products)


# =========================================
# PRODUCT IDs
# =========================================

print("\nUnique Product IDs:")
print(df["Product ID"].nunique())


# =========================================
# PRODUCT AND PRODUCT ID
# =========================================

print("\nProduct Name and Product ID:")

product_info = (
    df[["Product ID", "Product Name"]]
    .drop_duplicates()
    .sort_values("Product Name")
)

print(product_info.to_string(index=False))


print("\nProduct check completed successfully!")