from sqlalchemy import text
from src.database.database import engine

with engine.connect() as conn:
    version = conn.execute(text("SELECT version();"))

    print(version.fetchone()[0])

print("Database connection successful!")