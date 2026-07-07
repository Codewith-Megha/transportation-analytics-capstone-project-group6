"""
Standardize column names across NYC transportation datasets.
"""

COLUMN_MAPPINGS = {

    "yellow": {
        "tpep_pickup_datetime": "pickup_datetime",
        "tpep_dropoff_datetime": "dropoff_datetime"
    },

    "green": {
        "lpep_pickup_datetime": "pickup_datetime",
        "lpep_dropoff_datetime": "dropoff_datetime"
    },

    "fhv": {
        "dropOff_datetime": "dropoff_datetime",
        "PUlocationID": "PULocationID",
        "DOlocationID": "DOLocationID"
    }

}


def standardize_columns(df, dataset):

    mapping = COLUMN_MAPPINGS.get(dataset, {})

    df = df.rename(columns=mapping)

    return df