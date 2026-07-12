import streamlit as st
import plotly.express as px

from utils import load_dashboard_data
st.set_page_config(layout="wide")

st.title("💰 Revenue Analysis")

# ----------------------------------
# Load Cached Data
# ----------------------------------

data = load_dashboard_data()

monthly_revenue = data["monthly_revenue"].copy()
hourly_revenue = data["revenue_by_hour"].copy()
avg_fare = data["average_fare"].copy()
avg_speed = data["monthly_average_speed"].copy()

# ----------------------------------
# Monthly Revenue
# ----------------------------------

fig1 = px.line(
    monthly_revenue,
    x="pickup_month",
    y="revenue",
    markers=True,
    title="Monthly Revenue"
)

# ----------------------------------
# Revenue by Hour
# ----------------------------------

fig2 = px.bar(
    hourly_revenue,
    x="pickup_hour",
    y="revenue",
    title="Revenue by Hour"
)

# ----------------------------------
# Average Fare
# ----------------------------------

fig3 = px.bar(
    avg_fare,
    x="pickup_month",
    y="average_fare",
    title="Average Fare by Month"
)

# ----------------------------------
# Monthly Average Speed
# ----------------------------------

fig4 = px.line(
    avg_speed,
    x="pickup_month",
    y="average_speed",
    markers=True,
    title="Average Speed by Month"
)

left, right = st.columns(2)

left.plotly_chart(fig1, use_container_width=True)
right.plotly_chart(fig2, use_container_width=True)

left, right = st.columns(2)

left.plotly_chart(fig3, use_container_width=True)
right.plotly_chart(fig4, use_container_width=True)