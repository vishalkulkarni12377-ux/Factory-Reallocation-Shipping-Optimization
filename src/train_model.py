import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


# =========================================
# 1. LOAD CLEANED DATASET
# =========================================

file_path = "data/cleaned_nassau_candy.csv"

df = pd.read_csv(file_path)

print("Dataset Shape:")
print(df.shape)


# =========================================
# 2. SELECT FEATURES
# =========================================

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

print("\nFeature Shape:")
print(X.shape)

print("\nTarget Shape:")
print(y.shape)


# =========================================
# 3. DEFINE CATEGORICAL AND NUMERICAL FEATURES
# =========================================

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


# =========================================
# 4. PREPROCESSING
# =========================================

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore", sparse_output=False),
            categorical_features
        ),
        (
            "numerical",
            StandardScaler(),
            numerical_features
        )
    ]
)


# =========================================
# 5. TRAIN-TEST SPLIT
# =========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining Data:")
print(X_train.shape)

print("\nTesting Data:")
print(X_test.shape)


# =========================================
# 6. DEFINE MODELS
# =========================================

models = {

    "Linear Regression": LinearRegression(),

    "Random Forest": RandomForestRegressor(
        n_estimators=100,
        random_state=42
    ),

    "Gradient Boosting": GradientBoostingRegressor(
        n_estimators=100,
        random_state=42
    )
}


# =========================================
# 7. TRAIN AND EVALUATE MODELS
# =========================================

results = []

best_model = None
best_model_name = None
best_rmse = float("inf")


for name, model in models.items():

    print("\n===================================")
    print("Training:", name)
    print("===================================")

    pipeline = Pipeline(
        steps=[
            ("preprocessing", preprocessor),
            ("model", model)
        ]
    )

    # Train model
    pipeline.fit(X_train, y_train)

    # Prediction
    y_pred = pipeline.predict(X_test)

    # Evaluation
    mae = mean_absolute_error(y_test, y_pred)

    rmse = np.sqrt(
        mean_squared_error(y_test, y_pred)
    )

    r2 = r2_score(y_test, y_pred)

    print("MAE :", round(mae, 4))
    print("RMSE:", round(rmse, 4))
    print("R2  :", round(r2, 4))

    results.append({
        "Model": name,
        "MAE": mae,
        "RMSE": rmse,
        "R2": r2
    })

    # Select best model using RMSE
    if rmse < best_rmse:
        best_rmse = rmse
        best_model = pipeline
        best_model_name = name


# =========================================
# 8. DISPLAY MODEL COMPARISON
# =========================================

results_df = pd.DataFrame(results)

print("\n===================================")
print("MODEL COMPARISON")
print("===================================")

print(results_df)


# =========================================
# 9. BEST MODEL
# =========================================

print("\n===================================")
print("BEST MODEL")
print("===================================")

print("Best Model:", best_model_name)
print("Best RMSE:", round(best_rmse, 4))


# =========================================
# 10. SAVE BEST MODEL
# =========================================

model_path = "models/best_shipping_model.pkl"

joblib.dump(best_model, model_path)

print("\nBest model saved successfully!")
print(model_path)


# =========================================
# 11. SAVE RESULTS
# =========================================

results_df.to_csv(
    "outputs/model_comparison.csv",
    index=False
)

print("\nModel comparison saved successfully!")
print("outputs/model_comparison.csv")


# =========================================
# 12. COMPLETION MESSAGE
# =========================================

print("\n===================================")
print("MODEL TRAINING COMPLETED!")
print("===================================")