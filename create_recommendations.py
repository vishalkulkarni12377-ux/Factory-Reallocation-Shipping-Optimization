import pandas as pd

# =========================================
# FILE PATHS
# =========================================

input_file = "data/factory_alternative_analysis.csv"
output_file = "data/factory_recommendations.csv"


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
# PRODUCT → CURRENT FACTORY MAPPING
# =========================================

product_factory = {
    "Wonka Bar - Nutty Crunch Surprise": "Lot's O' Nuts",
    "Wonka Bar - Fudge Mallows": "Lot's O' Nuts",
    "Wonka Bar -Scrumdiddlyumptious": "Lot's O' Nuts",

    "Wonka Bar - Milk Chocolate": "Wicked Choccy's",
    "Wonka Bar - Triple Dazzle Caramel": "Wicked Choccy's",

    "Laffy Taffy": "Sugar Shack",
    "SweeTARTS": "Sugar Shack",
    "Nerds": "Sugar Shack",
    "Fun Dip": "Sugar Shack",

    "Everlasting Gobstopper": "Secret Factory",
    "Lickable Wallpaper": "Secret Factory",
    "Wonka Gum": "Secret Factory",

    "Hair Toffee": "The Other Factory",
    "Kazookles": "The Other Factory",

    "Fizzy Lifting Drinks": "Sugar Shack"
}


# =========================================
# CHECK PRODUCT MAPPING
# =========================================

df["Mapped Factory"] = df["Product Name"].map(product_factory)

missing_mapping = df["Mapped Factory"].isna().sum()

print("\nProducts without mapping:", missing_mapping)


# =========================================
# FIND BEST ALTERNATIVE FACTORY
# =========================================

def find_best_alternative(row):

    current_factory = row["Current Factory"]

    alternatives = {}

    for factory, column in factory_distances.items():

        if factory != current_factory:
            alternatives[factory] = row[column]

    if not alternatives:
        return pd.Series([
            current_factory,
            row[factory_distances[current_factory]],
            0
        ])

    best_factory = min(alternatives, key=alternatives.get)
    best_distance = alternatives[best_factory]

    current_distance = row[factory_distances[current_factory]]

    reduction = current_distance - best_distance

    return pd.Series([
        best_factory,
        best_distance,
        reduction
    ])


# =========================================
# APPLY ALTERNATIVE ANALYSIS
# =========================================

result = df.apply(find_best_alternative, axis=1)

result.columns = [
    "Recommended Factory",
    "Recommended Distance (km)",
    "Distance Reduction (km)"
]

df = pd.concat([df, result], axis=1)


# =========================================
# DISTANCE REDUCTION %
# =========================================

df["Distance Reduction (%)"] = (
    df["Distance Reduction (km)"]
    / df["Current Factory Distance (km)"]
) * 100


# =========================================
# RECOMMENDATION STATUS
# =========================================

df["Recommendation"] = "No Reallocation"

df.loc[
    df["Distance Reduction (km)"] > 0,
    "Recommendation"
] = "Consider Reallocation"


# =========================================
# SAVE
# =========================================

df.to_csv(output_file, index=False)


# =========================================
# RESULTS
# =========================================

print("\nRecommendation analysis completed successfully!")

print("\nOutput File:")
print(output_file)

print("\nFinal Shape:")
print(df.shape)

print("\nRecommendation Summary:")
print(df["Recommendation"].value_counts())

print("\nSample Recommendations:")

columns = [
    "Product Name",
    "Current Factory",
    "Current Factory Distance (km)",
    "Recommended Factory",
    "Recommended Distance (km)",
    "Distance Reduction (km)",
    "Distance Reduction (%)",
    "Recommendation"
]

print(
    df[columns]
    .head(10)
    .to_string(index=False)
)