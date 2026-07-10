import streamlit as st
import plotly.express as px

from utils import run_query
from src.analytics import queries

st.set_page_config(layout="wide")

st.title("📍 Location Analysis")

# -----------------------------------
# Top Pickup Locations
# -----------------------------------

pickup = run_query(queries.TOP_PICKUPS)

fig1 = px.bar(
    pickup,
    x="pulocationid",
    y="trips",
    title="Top 10 Pickup Locations"
)

# -----------------------------------
# Top Dropoff Locations
# -----------------------------------

dropoff = run_query(queries.TOP_DROPOFFS)

fig2 = px.bar(
    dropoff,
    x="dolocationid",
    y="trips",
    title="Top 10 Dropoff Locations"
)

# -----------------------------------
# Top Revenue Locations
# -----------------------------------

revenue = run_query(queries.TOP_REVENUE_LOCATIONS)

fig3 = px.bar(
    revenue,
    x="pulocationid",
    y="revenue",
    title="Top Revenue Generating Pickup Locations"
)

left, right = st.columns(2)

left.plotly_chart(fig1, use_container_width=True)

right.plotly_chart(fig2, use_container_width=True)

st.plotly_chart(fig3, use_container_width=True)