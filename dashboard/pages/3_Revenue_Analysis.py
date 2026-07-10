import streamlit as st
import plotly.express as px

from utils import run_query
from src.analytics import queries

st.set_page_config(layout="wide")

st.title("💰 Revenue Analysis")

# ----------------------------------
# Monthly Revenue
# ----------------------------------

monthly_revenue = run_query(queries.MONTHLY_REVENUE)

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

hourly_revenue = run_query(queries.REVENUE_BY_HOUR)

fig2 = px.bar(
    hourly_revenue,
    x="pickup_hour",
    y="revenue",
    title="Revenue by Hour"
)

# ----------------------------------
# Average Fare
# ----------------------------------

avg_fare = run_query(queries.AVERAGE_FARE)

fig3 = px.bar(
    avg_fare,
    x="pickup_month",
    y="average_fare",
    title="Average Fare by Month"
)

# ----------------------------------
# Monthly Average Speed
# ----------------------------------

avg_speed = run_query(queries.MONTHLY_AVERAGE_SPEED)

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