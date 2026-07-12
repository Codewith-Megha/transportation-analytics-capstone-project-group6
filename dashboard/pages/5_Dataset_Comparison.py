import streamlit as st
import plotly.express as px
import pandas as pd

from utils import load_dashboard_data
st.set_page_config(layout="wide")

st.title("🚕 Dataset Comparison")

# ------------------------------------
# Load Cached Data
# ------------------------------------

data = load_dashboard_data()

comparison = data["dataset_comparison"]

yellow = data["monthly_trips"].copy()
green = data["green"].copy()
fhv = data["fhv"].copy()

# ------------------------------------
# Dataset Comparison
# ------------------------------------

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

yellow["dataset"] = "Yellow"
green["dataset"] = "Green"
fhv["dataset"] = "FHV"

yellow = yellow.rename(columns={"total_trips": "trips"})
green = green.rename(columns={"total_trips": "trips"})
fhv = fhv.rename(columns={"total_trips": "trips"})

comparison_df = pd.concat(
    [
        yellow[["pickup_month", "trips", "dataset"]],
        green[["pickup_month", "trips", "dataset"]],
        fhv[["pickup_month", "trips", "dataset"]],
    ],
    ignore_index=True,
)

fig2 = px.line(
    comparison_df,
    x="pickup_month",
    y="trips",
    color="dataset",
    markers=True,
    title="Monthly Dataset Comparison"
)

st.plotly_chart(fig2, use_container_width=True)