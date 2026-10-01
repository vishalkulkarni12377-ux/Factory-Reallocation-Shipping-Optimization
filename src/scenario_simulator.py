import pandas as pd

# =========================================
# FILE
# =========================================

input_file = "data/final_recommendations.csv"

df = pd.read_csv(input_file)

print("Dataset loaded successfully!")
print("Total Orders:", len(df))


# =========================================
# USER INPUT
# =========================================

product = input("Enter Product Name: ").strip()

factory = input("Enter Alternative Factory: ").strip()


# =========================================
# FILTER PRODUCT
# =========================================

product_data = df[
    df["Product Name"].str.lower() == product.lower()
].copy()


if product_data.empty:

    print("\nProduct not found.")

else:

    # =====================================
    # FACTORY DISTANCE COLUMN
    # =====================================

    factory_columns = {
        "Lot's O' Nuts": "Lot's O' Nuts Distance (km)",
        "Wicked Choccy's": "Wicked Choccy's Distance (km)",
        "Sugar Shack": "Sugar Shack Distance (km)",
        "Secret Factory": "Secret Factory Distance (km)",
        "The Other Factory": "The Other Factory Distance (km)"
    }

    if factory not in factory_columns:

        print("\nFactory not found.")

    else:

        distance_column = factory_columns[factory]

        # =================================
        # CURRENT FACTORY DISTANCE
        # =================================

        current_column = "Current Factory Distance (km)"

        product_data["Scenario Factory"] = factory

        product_data["Scenario Distance (km)"] = (
            product_data[distance_column]
        )

        product_data["Scenario Distance Reduction (km)"] = (
            product_data[current_column]
            - product_data["Scenario Distance (km)"]
        )

        product_data["Scenario Distance Reduction (%)"] = (
            product_data["Scenario Distance Reduction (km)"]
            / product_data[current_column]
        ) * 100


        # =================================
        # DISPLAY RESULT
        # =================================

        print("\n========================================")
        print("WHAT-IF SCENARIO RESULT")
        print("========================================")

        print("\nProduct:")
        print(product)

        print("\nAlternative Factory:")
        print(factory)

        print("\nNumber of Matching Orders:")
        print(len(product_data))

        print("\nAverage Current Distance:")
        print(
            round(
                product_data[current_column].mean(),
                2
            ),
            "km"
        )

        print("\nAverage Scenario Distance:")
        print(
            round(
                product_data["Scenario Distance (km)"].mean(),
                2
            ),
            "km"
        )

        print("\nAverage Distance Reduction:")
        print(
            round(
                product_data[
                    "Scenario Distance Reduction (km)"
                ].mean(),
                2
            ),
            "km"
        )


        # =================================
        # AVERAGE DISTANCE REDUCTION %
        # =================================

        average_current = product_data[
            current_column
        ].mean()

        average_scenario = product_data[
            "Scenario Distance (km)"
        ].mean()

        average_reduction_percentage = (
            (average_current - average_scenario)
            / average_current
        ) * 100

        print("\nAverage Distance Reduction:")
        print(
            round(
                average_reduction_percentage,
                2
            ),
            "%"
        )


        # =================================
        # AVERAGE GROSS PROFIT
        # =================================

        print("\nAverage Gross Profit:")
        print(
            round(
                product_data["Gross Profit"].mean(),
                2
            )
        )


        print("\n========================================")