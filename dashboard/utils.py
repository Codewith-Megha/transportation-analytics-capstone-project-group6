import pandas as pd
from src.database.database import engine
from src.analytics import queries


def run_query(query):
    """
    Execute SQL query and return DataFrame.
    """
    return pd.read_sql(query, engine)