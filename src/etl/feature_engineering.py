"""
Feature engineering for NYC Transportation Analytics.
"""

import pandas as pd

from src.logger import logger


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create analytical features.
    """

    logger.info("Creating features...")

    # -------------------------------
    # Date & Time Features
    # -------------------------------

    df["pickup_hour"] = df["pickup_datetime"].dt.hour

    df["pickup_day"] = df["pickup_datetime"].dt.day

    df["pickup_month"] = df["pickup_datetime"].dt.month

    df["pickup_weekday"] = df["pickup_datetime"].dt.day_name()

    df["is_weekend"] = (
        df["pickup_datetime"].dt.weekday >= 5
    )

    # -------------------------------
    # Rush Hour
    # -------------------------------

    df["rush_hour"] = df["pickup_hour"].between(7, 10) | \
                      df["pickup_hour"].between(16, 19)

    # -------------------------------
    # Speed
    # -------------------------------

    if "trip_distance" in df.columns:

        hours = df["trip_duration_minutes"] / 60

        df["average_speed_mph"] = (
            df["trip_distance"] / hours
        ).fillna(0)

        df["average_speed_mph"] = (
            df["average_speed_mph"]
            .replace([float("inf"), -float("inf")], 0)
        )

    # -------------------------------
    # Trip Category
    # -------------------------------

    if "trip_distance" in df.columns:

        df["trip_category"] = pd.cut(

            df["trip_distance"],

            bins=[0, 2, 10, float("inf")],

            labels=["Short", "Medium", "Long"]

        )

    logger.info("Feature engineering completed")

    return df