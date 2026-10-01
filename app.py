import streamlit as st
import pandas as pd


# =========================================
# PAGE CONFIGURATION
# =========================================

st.set_page_config(
    page_title="Factory Reallocation & Shipping Optimization",
    page_icon="🏭",
    layout="wide"
)


# =========================================
# LOAD DATA
# =========================================

data_file = "data/final_recommendations.csv"

df = pd.read_csv(data_file)


# =========================================
# TITLE
# =========================================

st.title("🏭 Factory Reallocation & Shipping Optimization")

st.write(
    "Nassau Candy Distributor - Factory Optimization Dashboard"
)

st.success("Dashboard loaded successfully!")


# =========================================
# PROJECT OVERVIEW
# =========================================

st.header("📊 Project Overview")

st.write(
    "This system analyzes factory-to-destination distances "
    "and evaluates candidate factory reallocation scenarios."
)


# =========================================
# WHAT-IF SCENARIO ANALYSIS
# =========================================

st.header("🔄 What-If Scenario Analysis")

st.write(
    "Select a product, region, and ship mode to analyze "
    "the potential shipping-distance impact."
)


# =========================================
# REGION SELECTOR
# =========================================

regions = sorted(
    df["Region"].dropna().unique()
)

region_options = ["All"] + regions

selected_region = st.selectbox(
    "Select Region",
    region_options
)


# =========================================
# SHIP MODE FILTER
# =========================================

ship_modes = sorted(
    df["Ship Mode"].dropna().unique()
)

ship_mode_options = ["All"] + ship_modes

selected_ship_mode = st.selectbox(
    "Select Ship Mode",
    ship_mode_options
)


# =========================================
# APPLY REGION AND SHIP MODE FILTERS
# =========================================

filtered_df = df.copy()

if selected_region != "All":
    filtered_df = filtered_df[
        filtered_df["Region"] == selected_region
    ]

if selected_ship_mode != "All":
    filtered_df = filtered_df[
        filtered_df["Ship Mode"] == selected_ship_mode
    ]


# =========================================
# KPI SUMMARY
# =========================================

st.header("📈 Key Performance Indicators (KPIs)")

st.write(
    "The following KPIs summarize the potential impact of "
    "the candidate factory reallocation scenarios."
)


# =========================================
# KPI DATA
# =========================================

total_kpi_records = len(filtered_df)

recommended_kpi_data = filtered_df[
    filtered_df["Final Recommendation"]
    == "Recommended for Analysis"
].copy()

recommended_kpi_count = len(recommended_kpi_data)


# =========================================
# KPI 1
# SHIPPING EFFICIENCY IMPROVEMENT
# =========================================

if recommended_kpi_count > 0:

    positive_reduction_data = recommended_kpi_data[
        recommended_kpi_data["Distance Reduction (%)"] > 0
    ]

    if len(positive_reduction_data) > 0:

        shipping_efficiency_improvement = (
            positive_reduction_data[
                "Distance Reduction (%)"
            ].mean()
        )

    else:

        shipping_efficiency_improvement = 0

else:

    shipping_efficiency_improvement = 0


# =========================================
# KPI 2
# RECOMMENDATION COVERAGE
# =========================================

if total_kpi_records > 0:

    recommendation_coverage_kpi = (
        recommended_kpi_count
        / total_kpi_records
    ) * 100

else:

    recommendation_coverage_kpi = 0


# =========================================
# KPI 3
# PROFIT IMPACT STABILITY
# =========================================

if recommended_kpi_count > 1:

    profit_margin_mean = (
        recommended_kpi_data[
            "Profit Margin (%)"
        ].mean()
    )

    profit_margin_std = (
        recommended_kpi_data[
            "Profit Margin (%)"
        ].std()
    )

    if profit_margin_mean != 0:

        profit_variation = (
            profit_margin_std
            / abs(profit_margin_mean)
        ) * 100

        profit_impact_stability = max(
            0,
            100 - profit_variation
        )

    else:

        profit_impact_stability = 0

else:

    profit_impact_stability = 0


# =========================================
# KPI 4
# SCENARIO CONFIDENCE SCORE
# =========================================

