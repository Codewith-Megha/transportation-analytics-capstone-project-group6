"""
Standardize column names across NYC Transportation datasets.
"""

COLUMN_MAPPINGS = {

    "yellow": {

        "VendorID": "vendor_id",

        "tpep_pickup_datetime": "pickup_datetime",
        "tpep_dropoff_datetime": "dropoff_datetime",

        "RatecodeID": "ratecode_id",

        "PULocationID": "pulocationid",
        "DOLocationID": "dolocationid",

        "Airport_fee": "airport_fee"

    },

    "green": {

        "VendorID": "vendor_id",

        "lpep_pickup_datetime": "pickup_datetime",
        "lpep_dropoff_datetime": "dropoff_datetime",

        "RatecodeID": "ratecode_id",

        "PULocationID": "pulocationid",
        "DOLocationID": "dolocationid"

    },

    "fhv": {

        "PUlocationID": "pulocationid",
        "DOlocationID": "dolocationid",

        "dropOff_datetime": "dropoff_datetime",
        "Affiliated_base_number": "affiliated_base_number",
    
        "SR_Flag": "sr_flag"

    }

}


def standardize_columns(df, dataset):

    mapping = COLUMN_MAPPINGS.get(dataset, {})

    df = df.rename(columns=mapping)

    return df