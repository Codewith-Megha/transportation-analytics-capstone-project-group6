from config.config import RAW_DATA

DATASETS = {
    "yellow": sorted(RAW_DATA.glob("yellow_tripdata_2026-*.parquet")),
    "green": sorted(RAW_DATA.glob("green_tripdata_2026-*.parquet")),
    "fhv": sorted(RAW_DATA.glob("fhv_tripdata_2026-*.parquet"))
}


def get_dataset_files(dataset_name):
    files = DATASETS.get(dataset_name)

    if files is None:
        raise ValueError(f"Dataset '{dataset_name}' not found.")

    return files