if recommended_kpi_count > 0:

    positive_scenarios = len(
        recommended_kpi_data[
            recommended_kpi_data[
                "Distance Reduction (km)"
            ] > 0
        ]
    )

    scenario_confidence_score = (
        positive_scenarios
        / recommended_kpi_count
    ) * 100

else:

    scenario_confidence_score = 0


# =========================================
# DISPLAY KPI CARDS
# =========================================

kpi1, kpi2, kpi3, kpi4 = st.columns(4)


with kpi1:

    st.metric(
        "Shipping Efficiency Improvement",
        f"{shipping_efficiency_improvement:.2f}%"
    )


with kpi2:

    st.metric(
        "Recommendation Coverage",
        f"{recommendation_coverage_kpi:.2f}%"
    )


with kpi3:

    st.metric(
        "Profit Impact Stability",
        f"{profit_impact_stability:.2f}%"
    )


with kpi4:

    st.metric(
        "Scenario Confidence Score",
        f"{scenario_confidence_score:.2f}%"
    )


# =========================================
# KPI METHODOLOGY
# =========================================

with st.expander("📖 KPI Calculation Methodology"):

    st.write(
        "**Shipping Efficiency Improvement:** "
        "Average positive distance reduction percentage "
        "among recommended cases."
    )

    st.write(
        "**Recommendation Coverage:** "
        "Recommended cases divided by total filtered cases "
        "multiplied by 100."
    )

    st.write(
        "**Profit Impact Stability:** "
        "A stability indicator derived from the variation "
        "of profit margin among recommended cases."
    )

    st.write(
        "**Scenario Confidence Score:** "
        "Percentage of recommended scenarios that produce "
        "a positive distance reduction."
    )

    st.info(
        "These KPIs evaluate candidate scenarios using "
        "destination distance as a shipping-efficiency proxy. "
        "They do not represent confirmed transportation savings "
        "or actual delivery-time improvements."
    )


# =========================================
# PRODUCT SELECTION
# =========================================

products = sorted(
    filtered_df["Product Name"].dropna().unique()
)

if len(products) == 0:

    st.warning(
        "No products are available for the selected "
        "Region and Ship Mode."
    )

    st.stop()


selected_product = st.selectbox(
    "Select Product",
    products
)


# =========================================
# FACTORY SELECTION
# =========================================

factories = [
    "Lot's O' Nuts",
    "Wicked Choccy's",
    "Sugar Shack",
    "Secret Factory",
    "The Other Factory"
]

selected_factory = st.selectbox(
    "Select Alternative Factory",
    factories
)


# =========================================
# FACTORY DISTANCE COLUMNS
# =========================================

factory_columns = {
    "Lot's O' Nuts": "Lot's O' Nuts Distance (km)",
    "Wicked Choccy's": "Wicked Choccy's Distance (km)",
    "Sugar Shack": "Sugar ShackDistance (km)",
    "Secret Factory": "Secret Factory Distance (km)",
    "The Other Factory": "The Other Factory Distance (km)"
}


# =========================================
# FILTER PRODUCT
# =========================================

product_data = filtered_df[
    filtered_df["Product Name"] == selected_product
].copy()


# =========================================
# CALCULATE SCENARIO
# =========================================

distance_column = factory_columns[selected_factory]

current_column = "Current Factory Distance (km)"

product_data["Scenario Distance (km)"] = (
    product_data[distance_column]
)

product_data["Distance Reduction (km)"] = (
    product_data[current_column]
    - product_data["Scenario Distance (km)"]
)


# =========================================
# AVERAGE VALUES
# =========================================

average_current = product_data[
    current_column
].mean()

average_scenario = product_data[
    "Scenario Distance (km)"
].mean()

average_reduction = (
    average_current
    - average_scenario
)


if average_current != 0:

    average_reduction_percentage = (
        average_reduction
        / average_current
    ) * 100

else:

    average_reduction_percentage = 0


average_profit = product_data[
    "Gross Profit"
].mean()


# =========================================
# DISPLAY SCENARIO RESULTS
# =========================================

st.subheader("Scenario Results")

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "Matching Orders",
        len(product_data)
    )


with col2:

    st.metric(
        "Current Distance",
        f"{average_current:.2f} km"
    )


with col3:

    st.metric(
        "Scenario Distance",
        f"{average_scenario:.2f} km"
    )


