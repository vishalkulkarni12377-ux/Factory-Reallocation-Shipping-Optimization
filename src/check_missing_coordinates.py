import pandas as pd

file = "data/destination_coordinates.csv"

df = pd.read_csv(file)

missing = df[df["Latitude"].isna() | df["Longitude"].isna()]

print("Missing Coordinate Records:")
print(missing.to_string(index=False))

print("\nTotal Missing Destinations:", len(missing))