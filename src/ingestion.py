import pandas as pd

FILE_PATH = "data/raw/yellow_tripdata_2026-01.parquet"

# Load dataset
df = pd.read_parquet(FILE_PATH)

print("=" * 60)
print("Dataset Information")
print("=" * 60)

print(f"\nRows: {df.shape[0]:,}")
print(f"Columns: {df.shape[1]}")

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nStatistical Summary:")
print(df.describe())

print("\nFirst 5 Records:")
print(df.head())