"""
Validation module for ETL pipeline.
"""

import pandas as pd

from src.logger import logger


REQUIRED_COLUMNS = [
    "pickup_datetime",
    "dropoff_datetime",
    "trip_duration_minutes",
    "pickup_hour",
    "pickup_day",
    "pickup_month",
    "pickup_weekday",
    "is_weekend",
    "rush_hour"
]


def validate_dataframe(df: pd.DataFrame):

    logger.info("Validating dataframe...")

    # Required columns
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]

    if missing:
        raise ValueError(
            f"Missing required columns: {missing}"
        )

    # Negative duration
    if (df["trip_duration_minutes"] < 0).any():
        raise ValueError(
            "Negative trip duration detected."
        )

    # Missing pickup datetime
    if df["pickup_datetime"].isna().any():
        raise ValueError(
            "pickup_datetime contains NULL values."
        )

    logger.info("Validation successful.")