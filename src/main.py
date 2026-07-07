from src.etl.ingestion import get_dataset_files
from src.etl.pipeline import process_file

DATASETS = ["yellow", "green", "fhv"]

print("=" * 60)
print("NYC TRANSPORTATION ANALYTICS ETL")
print("=" * 60)

for dataset in DATASETS:

    print(f"\nProcessing {dataset.upper()}")

    files = get_dataset_files(dataset)

    for file in files:

        df = process_file(file, dataset)

        del df

print("\nCompleted successfully.")