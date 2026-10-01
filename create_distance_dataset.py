import pandas as pd

# =========================================
# FILE PATHS
# =========================================

orders_file = "data/final_dataset.csv"
distance_file = "data/destination_factory_distances.csv"
output_file = "data/order_distance_dataset.csv"


# =========================================
# LOAD DATA
# =========================================

orders = pd.read_csv(orders_file)
distances = pd.read_csv(distance_file)

print("Orders Dataset Shape:", orders.shape)
print("Distance Dataset Shape:", distances.shape)


# =========================================
# COLUMNS USED FOR MERGING
# =========================================

merge_columns = [
    "Country/Region",
    "City",
    "State/Province",
    "Postal Code"
]


# =========================================
# SELECT DISTANCE COLUMNS
# =========================================

distance_columns = merge_columns + [
    "Lot's O' Nuts Distance (km)",
    "Wicked Choccy's Distance (km)",
    "Sugar Shack Distance (km)",
    "Secret Factory Distance (km)",
    "The Other Factory Distance (km)"
]

distances = distances[distance_columns]


# =========================================
# MERGE
# =========================================

df = orders.merge(
    distances,
    on=merge_columns,
    how="left"
)


# =========================================
# CHECK MISSING DISTANCES
# =========================================

factory_distance_columns = [
    "Lot's O' Nuts Distance (km)",
    "Wicked Choccy's Distance (km)",
    "Sugar Shack Distance (km)",
    "Secret Factory Distance (km)",
    "The Other Factory Distance (km)"
]

print("\nMissing Distance Values:")

print(
    df[factory_distance_columns]
    .isna()
    .sum()
)


# =========================================
# SAVE DATASET
# =========================================

df.to_csv(output_file, index=False)


# =========================================
# RESULTS
# =========================================

print("\nOrder-level distance dataset created successfully!")

print("Output File:", output_file)

print("\nFinal Shape:", df.shape)

print("\nFirst 5 Records:")

print(
    df.head().to_string(index=False)
)