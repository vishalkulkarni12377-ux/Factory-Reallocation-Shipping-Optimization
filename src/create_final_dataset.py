import pandas as pd

# =========================================
# CREATE FINAL DATASET
# =========================================

# File paths
input_file = "data/Nassau Candy Distributor.csv"
output_file = "data/final_dataset.csv"

# =========================================
# 1. LOAD ORIGINAL DATASET
# =========================================

df = pd.read_csv(input_file)

print("Original Dataset Shape:", df.shape)


# =========================================
# 2. CONVERT DATE COLUMNS
# =========================================

df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    dayfirst=True,
    errors="coerce"
)

df["Ship Date"] = pd.to_datetime(
    df["Ship Date"],
    dayfirst=True,
    errors="coerce"
)


# =========================================
# 3. CALCULATE LEAD TIME
# =========================================

df["Lead Time"] = (
    df["Ship Date"] - df["Order Date"]
).dt.days


# =========================================
# 4. ADD LEAD TIME STATUS
# =========================================

df["Lead Time Status"] = df["Lead Time"].apply(
    lambda x: "Needs Validation" if x > 365 else "Normal"
)


# =========================================
# 5. PRODUCT - FACTORY MAPPING
# =========================================

factory_mapping = {

    # Chocolate
    "Wonka Bar - Nutty Crunch Surprise": "Lot's O' Nuts",
    "Wonka Bar - Fudge Mallows": "Lot's O' Nuts",
    "Wonka Bar -Scrumdiddlyumptious": "Lot's O' Nuts",

    "Wonka Bar - Milk Chocolate": "Wicked Choccy's",
    "Wonka Bar - Triple Dazzle Caramel": "Wicked Choccy's",

    # Sugar
    "Laffy Taffy": "Sugar Shack",
    "SweeTARTS": "Sugar Shack",
    "Nerds": "Sugar Shack",
    "Fun Dip": "Sugar Shack",

    "Everlasting Gobstopper": "Secret Factory",
    "Hair Toffee": "The Other Factory",

    # Other
    "Fizzy Lifting Drinks": "Sugar Shack",
    "Lickable Wallpaper": "Secret Factory",
    "Wonka Gum": "Secret Factory",
    "Kazookles": "The Other Factory"
}


# =========================================
# 6. ADD CURRENT FACTORY
# =========================================

df["Current Factory"] = df["Product Name"].map(
    factory_mapping
)


# =========================================
# 7. CHECK FACTORY MAPPING
# =========================================

missing_factory = df["Current Factory"].isna().sum()

print("\nMissing Factory Mapping:", missing_factory)


# =========================================
# 8. DISPLAY FINAL COLUMNS
# =========================================

print("\nFinal Dataset Columns:")

print(df.columns.tolist())


# =========================================
# 9. DISPLAY SAMPLE
# =========================================

print("\nFinal Dataset Sample:")

print(
    df[
        [
            "Product ID",
            "Product Name",
            "Order Date",
            "Ship Date",
            "Lead Time",
            "Lead Time Status",
            "Current Factory"
        ]
    ].head(10)
)


# =========================================
# 10. SAVE FINAL DATASET
# =========================================

df.to_csv(
    output_file,
    index=False
)

print("\nFinal dataset saved successfully!")
print("File:", output_file)
print("Final Dataset Shape:", df.shape)


# =========================================
# 11. FACTORY SUMMARY
# =========================================

print("\nRecords by Current Factory:")

print(
    df["Current Factory"]
    .value_counts()
)


print("\nFinal dataset creation completed successfully!")