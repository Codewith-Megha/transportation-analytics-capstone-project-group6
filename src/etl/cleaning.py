from src.logger import logger
"""
Generic cleaning functions for NYC Transportation Analytics.
Supports:
- Yellow Taxi
- Green Taxi
- FHV
"""

import pandas as pd


def clean_dataset(df: pd.DataFrame, dataset: str) -> pd.DataFrame:
    """
    Cleans one dataframe based on dataset type.

    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe.

    dataset : str
        yellow | green | fhv

    Returns
    -------
    pd.DataFrame
        Cleaned dataframe.
    """

    logger.info(f"Cleaning {dataset.upper()} dataset")

    original_rows = len(df)

    # ---------------------------------------------------
    # Remove duplicate rows
    # ---------------------------------------------------
    df = df.drop_duplicates()

    # ---------------------------------------------------
    # Remove invalid timestamps
    # ---------------------------------------------------
    if "pickup_datetime" in df.columns and "dropoff_datetime" in df.columns:

        df = df[
            df["pickup_datetime"] <= df["dropoff_datetime"]
        ]

        df["trip_duration_minutes"] = (
            df["dropoff_datetime"] -
            df["pickup_datetime"]
        ).dt.total_seconds() / 60

        df = df[df["trip_duration_minutes"] > 0]

    # ---------------------------------------------------
    # Yellow Taxi Cleaning
    # ---------------------------------------------------
    if dataset == "yellow":

        if "passenger_count" in df.columns:
            df["passenger_count"] = df["passenger_count"].fillna(1)

        df["RatecodeID"] = df["RatecodeID"].fillna(1)

        df["store_and_fwd_flag"] = (
            df["store_and_fwd_flag"]
            .fillna("N")
        )

        df["congestion_surcharge"] = (
            df["congestion_surcharge"]
            .fillna(0)
        )

        df["Airport_fee"] = (
            df["Airport_fee"]
            .fillna(0)
        )

    # ---------------------------------------------------
    # Green Taxi Cleaning
    # ---------------------------------------------------
    elif dataset == "green":

        df["passenger_count"] = df["passenger_count"].fillna(1)

        df["RatecodeID"] = df["RatecodeID"].fillna(1)

        df["store_and_fwd_flag"] = (
            df["store_and_fwd_flag"]
            .fillna("N")
        )

        df["payment_type"] = (
            df["payment_type"]
            .fillna(0)
        )

        df["trip_type"] = (
            df["trip_type"]
            .fillna(0)
        )

        df["congestion_surcharge"] = (
            df["congestion_surcharge"]
            .fillna(0)
        )

        # Entire column is null
        if "ehail_fee" in df.columns:
            df["ehail_fee"] = df["ehail_fee"].fillna(0)

    # ---------------------------------------------------
    # FHV Cleaning
    # ---------------------------------------------------
    elif dataset == "fhv":

        # Remove rows where BOTH locations are missing
        df = df.dropna(
            subset=["PULocationID", "DOLocationID"],
            how="all"
        )

        df["Affiliated_base_number"] = (
            df["Affiliated_base_number"]
            .fillna("Unknown")
        )

    # ---------------------------------------------------
    # Summary
    # ---------------------------------------------------
    logger.info(f"Original Rows: {original_rows:,}")
    logger.info(f"Clean Rows: {len(df):,}")

    logger.info("Cleaning completed")

    return df