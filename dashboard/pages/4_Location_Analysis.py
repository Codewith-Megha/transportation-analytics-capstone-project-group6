import streamlit as st
import plotly.express as px

from utils import load_dashboard_data
st.set_page_config(layout="wide")

st.title("📍 Location Analysis")

# -----------------------------------
# Load Cached Data
# -----------------------------------

data = load_dashboard_data()

pickup = data["pickups"].copy()
dropoff = data["dropoffs"].copy()
revenue = data["top_revenue"].copy()

# -----------------------------------
# Top Pickup Locations
# -----------------------------------

fig1 = px.bar(
    pickup,
    x="pulocationid",
    y="trips",
    title="Top 10 Pickup Locations"
)

# -----------------------------------
# Top Dropoff Locations
# -----------------------------------

fig2 = px.bar(
    dropoff,
    x="dolocationid",
    y="trips",
    title="Top 10 Dropoff Locations"
)

# -----------------------------------
# Top Revenue Locations
# -----------------------------------

fig3 = px.bar(
    revenue,
    x="pulocationid",
    y="revenue",
    title="Top Revenue Generating Pickup Locations"
)

# -----------------------------------
# Display Charts
# -----------------------------------

left, right = st.columns(2)

left.plotly_chart(fig1, use_container_width=True)
right.plotly_chart(fig2, use_container_width=True)

st.plotly_chart(fig3, use_container_width=True)