import pandas as pd

INPUT_FILE = "data/cleaned/yellow_tripdata_cleaned.parquet"
OUTPUT_FILE = "data/processed/yellow_tripdata_features.parquet"

print("=" * 60)
print("Feature Engineering")
print("=" * 60)

df = pd.read_parquet(INPUT_FILE)

# -----------------------
# Time Features
# -----------------------
df["pickup_hour"] = df["tpep_pickup_datetime"].dt.hour
df["pickup_day"] = df["tpep_pickup_datetime"].dt.day
df["pickup_month"] = df["tpep_pickup_datetime"].dt.month
df["pickup_weekday"] = df["tpep_pickup_datetime"].dt.day_name()

# -----------------------
# Weekend
# -----------------------
df["is_weekend"] = df["pickup_weekday"].isin(
    ["Saturday", "Sunday"]
)

# -----------------------
# Rush Hour
# -----------------------
df["rush_hour"] = df["pickup_hour"].isin(
    [7, 8, 9, 16, 17, 18]
)

# -----------------------
# Trip Category
# -----------------------
def classify_trip(distance):
    if distance < 2:
        return "Short"
    elif distance < 10:
        return "Medium"
    else:
        return "Long"

df["trip_category"] = df["trip_distance"].apply(classify_trip)

# -----------------------
# Save
# -----------------------
df.to_parquet(OUTPUT_FILE, index=False)

print("\nFeature engineering completed!")

print("\nColumns Created:")
print([
    "pickup_hour",
    "pickup_day",
    "pickup_month",
    "pickup_weekday",
    "is_weekend",
    "rush_hour",
    "trip_category"
])

print(f"\nRows : {len(df):,}")

print(f"Saved to:\n{OUTPUT_FILE}")