with col4:

    st.metric(
        "Distance Reduction",
        f"{average_reduction:.2f} km"
    )


# =========================================
# PERCENTAGE AND PROFIT
# =========================================

col5, col6 = st.columns(2)


with col5:

    st.metric(
        "Distance Reduction %",
        f"{average_reduction_percentage:.2f}%"
    )


with col6:

    st.metric(
        "Average Gross Profit",
        f"{average_profit:.2f}"
    )


# =========================================
# SCENARIO INFORMATION
# =========================================

st.subheader("Scenario Information")

st.write(
    f"**Product:** {selected_product}"
)

st.write(
    f"**Region:** {selected_region}"
)

st.write(
    f"**Ship Mode:** {selected_ship_mode}"
)

st.write(
    f"**Candidate Alternative Factory:** {selected_factory}"
)


st.info(
    "This scenario uses destination distance as a proxy for "
    "shipping efficiency. It represents a candidate factory "
    "reallocation scenario and does not confirm actual "
    "manufacturing or shipping feasibility."
)


# =========================================
# SPEED VS PROFIT OPTIMIZATION PRIORITY
# =========================================

st.header("⚖️ Speed vs Profit Optimization Priority")

st.write(
    "Adjust the priority between shipping-distance efficiency "
    "and profitability."
)


# =========================================
# PRIORITY SLIDER
# =========================================

speed_priority = st.slider(
    "Speed Priority (%)",
    min_value=0,
    max_value=100,
    value=70,
    step=10
)

profit_priority = 100 - speed_priority


# =========================================
# DISPLAY PRIORITIES
# =========================================

col1, col2 = st.columns(2)


with col1:

    st.metric(
        "Shipping Speed Priority",
        f"{speed_priority}%"
    )


with col2:

    st.metric(
        "Profit Priority",
        f"{profit_priority}%"
    )


# =========================================
# DYNAMIC OPTIMIZATION
# =========================================

optimization_data = filtered_df.copy()

optimization_data["Dynamic Recommendation Score"] = (
    optimization_data["Distance Benefit Score"]
    * (speed_priority / 100)
    +
    optimization_data["Profit Margin (%)"]
    * (profit_priority / 100)
)


# =========================================
# DYNAMIC RANKING
# =========================================

optimization_data["Dynamic Recommendation Rank"] = (
    optimization_data[
        "Dynamic Recommendation Score"
    ]
    .rank(
        method="min",
        ascending=False
    )
)


# =========================================
# OPTIMIZATION RESULT
# =========================================

st.subheader("Optimization Result")

st.write(
    f"The current setting gives **{speed_priority}% importance "
    f"to shipping speed** and **{profit_priority}% importance "
    f"to profit margin**."
)


# =========================================
# OPTIMIZATION TABLE
# =========================================

optimization_columns = [
    "Product Name",
    "Region",
    "Ship Mode",
    "Current Factory",
    "Recommended Factory",
    "Distance Reduction (km)",
    "Distance Reduction (%)",
    "Distance Benefit Score",
    "Profit Margin (%)",
    "Dynamic Recommendation Score",
    "Dynamic Recommendation Rank"
]


available_optimization_columns = [
    column
    for column in optimization_columns
    if column in optimization_data.columns
]


st.dataframe(
    optimization_data[
        available_optimization_columns
    ].sort_values(
        "Dynamic Recommendation Score",
        ascending=False
    ),
    use_container_width=True,
    height=500
)


# =========================================
# RECOMMENDATION DASHBOARD
# =========================================

st.header("📋 Recommendation Dashboard")

st.write(
    "View candidate factory reallocation recommendations "
    "generated from the distance and profit analysis."
)


# =========================================
# RECOMMENDATION FILTER
# =========================================

recommendation_status = st.selectbox(
    "Select Recommendation Status",
    [
        "All",
        "Recommended for Analysis",
        "No Reallocation"
    ]
)


# =========================================
# FILTER RECOMMENDATIONS
# =========================================

recommendation_data = filtered_df.copy()


if recommendation_status != "All":

    recommendation_data = recommendation_data[
        recommendation_data["Final Recommendation"]
        == recommendation_status
    ]


# =========================================
# DISPLAY SUMMARY
# =========================================

st.subheader("Recommendation Summary")

