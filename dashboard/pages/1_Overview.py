import streamlit as st
import plotly.express as px

from utils import load_dashboard_data
st.set_page_config(layout="wide")

st.title("📊 Overview")

# -------------------------
# Load Cached Data
# -------------------------

data = load_dashboard_data()

total_trips = data["total_trips"].iloc[0, 0]
total_revenue = data["total_revenue"].iloc[0, 0]
avg_fare = data["avg_fare"].iloc[0, 0]
avg_distance = data["avg_trip_distance"].iloc[0, 0]
avg_duration = data["avg_trip_duration"].iloc[0, 0]

monthly_trips = data["monthly_trips"]
monthly_revenue = data["monthly_revenue"]

# -------------------------
# KPI Cards
# -------------------------

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Total Trips",
    f"{total_trips:,}"
)

col2.metric(
    "Total Revenue",
    f"${total_revenue/1_000_000:.2f} M"
)

col3.metric(
    "Average Fare",
    f"${avg_fare:.2f}"
)

col4.metric(
    "Average Distance",
    f"{avg_distance:.2f} miles"
)

col5.metric(
    "Average Duration",
    f"{avg_duration:.2f} mins"
)

# -------------------------
# Charts
# -------------------------

fig1 = px.bar(
    monthly_trips,
    x="pickup_month",
    y="total_trips",
    title="Monthly Trips"
)

fig2 = px.line(
    monthly_revenue,
    x="pickup_month",
    y="revenue",
    title="Monthly Revenue",
    markers=True
)

left, right = st.columns(2)

left.plotly_chart(fig1, use_container_width=True)

right.plotly_chart(fig2, use_container_width=True)