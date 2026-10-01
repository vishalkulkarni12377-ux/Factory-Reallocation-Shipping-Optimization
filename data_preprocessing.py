import pandas as pd

# =========================================
# DATA PREPROCESSING
# =========================================

# File paths
input_file = "data/Nassau Candy Distributor.csv"
output_file = "data/cleaned_nassau_candy.csv"

# =========================================
# 1. LOAD DATASET
# =========================================

df = pd.read_csv(input_file)

print("Original Dataset Shape:", df.shape)

# =========================================
# 2. CHECK MISSING VALUES
# =========================================

print("\nMissing Values:")
print(df.isnull().sum())

# =========================================
# 3. CONVERT DATE COLUMNS
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
# 4. CHECK INVALID DATES
# =========================================

invalid_order_dates = df["Order Date"].isna().sum()
invalid_ship_dates = df["Ship Date"].isna().sum()

print("\nInvalid Order Dates:", invalid_order_dates)
print("Invalid Ship Dates:", invalid_ship_dates)

# =========================================
# 5. CALCULATE LEAD TIME
# =========================================

df["Lead Time"] = (
    df["Ship Date"] - df["Order Date"]
).dt.days

print("\nLead Time Statistics:")
print(df["Lead Time"].describe())

# =========================================
# 6. FLAG UNUSUALLY LARGE LEAD TIMES
# =========================================

df["Lead Time Status"] = df["Lead Time"].apply(
    lambda x: "Needs Validation" if x > 365 else "Normal"
)

print("\nLead Time Status:")
print(df["Lead Time Status"].value_counts())

# =========================================
# 7. DISPLAY SAMPLE DATA
# =========================================

print("\nSample Processed Data:")
print(
    df[
        [
            "Order Date",
            "Ship Date",
            "Lead Time",
            "Lead Time Status"
        ]
    ].head(10)
)

# =========================================
# 8. SAVE CLEANED DATASET
# =========================================

df.to_csv(output_file, index=False)

print("\nCleaned dataset saved successfully!")
print("File:", output_file)
print("Final Dataset Shape:", df.shape)