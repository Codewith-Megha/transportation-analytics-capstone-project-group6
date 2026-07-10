import streamlit as st
import plotly.express as px

from utils import run_query
from src.analytics import queries

st.set_page_config(layout="wide")

st.title("🚕 Dataset Comparison")

# ------------------------------------
# Dataset Comparison
# ------------------------------------

comparison = run_query(queries.DATASET_COMPARISON)

fig1 = px.bar(
    comparison,
    x="dataset",
    y="total_trips",
    color="dataset",
    title="Trips Across Datasets"
)

st.plotly_chart(fig1, use_container_width=True)

# ------------------------------------
# Monthly Comparison
# ------------------------------------

yellow = run_query(queries.MONTHLY_TRIPS)
yellow["dataset"] = "Yellow"

green = run_query(queries.GREEN_MONTHLY_TRIPS)
green["dataset"] = "Green"

fhv = run_query(queries.FHV_MONTHLY_TRIPS)
fhv["dataset"] = "FHV"

combined = yellow.rename(columns={"total_trips": "trips"})
green = green.rename(columns={"total_trips": "trips"})
fhv = fhv.rename(columns={"total_trips": "trips"})

combined = combined[["pickup_month", "trips", "dataset"]]

green = green[["pickup_month", "trips", "dataset"]]

fhv = fhv[["pickup_month", "trips", "dataset"]]

comparison_df = combined

comparison_df = comparison_df._append(green, ignore_index=True)
comparison_df = comparison_df._append(fhv, ignore_index=True)

fig2 = px.line(
    comparison_df,
    x="pickup_month",
    y="trips",
    color="dataset",
    markers=True,
    title="Monthly Dataset Comparison"
)

st.plotly_chart(fig2, use_container_width=True)