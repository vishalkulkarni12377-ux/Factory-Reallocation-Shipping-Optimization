import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

# ==========================================
# 1. LOAD CLEANED DATASET
# ==========================================

file_path = "data/cleaned_nassau_candy.csv"

df = pd.read_csv(file_path)

print("Dataset Shape:")
print(df.shape)


# ==========================================
# 2. SELECT FEATURES AND TARGET
# ==========================================

features = [
    "Ship Mode",
    "Division",
    "Region",
    "Product Name",
    "Sales",
    "Units",
    "Gross Profit",
    "Cost"
]

target = "Lead Time"

X = df[features]
y = df[target]


# ==========================================
# 3. CATEGORICAL AND NUMERICAL COLUMNS
# ==========================================

categorical_features = [
    "Ship Mode",
    "Division",
    "Region",
    "Product Name"
]

numerical_features = [
    "Sales",
    "Units",
    "Gross Profit",
    "Cost"
]


# ==========================================
# 4. ENCODE CATEGORICAL DATA
# ==========================================

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ],
    remainder="passthrough"
)


# ==========================================
# 5. TRANSFORM FEATURES
# ==========================================

X_encoded = preprocessor.fit_transform(X)


# ==========================================
# 6. TRAIN-TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X_encoded,
    y,
    test_size=0.20,
    random_state=42
)


# ==========================================
# 7. DISPLAY RESULTS
# ==========================================

print("\nOriginal Feature Shape:")
print(X.shape)

print("\nEncoded Feature Shape:")
print(X_encoded.shape)

print("\nTraining Data Shape:")
print(X_train.shape)

print("\nTesting Data Shape:")
print(X_test.shape)

print("\nTraining Target Shape:")
print(y_train.shape)

print("\nTesting Target Shape:")
print(y_test.shape)

print("\nML data preparation completed successfully!")