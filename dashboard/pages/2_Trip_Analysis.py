import streamlit as st
import plotly.express as px

from utils import load_dashboard_data
st.set_page_config(layout="wide")

st.title("🚖 Trip Analysis")

# -----------------------------
# Load Cached Data
# -----------------------------

data = load_dashboard_data()

monthly = data["monthly_trips"].copy()
hourly = data["hourly_trips"].copy()
weekday = data["weekday_trips"].copy()
category = data["trip_category"].copy()

# -----------------------------
# Monthly Trips
# -----------------------------

fig1 = px.bar(
    monthly,
    x="pickup_month",
    y="total_trips",
    title="Monthly Trips"
)

# -----------------------------
# Trips by Hour
# -----------------------------

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

fig3 = px.bar(
    weekday,
    x="pickup_weekday",
    y="total_trips",
    title="Trips by Weekday"
)

# -----------------------------
# Trip Category
# -----------------------------

fig4 = px.pie(
    category,
    names="trip_category",
    values="total_trips",
    title="Trip Category Distribution"
)

# -----------------------------
# Display Charts
# -----------------------------

left, right = st.columns(2)

left.plotly_chart(fig1, use_container_width=True)
right.plotly_chart(fig2, use_container_width=True)

left, right = st.columns(2)

left.plotly_chart(fig3, use_container_width=True)
right.plotly_chart(fig4, use_container_width=True)