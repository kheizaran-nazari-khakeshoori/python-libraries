"""Data ingestion and preprocessing utilities for climate time series."""

import pandas as pd


def load_dataset(csv_path: str) -> pd.DataFrame:
    """Load climate data and ensure the index is a datetime column."""
    df = pd.read_csv(csv_path)
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df = df.set_index('date')
    return df

def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """Drop invalid values and fill gaps for time-series analysis."""
    df = df.dropna(subset=['average_temperature'])
    df['average_temperature'] = pd.to_numeric(df['average_temperature'], errors='coerce')
    return df.resample('M').mean().interpolate('time')


def aggregate_decades(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate data by decade to show long-term climate shifts."""
    df = df.copy()
    df['decade'] = (df.index.year // 10) * 10
    return df.groupby('decade')['average_temperature'].mean().to_frame('decade_mean')
