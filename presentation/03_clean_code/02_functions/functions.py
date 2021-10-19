import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame

##  EXAMPLE 1 =========================================================================
file_name = "my_data.csv"
with open(file_name, "r") as file_handle:
    df = pd.read_csv(file_handle)

# We have some missing values to clean
df = df.replace(to_replace="missing", value=np.NaN)
df.dropna()

df["cumsum"] = df["sales"].cumsum()

export_filename = "exported_data.csv"
with open(export_filename, "w") as file:
    df.to_csv(file)


##  EXAMPLE 2 =========================================================================
def main():
    file_name = "my_data.csv"
    export_filename = "exported_data.csv"

    df = import_data(file_name)
    df = clean_data_from_missing_values(df)
    df = calculate_salery_statistics(df)
    export_results(df, export_filename)


def import_data(file_name: str) -> pd.DataFrame:
    with open(file_name, "r") as file_handle:
        return pd.read_csv(file_handle)


def clean_data_from_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    df = df.replace(to_replace="missing", value=np.NaN)
    df = df.dropna()
    return df


def calculate_salery_statistics(df: pd.DataFrame) -> pd.DataFrame:
    df["cumsum"] = df["sales"].cumsum()
    return df


def export_results(df: pd.DataFrame, file_name: str) -> None:
    with open(file_name, "w") as file:
        df.to_csv(file)


if __name__ == "__main__":
    main()

##  EXAMPLE 3 =========================================================================
def main():
    file_name = "my_data.csv"
    export_filename = "exported_data.csv"

    df = import_data(file_name)
    # We have some missing values to clean
    df = df.replace(to_replace="missing", value=np.NaN)
    df.dropna()
    df = calculate_salery_statistics(df)
    export_results(df, export_filename)
