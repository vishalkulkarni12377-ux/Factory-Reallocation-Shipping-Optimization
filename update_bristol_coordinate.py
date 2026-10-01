import pandas as pd

file = "data/destination_coordinates.csv"

df = pd.read_csv(file)

condition = (
    (df["City"] == "Bristol") &
    (df["State/Province"] == "Tennessee") &
    (df["Postal Code"].astype(str) == "37620")
)

df.loc[condition, "Latitude"] = 36.5945034
df.loc[condition, "Longitude"] = -82.1885212

df.to_csv(file, index=False)

print("Bristol coordinate updated successfully!")

print("\nUpdated Record:")
print(df[condition].to_string(index=False))

print("\nMissing Coordinates:")
print(df[["Latitude", "Longitude"]].isna().sum())