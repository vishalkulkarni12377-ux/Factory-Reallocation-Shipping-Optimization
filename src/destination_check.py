import pandas as pd

# =========================================
# DESTINATION DATA CHECK
# =========================================

file_path = "data/Nassau Candy Distributor.csv"

df = pd.read_csv(file_path)

print("Dataset Shape:")
print(df.shape)


# =========================================
# 1. CHECK DESTINATION COLUMNS
# =========================================

print("\nDestination Columns:")

destination_columns = [
    "Country/Region",
    "City",
    "State/Province",
    "Postal Code",
    "Region"
]

for column in destination_columns:
    print(
        f"{column}: "
        f"{df[column].nunique()} unique values"
    )


# =========================================
# 2. SHOW STATES
# =========================================

print("\nStates / Provinces:")

print(
    df["State/Province"]
    .value_counts()
    .head(30)
)


# =========================================
# 3. SHOW REGIONS
# =========================================

print("\nRegions:")

print(
    df["Region"]
    .value_counts()
)


# =========================================
# 4. CHECK POSTAL CODES
# =========================================

print("\nPostal Code Examples:")

print(
    df["Postal Code"]
    .head(20)
)


# =========================================
# 5. SHOW CITY EXAMPLES
# =========================================

print("\nCity Examples:")

print(
    df["City"]
    .drop_duplicates()
    .head(30)
)


# =========================================
# 6. SHOW COMPLETE DESTINATION SAMPLE
# =========================================

print("\nDestination Sample:")

print(
    df[
        [
            "Country/Region",
            "City",
            "State/Province",
            "Postal Code",
            "Region"
        ]
    ].head(10)
)


print("\nDestination check completed successfully!")