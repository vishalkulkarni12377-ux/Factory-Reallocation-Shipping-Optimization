import pandas as pd

# =========================================
# FILE PATHS
# =========================================

input_file = "data/factory_recommendations.csv"
output_file = "data/final_recommendations.csv"


# =========================================
# LOAD DATA
# =========================================

df = pd.read_csv(input_file)

print("Input Dataset Shape:", df.shape)


# =========================================
# IMPACT CALCULATIONS
# =========================================

# Distance reduction is already calculated.
# We use Gross Profit as the historical profitability measure.

df["Profit Margin (%)"] = (
    df["Gross Profit"] / df["Sales"]
) * 100


# =========================================
# NORMALIZED DISTANCE BENEFIT
# =========================================

max_reduction = df["Distance Reduction (km)"].max()

if max_reduction > 0:
    df["Distance Benefit Score"] = (
        df["Distance Reduction (km)"] / max_reduction
    ) * 100
else:
    df["Distance Benefit Score"] = 0


# =========================================
# RECOMMENDATION SCORE
# =========================================

# Distance is the main optimization factor.
# Profit margin is used as a supporting business factor.

df["Recommendation Score"] = (
    0.70 * df["Distance Benefit Score"]
    + 0.30 * df["Profit Margin (%)"]
)


# =========================================
# REMOVE NEGATIVE DISTANCE REDUCTIONS
# =========================================

df.loc[
    df["Distance Reduction (km)"] <= 0,
    "Recommendation Score"
] = 0


# =========================================
# RANK RECOMMENDATIONS
# =========================================

df["Recommendation Rank"] = (
    df["Recommendation Score"]
    .rank(method="dense", ascending=False)
)


# =========================================
# PRIORITY
# =========================================

def assign_priority(score):

    if score >= 50:
        return "High"

    elif score >= 20:
        return "Medium"

    else:
        return "Low"


df["Priority"] = df["Recommendation Score"].apply(
    assign_priority
)


# =========================================
# FINAL RECOMMENDATION
# =========================================

df["Final Recommendation"] = "No Reallocation"

df.loc[
    (df["Distance Reduction (km)"] > 0) &
    (df["Recommendation Score"] >= 20),
    "Final Recommendation"
] = "Recommended for Analysis"


# =========================================
# SAVE
# =========================================

df.to_csv(output_file, index=False)


# =========================================
# RESULTS
# =========================================

print("\nRecommendation impact analysis completed!")

print("\nOutput File:")
print(output_file)

print("\nFinal Dataset Shape:")
print(df.shape)

print("\nPriority Summary:")
print(df["Priority"].value_counts())

print("\nFinal Recommendation Summary:")
print(df["Final Recommendation"].value_counts())


# =========================================
# TOP 10
# =========================================

columns = [
    "Product Name",
    "Current Factory",
    "Recommended Factory",
    "Distance Reduction (km)",
    "Distance Reduction (%)",
    "Sales",
    "Gross Profit",
    "Profit Margin (%)",
    "Recommendation Score",
    "Priority",
    "Final Recommendation"
]

print("\nTop 10 Recommendations:")

top10 = (
    df[df["Final Recommendation"] == "Recommended for Analysis"]
    .sort_values("Recommendation Score", ascending=False)
    .head(10)
)

print(
    top10[columns].to_string(index=False)
)