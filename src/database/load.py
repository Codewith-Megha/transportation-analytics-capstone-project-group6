import pandas as pd
from sqlalchemy.exc import SQLAlchemyError
from src.database.database import engine
from src.database.schema import (
    YELLOW_COLUMNS,
    GREEN_COLUMNS,
    FHV_COLUMNS
)

TABLE_MAPPING = {
    "yellow": "yellow_trips",
    "green": "green_trips",
    "fhv": "fhv_trips"
}

COLUMN_MAPPING = {
    "yellow": YELLOW_COLUMNS,
    "green": GREEN_COLUMNS,
    "fhv": FHV_COLUMNS
}


def load_dataframe(df: pd.DataFrame, dataset: str):

    table_name = TABLE_MAPPING[dataset]

    # Keep only required columns
    df = df[COLUMN_MAPPING[dataset]]

    print(f"Loading {len(df):,} rows into {table_name}...")

    from sqlalchemy.exc import SQLAlchemyError



    df.to_sql(
    table_name,
    engine,
    if_exists="append",
    index=False,
    chunksize=50000,
    method="multi"
    )

print("Load completed.")

    