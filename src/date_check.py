import pandas as pd

# =========================================
# DATE CHECK
# =========================================

# Load original dataset
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
# DATE RANGE
# =========================================

print("\nOrder Date Range:")
print(df["Order Date"].min())
print(df["Order Date"].max())

print("\nShip Date Range:")
print(df["Ship Date"].min())
print(df["Ship Date"].max())


# =========================================
# LEAD TIME SUMMARY
# =========================================

print("\nLead Time Summary:")
print(df["Lead Time"].describe())


# =========================================
# CHECK LARGE LEAD TIMES
# =========================================

print("\nLarge Lead Time Check:")

for days in [30, 60, 90, 180, 365]:

    count = (df["Lead Time"] > days).sum()
    percentage = (count / len(df)) * 100

    print(
        f"Lead Time > {days} days: "
        f"{count} records ({percentage:.2f}%)"
    )


# =========================================
# CHECK INVALID DATES
# =========================================

print("\nInvalid Date Check:")

invalid_order = df["Order Date"].isna().sum()
invalid_ship = df["Ship Date"].isna().sum()

print("Invalid Order Dates:", invalid_order)
print("Invalid Ship Dates:", invalid_ship)


# =========================================
# SAMPLE RECORDS
# =========================================

print("\nSample Date Records:")

print(
    df[
        ["Order Date", "Ship Date", "Lead Time"]
    ].head(10)
)


print("\nDate check completed successfully!")