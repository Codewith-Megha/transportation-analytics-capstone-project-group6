import pandas as pd

RAW_FILE = "data/raw/yellow_tripdata_2026-01.parquet"
OUTPUT_FILE = "data/cleaned/yellow_tripdata_cleaned.parquet"

print("=" * 60)
print("Loading Dataset...")
print("=" * 60)

df = pd.read_parquet(RAW_FILE)

print(f"Original Rows : {len(df):,}")

# -----------------------------
# Remove duplicates
# -----------------------------
duplicates = df.duplicated().sum()
print(f"\nDuplicate Rows: {duplicates:,}")

df = df.drop_duplicates()

# -----------------------------
# Fill missing values
# -----------------------------
df["passenger_count"] = df["passenger_count"].fillna(0)

df["RatecodeID"] = df["RatecodeID"].fillna(1)

df["store_and_fwd_flag"] = df["store_and_fwd_flag"].fillna("N")

df["congestion_surcharge"] = df["congestion_surcharge"].fillna(0)

df["Airport_fee"] = df["Airport_fee"].fillna(0)

# -----------------------------
# Remove invalid trips
# -----------------------------
df = df[df["trip_distance"] > 0]

df = df[df["fare_amount"] >= 0]

df = df[df["total_amount"] >= 0]

# -----------------------------
# Create trip duration
# -----------------------------
df["trip_duration_minutes"] = (
    df["tpep_dropoff_datetime"] -
    df["tpep_pickup_datetime"]
).dt.total_seconds() / 60

# Remove negative duration
df = df[df["trip_duration_minutes"] > 0]

# -----------------------------
# Average speed
# -----------------------------
df["average_speed_mph"] = (
    df["trip_distance"] /
    (df["trip_duration_minutes"] / 60)
)

# Remove impossible speeds
df = df[df["average_speed_mph"] <= 100]

# -----------------------------
# Save cleaned dataset
# -----------------------------
df.to_parquet(OUTPUT_FILE, index=False)

print("\nCleaning Completed!")

print(f"Clean Rows : {len(df):,}")

print("\nMissing Values After Cleaning")

print(df.isnull().sum())

print("\nSaved to:")

print(OUTPUT_FILE)