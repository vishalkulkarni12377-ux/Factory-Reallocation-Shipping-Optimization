import pandas as pd

# =========================================
# FILE PATHS
# =========================================

input_file = "data/order_distance_dataset.csv"
output_file = "data/factory_alternative_analysis.csv"


# =========================================
# LOAD DATA
# =========================================

df = pd.read_csv(input_file)

print("Input Dataset Shape:", df.shape)


# =========================================
# FACTORY DISTANCE COLUMNS
# =========================================

factory_distances = {
    "Lot's O' Nuts": "Lot's O' Nuts Distance (km)",
    "Wicked Choccy's": "Wicked Choccy's Distance (km)",
    "Sugar Shack": "Sugar Shack Distance (km)",
    "Secret Factory": "Secret Factory Distance (km)",
    "The Other Factory": "The Other Factory Distance (km)"
}


# =========================================
# CURRENT FACTORY DISTANCE
# =========================================

def get_current_distance(row):
    current_factory = row["Current Factory"]
    column = factory_distances[current_factory]
    return row[column]


df["Current Factory Distance (km)"] = df.apply(
    get_current_distance,
    axis=1
)


# =========================================
# FIND NEAREST FACTORY
# =========================================

distance_columns = list(factory_distances.values())

df["Nearest Factory"] = df[distance_columns].idxmin(axis=1)

# Convert distance column name to factory name
reverse_mapping = {
    value: key for key, value in factory_distances.items()
}

df["Nearest Factory"] = df["Nearest Factory"].map(reverse_mapping)

df["Nearest Factory Distance (km)"] = df[distance_columns].min(axis=1)


# =========================================
# DISTANCE REDUCTION
# =========================================

df["Potential Distance Reduction (km)"] = (
    df["Current Factory Distance (km)"]
    - df["Nearest Factory Distance (km)"]
)


# =========================================
# DISTANCE REDUCTION PERCENTAGE
# =========================================

df["Potential Distance Reduction (%)"] = (
    df["Potential Distance Reduction (km)"]
    / df["Current Factory Distance (km)"]
) * 100


# =========================================
# CHECK WHETHER REALLOCATION IS POSSIBLE
# =========================================

df["Reallocation Possible"] = (
    df["Nearest Factory"] != df["Current Factory"]
)


# =========================================
# SAVE RESULT
# =========================================

df.to_csv(output_file, index=False)


# =========================================
# RESULTS
# =========================================

print("\nFactory alternative analysis completed successfully!")

print("\nOutput File:")
print(output_file)

print("\nFinal Shape:")
print(df.shape)

print("\nReallocation Summary:")

print(
    df["Reallocation Possible"]
    .value_counts()
)

print("\nSample Results:")

columns_to_show = [
    "Product Name",
    "Current Factory",
    "Current Factory Distance (km)",
    "Nearest Factory",
    "Nearest Factory Distance (km)",
    "Potential Distance Reduction (km)",
    "Potential Distance Reduction (%)",
    "Reallocation Possible"
]

print(
    df[columns_to_show]
    .head(10)
    .to_string(index=False)
)