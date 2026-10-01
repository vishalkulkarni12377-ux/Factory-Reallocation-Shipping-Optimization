import pandas as pd
from math import radians, sin, cos, sqrt, atan2

# =========================================
# FILE PATHS
# =========================================

input_file = "data/destination_coordinates.csv"
output_file = "data/destination_factory_distances.csv"


# =========================================
# FACTORY COORDINATES
# =========================================

factories = {
    "Lot's O' Nuts": (32.881893, -111.768036),
    "Wicked Choccy's": (32.076176, -81.088371),
    "Sugar Shack": (48.11914, -96.18115),
    "Secret Factory": (41.446333, -90.565487),
    "The Other Factory": (35.1175, -89.971107)
}


# =========================================
# HAVERSINE DISTANCE FUNCTION
# =========================================

def calculate_distance(lat1, lon1, lat2, lon2):

    R = 6371  # Earth radius in kilometers

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        sin(dlat / 2) ** 2
        + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    )

    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c


# =========================================
# LOAD DESTINATION DATA
# =========================================

df = pd.read_csv(input_file)

print("Destination Dataset Shape:", df.shape)


# =========================================
# CALCULATE DISTANCE TO EACH FACTORY
# =========================================

for factory_name, (factory_lat, factory_lon) in factories.items():

    column_name = factory_name + " Distance (km)"

    df[column_name] = df.apply(
        lambda row: calculate_distance(
            row["Latitude"],
            row["Longitude"],
            factory_lat,
            factory_lon
        ),
        axis=1
    )


# =========================================
# SAVE RESULT
# =========================================

df.to_csv(output_file, index=False)


# =========================================
# DISPLAY RESULTS
# =========================================

print("\nDistance calculation completed successfully!")

print("\nOutput File:")
print(output_file)

print("\nFinal Dataset Shape:")
print(df.shape)

print("\nDistance Columns:")

for factory_name in factories:
    print(factory_name + " Distance (km)")

print("\nFirst 5 Records:")
print(df.head().to_string(index=False))