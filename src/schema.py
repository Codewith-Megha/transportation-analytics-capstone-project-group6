import pandas as pd


def inspect_schema(file_path):

    df = pd.read_parquet(file_path)

    print("=" * 80)
    print(file_path.name)
    print("=" * 80)

    print("\nRows:", len(df))
    print("Columns:", len(df.columns))

    print("\nColumn Names")

    for column in df.columns:

        print(column)

    print("\nData Types")

    print(df.dtypes)

    print("\nMissing Values")

    print(df.isnull().sum())

    print("\n")

    del df