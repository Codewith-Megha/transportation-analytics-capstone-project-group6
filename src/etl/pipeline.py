import pandas as pd

from src.database.load import load_dataframe
from src.etl.standardize import standardize_columns
from src.etl.cleaning import clean_dataset
from src.etl.feature_engineering import engineer_features
from src.etl.validation import validate_dataframe
from src.logger import logger

def process_file(file_path, dataset):

    logger.info(f"Reading {file_path.name}")

    df = pd.read_parquet(file_path)

    logger.info(f"Rows: {len(df):,}")

    df = standardize_columns(df, dataset)

    logger.info("Columns standardized")

    df = clean_dataset(df, dataset)

    df = engineer_features(df)

    df["dataset"] = dataset

    validate_dataframe(df)

    load_dataframe(df, dataset)



    return df