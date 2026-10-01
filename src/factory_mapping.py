import pandas as pd

# =========================================
# PRODUCT - FACTORY MAPPING
# =========================================

file_path = "data/Nassau Candy Distributor.csv"

df = pd.read_csv(file_path)


# Current factory assigned to each product
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
# ADD CURRENT FACTORY
# =========================================

df["Current Factory"] = df["Product Name"].map(factory_mapping)


# =========================================
# CHECK MISSING FACTORY MAPPING
# =========================================

missing = df["Current Factory"].isna().sum()

print("Total Records:", len(df))
print("Missing Factory Mapping:", missing)


# =========================================
# DISPLAY MAPPING
# =========================================

print("\nProduct - Current Factory:")

mapping_check = (
    df[["Product Name", "Current Factory"]]
    .drop_duplicates()
    .sort_values("Product Name")
)

print(mapping_check.to_string(index=False))


# =========================================
# FACTORY RECORD COUNT
# =========================================

print("\nRecords by Factory:")

print(
    df["Current Factory"]
    .value_counts()
)


print("\nFactory mapping completed successfully!")