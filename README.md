# Factory Reallocation and Shipping Optimization Recommendation System

## Project Overview

This project develops a Machine Learning based Factory Reallocation and Shipping Optimization Recommendation System for Nassau Candy Distributor.

The system analyzes order, product, customer, sales, cost, gross profit, destination, and shipping information to evaluate alternative factory allocation scenarios. It uses factory-to-destination distance analysis, machine learning, scenario simulation, and recommendation logic to identify potential shipping-efficiency improvements.

## Problem Statement

Nassau Candy Distributor uses factory-product assignments for fulfilling customer orders. Static factory assignments can result in longer shipping distances for some destinations and may affect shipping efficiency and profitability.

This project evaluates alternative factory scenarios and provides recommendations based on shipping distance and profit-related factors.

## Objectives

- Analyze the Nassau Candy order dataset.
- Prepare and preprocess the data for analysis.
- Calculate order lead time from order and ship dates.
- Map products to their current factories.
- Calculate distances between customer destinations and available factories.
- Analyze alternative factory scenarios.
- Use Machine Learning models for shipping-related analysis.
- Generate factory reallocation recommendations.
- Provide an interactive Streamlit dashboard.
- Allow users to compare alternative factory scenarios using speed and profit priorities.

## Dataset

The project uses the Nassau Candy Distributor dataset provided for the project.

The dataset contains the following fields:

- Row ID
- Order ID
- Order Date
- Ship Date
- Ship Mode
- Customer ID
- Country/Region
- City
- State/Province
- Postal Code
- Division
- Region
- Product ID
- Product Name
- Sales
- Units
- Gross Profit
- Cost

## Methodology

The project follows these major steps:

1. Data preprocessing
2. Data validation
3. Lead time calculation
4. Product-to-factory mapping
5. Destination geocoding
6. Factory-to-destination distance calculation
7. Alternative factory analysis
8. Scenario simulation
9. Machine Learning model preparation
10. Model training and comparison
11. Factory recommendation generation
12. Streamlit dashboard development

## Machine Learning

The project evaluates the following regression models:

- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor

The models are evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

The trained model is stored in the `models` folder.

## Factory Analysis

The project considers the following factories:

- Lot's O' Nuts
- Wicked Choccy's
- Sugar Shack
- Secret Factory
- The Other Factory

Destination coordinates are used to calculate the distance from customer destinations to the available factories.

Alternative factory scenarios are then evaluated based on distance and project-defined profit-related factors.

## Recommendation System

The recommendation system evaluates whether an alternative factory could provide a shipping-distance benefit.

The dashboard allows users to adjust the optimization priority between:

- Shipping speed
- Profit

The recommendation score changes according to the selected priority.

The recommendation results are intended as candidate scenarios and should be validated against actual factory capacity, manufacturing constraints, transportation costs, and operational feasibility before implementation.

## Streamlit Dashboard

The project includes an interactive Streamlit dashboard with the following modules:

- Project Overview
- What-If Scenario Analysis
- Region Filter
- Ship Mode Filter
- Product Selection
- Alternative Factory Selection
- Scenario Results
- Speed vs Profit Optimization Priority
- Recommendation Dashboard
- Risk & Impact Panel
- KPI Summary

## Key KPIs

The dashboard presents project-defined KPIs including:

- Shipping Efficiency Improvement
- Recommendation Coverage
- Profit Impact Stability
- Scenario Confidence Score

These KPIs are based on the implemented project methodology and should be interpreted as analytical indicators rather than guarantees of actual operational savings.

## Project Structure

```text
Factory_Reallocation_Optimization/
│
├── data/
│   ├── Nassau Candy Distributor.csv
│   ├── cleaned_nassau_candy.csv
│   ├── destination_coordinates.csv
│   ├── destination_factory_distances.csv
│   ├── factory_alternative_analysis.csv
│   ├── factory_recommendations.csv
│   ├── final_dataset.csv
│   ├── final_recommendations.csv
│   └── order_distance_dataset.csv
│
├── models/
│   └── best_shipping_model.pkl
│
├── notebooks/
│
├── outputs/
│   └── model_comparison.csv
│
├── src/
│   ├── app.py
│   ├── data_preprocessing.py
│   ├── ml_preparation.py
│   ├── train_model.py
│   ├── factory_mapping.py
│   ├── calculate_distances.py
│   ├── create_distance_dataset.py
│   ├── create_recommendations.py
│   ├── scenario_simulator.py
│   ├── recommendation_impact.py
│   └── other supporting scripts
│
├── requirements.txt
└── README.md