import streamlit as st

from utils import run_query
from src.analytics import queries

st.set_page_config(layout="wide")

st.title("📊 Overview")

# -------------------------
# Load KPI Data
# -------------------------

total_trips = run_query(queries.TOTAL_TRIPS).iloc[0, 0]

total_revenue = run_query(queries.TOTAL_REVENUE).iloc[0, 0]

avg_fare = run_query(queries.AVERAGE_FARE_OVERALL).iloc[0, 0]

avg_distance = run_query(queries.AVERAGE_TRIP_DISTANCE).iloc[0, 0]

avg_duration = run_query(queries.AVERAGE_TRIP_DURATION).iloc[0, 0]

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
import plotly.express as px

# -------------------------
# Monthly Trips
# -------------------------

monthly_trips = run_query(queries.MONTHLY_TRIPS)

fig1 = px.bar(
    monthly_trips,
    x="pickup_month",
    y="total_trips",
    title="Monthly Trips"
)

# -------------------------
# Monthly Revenue
# -------------------------

monthly_revenue = run_query(queries.MONTHLY_REVENUE)

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