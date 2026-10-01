# =========================================
# CHECK GEOCODING LIBRARY
# =========================================

try:
    import geopy

    print("geopy is installed successfully!")
    print("geopy version:", geopy.__version__)

except ImportError:
    print("geopy is NOT installed.")
    print("We will install it in the next step.")