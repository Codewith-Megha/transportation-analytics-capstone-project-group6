from pathlib import Path

# Project root

BASE_DIR = Path(__file__).resolve().parent.parent

# Data folders

RAW_DATA = BASE_DIR / "data" / "raw"

CLEAN_DATA = BASE_DIR / "data" / "cleaned"

PROCESSED_DATA = BASE_DIR / "data" / "processed"

EXPORT_DATA = BASE_DIR / "data" / "exports"

# PostgreSQL

# PostgreSQL
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "transportation_analytics"
DB_USER = "postgres"
DB_PASSWORD = "YOUR_PASSWORD"
EXPORT_DATA = BASE_DIR / "data" / "exports"
