import pandas as pd
import time
from geopy.geocoders import Nominatim

# =========================================
# GEOCODE DESTINATIONS
# =========================================

input_file = "data/final_dataset.csv"
output_file = "data/destination_coordinates.csv"

# Load dataset
df = pd.read_csv(input_file)

# Get unique destinations
destinations = (
    df[
        [
            "Country/Region",
            "City",
            "State/Province",
            "Postal Code"
        ]
    ]
    .drop_duplicates()
    .reset_index(drop=True)
)

print("Unique destinations to process:", len(destinations))

# Create geocoder
geolocator = Nominatim(
    user_agent="factory_reallocation_optimization"
)

# Store results
results = []

for index, row in destinations.iterrows():

    city = row["City"]
    state = row["State/Province"]
    country = row["Country/Region"]

    query = f"{city}, {state}, {country}"

    try:
        location = geolocator.geocode(
            query,
            timeout=10
        )

        if location:
            latitude = location.latitude
            longitude = location.longitude

            print(
                f"{index + 1}/{len(destinations)} "
                f"{city}, {state} -> "
                f"{latitude}, {longitude}"
            )

        else:
            latitude = None
            longitude = None

            print(
                f"{index + 1}/{len(destinations)} "
                f"{city}, {state} -> NOT FOUND"
            )

    except Exception as e:

        latitude = None
        longitude = None

        print(
            f"{index + 1}/{len(destinations)} "
            f"{city}, {state} -> ERROR: {e}"
        )

    results.append({
        "Country/Region": country,
        "City": city,
        "State/Province": state,
        "Postal Code": row["Postal Code"],
        "Latitude": latitude,
        "Longitude": longitude
    })

    # Small delay between requests
    time.sleep(1)


# =========================================
# SAVE COORDINATES
# =========================================

coordinates_df = pd.DataFrame(results)

coordinates_df.to_csv(
    output_file,
    index=False
)

print("\nDestination coordinates saved successfully!")
print("File:", output_file)

print("\nCoordinate Dataset Shape:")
print(coordinates_df.shape)

print("\nMissing Coordinates:")

print(
    coordinates_df[
        ["Latitude", "Longitude"]
    ].isna().sum()
)