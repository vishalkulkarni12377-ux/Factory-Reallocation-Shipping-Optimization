from geopy.geocoders import Nominatim
import time

geolocator = Nominatim(user_agent="factory_reallocation_optimization")

city = "Bristol"
state = "Tennessee"
country = "United States"
postal_code = "37620"

query = f"{city}, {state}, {postal_code}, {country}"

print("Searching for:", query)

location = geolocator.geocode(query, timeout=30)

if location:
    print("\nCoordinate Found!")
    print("Latitude:", location.latitude)
    print("Longitude:", location.longitude)
    print("Address:", location.address)
else:
    print("\nCoordinate not found.")

time.sleep(1)