col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "Total Orders",
        len(recommendation_data)
    )


with col2:

    high_priority = len(
        recommendation_data[
            recommendation_data["Priority"]
            == "High"
        ]
    )

    st.metric(
        "High Priority",
        high_priority
    )


with col3:

    medium_priority = len(
        recommendation_data[
            recommendation_data["Priority"]
            == "Medium"
        ]
    )

    st.metric(
        "Medium Priority",
        medium_priority
    )


# =========================================
# RECOMMENDATION TABLE
# =========================================

st.subheader("Factory Reallocation Recommendations")


display_columns = [
    "Product Name",
    "Region",
    "Ship Mode",
    "Current Factory",
    "Recommended Factory",
    "Distance Reduction (km)",
    "Distance Reduction (%)",
    "Priority",
    "Final Recommendation"
]


available_columns = [
    column
    for column in display_columns
    if column in recommendation_data.columns
]


st.dataframe(
    recommendation_data[
        available_columns
    ],
    use_container_width=True,
    height=600
)


# =========================================
# RISK & IMPACT PANEL
# =========================================

st.header("⚠️ Risk & Impact Panel")

st.write(
    "This section summarizes the potential impact and risk "
    "of the candidate factory reallocation recommendations."
)


# =========================================
# RECOMMENDATION COUNTS
# =========================================

recommended_count = len(
    filtered_df[
        filtered_df["Final Recommendation"]
        == "Recommended for Analysis"
    ]
)


no_reallocation_count = len(
    filtered_df[
        filtered_df["Final Recommendation"]
        == "No Reallocation"
    ]
)


high_priority_count = len(
    filtered_df[
        filtered_df["Priority"]
        == "High"
    ]
)


medium_priority_count = len(
    filtered_df[
        filtered_df["Priority"]
        == "Medium"
    ]
)


low_priority_count = len(
    filtered_df[
        filtered_df["Priority"]
        == "Low"
    ]
)


# =========================================
# RECOMMENDATION COVERAGE
# =========================================

total_records = len(filtered_df)


if total_records > 0:

    recommendation_coverage = (
        recommended_count
        / total_records
    ) * 100

else:

    recommendation_coverage = 0


# =========================================
# AVERAGE DISTANCE IMPACT
# =========================================

recommended_data = filtered_df[
    filtered_df["Final Recommendation"]
    == "Recommended for Analysis"
]


if len(recommended_data) > 0:

    average_distance_reduction = (
        recommended_data[
            "Distance Reduction (km)"
        ].mean()
    )

    average_distance_percentage = (
        recommended_data[
            "Distance Reduction (%)"
        ].mean()
    )

else:

    average_distance_reduction = 0
    average_distance_percentage = 0


# =========================================
# DISPLAY IMPACT METRICS
# =========================================

st.subheader("Impact Summary")

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "Recommended Cases",
        recommended_count
    )


with col2:

    st.metric(
        "No Reallocation",
        no_reallocation_count
    )


with col3:

    st.metric(
        "Recommendation Coverage",
        f"{recommendation_coverage:.2f}%"
    )


with col4:

    st.metric(
        "Avg Distance Reduction",
        f"{average_distance_reduction:.2f} km"
    )


# =========================================
# PRIORITY SUMMARY
# =========================================

st.subheader("Priority Distribution")

col5, col6, col7 = st.columns(3)


with col5:

    st.metric(
        "High Priority",
        high_priority_count
    )


with col6:

    st.metric(
        "Medium Priority",
        medium_priority_count
    )


with col7:

    st.metric(
        "Low Priority",
        low_priority_count
    )


# =========================================
# IMPACT INFORMATION
# =========================================

st.subheader("Impact Information")


st.write(
    f"Average distance reduction among recommended cases: "
    f"**{average_distance_reduction:.2f} km**"
)


st.write(
    f"Average percentage distance reduction among recommended cases: "
    f"**{average_distance_percentage:.2f}%**"
)


# =========================================
# FINAL VALIDATION WARNING
# =========================================

st.warning(
    "These results are candidate scenarios based on destination "
    "distance as a shipping-efficiency proxy. They should be "
    "validated against actual factory capacity, manufacturing "
    "constraints, transportation costs, and operational feasibility "
    "before implementation."
)