"""Data ingestion and preprocessing utilities for climate time series."""

import pandas as pd


def load_dataset(csv_path: str) -> pd.DataFrame:
    """Load climate data and ensure the index is a datetime column."""
    df = pd.read_csv(csv_path)
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df = df.set_index('date')
    return df
