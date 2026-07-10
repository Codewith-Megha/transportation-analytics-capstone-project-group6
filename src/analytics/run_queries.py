"""
Execute SQL analytics queries.
"""

import pandas as pd

from src.database.database import engine
from src.analytics import queries


def run_query(sql):
    """
    Execute a SQL query and return a DataFrame.
    """
    return pd.read_sql(sql, engine)


QUERY_LIST = {

    # ==========================
    # KPI Queries
    # ==========================

    "Total Trips": queries.TOTAL_TRIPS,
    "Total Revenue": queries.TOTAL_REVENUE,
    "Average Fare": queries.AVERAGE_FARE_OVERALL,
    "Average Trip Distance": queries.AVERAGE_TRIP_DISTANCE,
    "Average Trip Duration": queries.AVERAGE_TRIP_DURATION,

    # ==========================
    # Trip Analysis
    # ==========================

    "Monthly Trips": queries.MONTHLY_TRIPS,
    "Trips by Weekday": queries.WEEKDAY_TRIPS,
    "Trips by Hour": queries.HOURLY_TRIPS,
    "Weekend Analysis": queries.WEEKEND_ANALYSIS,
    "Rush Hour": queries.RUSH_HOUR,
    "Passenger Count Distribution": queries.PASSENGER_COUNT_DISTRIBUTION,
    "Trip Category": queries.TRIP_CATEGORY,

    # ==========================
    # Revenue Analysis
    # ==========================

    "Monthly Revenue": queries.MONTHLY_REVENUE,
    "Revenue by Hour": queries.REVENUE_BY_HOUR,
    "Average Fare by Month": queries.AVERAGE_FARE,

    # ==========================
    # Speed & Distance
    # ==========================

    "Average Distance by Month": queries.AVERAGE_DISTANCE,
    "Average Duration by Month": queries.AVERAGE_DURATION,
    "Hourly Average Speed": queries.HOURLY_AVERAGE_SPEED,
    "Monthly Average Speed": queries.MONTHLY_AVERAGE_SPEED,

    # ==========================
    # Location Analysis
    # ==========================

    "Top Pickup Locations": queries.TOP_PICKUPS,
    "Top Dropoff Locations": queries.TOP_DROPOFFS,
    "Top Revenue Locations": queries.TOP_REVENUE_LOCATIONS,

    # ==========================
    # Dataset Analysis
    # ==========================

    "Green Taxi Monthly Trips": queries.GREEN_MONTHLY_TRIPS,
    "FHV Monthly Trips": queries.FHV_MONTHLY_TRIPS,
    "Payment Types": queries.PAYMENT_TYPES,
    "Dataset Comparison": queries.DATASET_COMPARISON
}


if __name__ == "__main__":

    for title, sql in QUERY_LIST.items():

        print("\n" + "=" * 70)
        print(title)
        print("=" * 70)

        try:
            df = run_query(sql)
            print(df)

        except Exception as e:
            print(f"Error: {e}")