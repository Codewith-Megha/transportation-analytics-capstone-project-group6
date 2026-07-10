import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))
sys.path.append(str(Path(__file__).parent.parent))
import streamlit as st

st.set_page_config(
    page_title="NYC Transportation Analytics",
    page_icon="🚖",
    layout="wide"
)

st.title("🚖 NYC Transportation Analytics Dashboard")

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