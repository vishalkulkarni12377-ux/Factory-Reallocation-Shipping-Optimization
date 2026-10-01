import pandas as pd

# =========================================
# DATE ANALYSIS
# =========================================

file_path = "data/Nassau Candy Distributor.csv"

df = pd.read_csv(file_path)

# Convert dates
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

# Calculate Lead Time
df["Lead Time"] = (
    df["Ship Date"] - df["Order Date"]
).dt.days


# =========================================
# 1. LEAD TIME BY SHIP MODE
# =========================================

print("\nLead Time by Ship Mode:")
print(
    df.groupby("Ship Mode")["Lead Time"]
    .agg(["count", "min", "mean", "max"])
)


# =========================================
# 2. LEAD TIME BY REGION
# =========================================

print("\nLead Time by Region:")
print(
    df.groupby("Region")["Lead Time"]
    .agg(["count", "min", "mean", "max"])
)


# =========================================
# 3. ORDER YEAR AND SHIP YEAR
# =========================================

df["Order Year"] = df["Order Date"].dt.year
df["Ship Year"] = df["Ship Date"].dt.year

print("\nOrder Year Distribution:")
print(df["Order Year"].value_counts().sort_index())

print("\nShip Year Distribution:")
print(df["Ship Year"].value_counts().sort_index())


# =========================================
# 4. YEAR DIFFERENCE
# =========================================

df["Year Difference"] = (
    df["Ship Year"] - df["Order Year"]
)

print("\nYear Difference:")
print(df["Year Difference"].value_counts().sort_index())


# =========================================
# 5. SAMPLE RECORDS
# =========================================

print("\nSample Records:")
print(
    df[
        [
            "Order Date",
            "Ship Date",
            "Ship Mode",
            "Region",
            "Lead Time"
        ]
    ].head(10)
)


print("\nDate analysis completed successfully!")