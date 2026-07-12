import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
import streamlit as st

from dashboard.utils import load_dashboard_data
st.set_page_config(
    page_title="NYC Transportation Analytics",
    page_icon="🚖",
    layout="wide"
)

st.title("🚖 NYC Transportation Analytics Dashboard")

with st.spinner("Loading dashboard..."):
    load_dashboard_data()

st.markdown("""
### Welcome

This dashboard provides insights into the NYC Taxi datasets.

Use the navigation menu on the left to explore:

- 📊 Overview
- 🚖 Trip Analysis
- 💰 Revenue Analysis
- 📍 Location Analysis
- 🚕 Dataset Comparison
""")