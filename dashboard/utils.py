import streamlit as st
import pandas as pd

from src.database.database import engine
from src.analytics import queries


@st.cache_data(ttl=3600, show_spinner=False)
def run_query(query):
    """
    Execute SQL query and cache the result for 1 hour.
    """
    return pd.read_sql(query, engine)


@st.cache_data(ttl=3600, show_spinner=True)
def load_dashboard_data():
    """
    Load all dashboard datasets once and cache them.
    """

    return {

        # ==========================
        # KPI DATA
        # ==========================

        "total_trips": run_query(queries.TOTAL_TRIPS),
        "total_revenue": run_query(queries.TOTAL_REVENUE),
        "avg_fare": run_query(queries.AVERAGE_FARE_OVERALL),
        "avg_trip_distance": run_query(queries.AVERAGE_TRIP_DISTANCE),
        "avg_trip_duration": run_query(queries.AVERAGE_TRIP_DURATION),

        # ==========================
        # TRIP ANALYSIS
        # ==========================

        "monthly_trips": run_query(queries.MONTHLY_TRIPS),
        "weekday_trips": run_query(queries.WEEKDAY_TRIPS),
        "hourly_trips": run_query(queries.HOURLY_TRIPS),
        "weekend": run_query(queries.WEEKEND_ANALYSIS),
        "rush_hour": run_query(queries.RUSH_HOUR),
        "trip_category": run_query(queries.TRIP_CATEGORY),

        # ==========================
        # REVENUE ANALYSIS
        # ==========================

        "monthly_revenue": run_query(queries.MONTHLY_REVENUE),
        "revenue_by_hour": run_query(queries.REVENUE_BY_HOUR),
        "average_fare": run_query(queries.AVERAGE_FARE),
        "average_distance": run_query(queries.AVERAGE_DISTANCE),
        "average_duration": run_query(queries.AVERAGE_DURATION),
        "monthly_average_speed": run_query(queries.MONTHLY_AVERAGE_SPEED),

        # ==========================
        # LOCATION ANALYSIS
        # ==========================

        "pickups": run_query(queries.TOP_PICKUPS),
        "dropoffs": run_query(queries.TOP_DROPOFFS),
        "top_revenue": run_query(queries.TOP_REVENUE_LOCATIONS),

        # ==========================
        # DATASET COMPARISON
        # ==========================

        "dataset_comparison": run_query(queries.DATASET_COMPARISON),
        "green": run_query(queries.GREEN_MONTHLY_TRIPS),
        "fhv": run_query(queries.FHV_MONTHLY_TRIPS),

        # ==========================
        # OTHER ANALYSIS
        # ==========================

        "payment_types": run_query(queries.PAYMENT_TYPES),
    }