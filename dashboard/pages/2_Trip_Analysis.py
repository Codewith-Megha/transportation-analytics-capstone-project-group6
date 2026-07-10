import streamlit as st
import plotly.express as px

from utils import run_query
from src.analytics import queries

st.set_page_config(layout="wide")

st.title("🚖 Trip Analysis")

# -----------------------------
# Monthly Trips
# -----------------------------

monthly = run_query(queries.MONTHLY_TRIPS)

fig1 = px.bar(
    monthly,
    x="pickup_month",
    y="total_trips",
    title="Monthly Trips"
)

# -----------------------------
# Trips by Hour
# -----------------------------

hourly = run_query(queries.HOURLY_TRIPS)

fig2 = px.line(
    hourly,
    x="pickup_hour",
    y="total_trips",
    markers=True,
    title="Trips by Hour"
)

# -----------------------------
# Trips by Weekday
# -----------------------------

weekday = run_query(queries.WEEKDAY_TRIPS)

fig3 = px.bar(
    weekday,
    x="pickup_weekday",
    y="total_trips",
    title="Trips by Weekday"
)

# -----------------------------
# Trip Category
# -----------------------------

category = run_query(queries.TRIP_CATEGORY)

fig4 = px.pie(
    category,
    names="trip_category",
    values="total_trips",
    title="Trip Category Distribution"
)

left, right = st.columns(2)

left.plotly_chart(fig1, use_container_width=True)
right.plotly_chart(fig2, use_container_width=True)

left, right = st.columns(2)

left.plotly_chart(fig3, use_container_width=True)
right.plotly_chart(fig4, use_container_width=True)