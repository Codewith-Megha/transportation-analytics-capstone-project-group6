import pandas as pd
import psycopg2
from io import StringIO

# ----------------------------
# PostgreSQL Configuration
# ----------------------------
DB_NAME = "transportation_analytics"
DB_USER = "postgres"
DB_PASSWORD = "Megha123"
DB_HOST = "localhost"
DB_PORT = "5432"

# ----------------------------
# Read processed dataset
# ----------------------------
print("Loading dataset...")

df = pd.read_parquet(
    "data/processed/yellow_tripdata_features.parquet"
)

print(f"Rows Loaded: {len(df):,}")

# ----------------------------
# Connect to PostgreSQL
# ----------------------------
print("Connecting to PostgreSQL...")

conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)

cursor = conn.cursor()

# ----------------------------
# Convert dataframe to CSV in memory
# ----------------------------
print("Preparing CSV buffer...")

buffer = StringIO()

df.to_csv(
    buffer,
    index=False,
    header=False
)

buffer.seek(0)

# ----------------------------
# COPY into PostgreSQL
# ----------------------------
print("Uploading data...")

cursor.copy_expert("""
COPY taxi_trips
FROM STDIN
WITH CSV
""", buffer)

conn.commit()

cursor.close()
conn.close()

print("=" * 50)
print("UPLOAD COMPLETED SUCCESSFULLY!")
print("=" * 50)