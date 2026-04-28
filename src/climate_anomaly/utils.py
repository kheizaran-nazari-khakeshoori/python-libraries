"""Utility helpers for climate anomaly workflows."""

import pandas as pd


def ensure_datetime_index(df: pd.DataFrame, date_column: str = 'date') -> pd.DataFrame:
    df = df.copy()
    if date_column in df.columns:
        df[date_column] = pd.to_datetime(df[date_column], errors='coerce')
        df = df.set_index(date_column)
    return df


def compute_anomalies(df: pd.DataFrame, baseline: float = None) -> pd.DataFrame:
    if baseline is None:
        baseline = df['average_temperature'].mean()
    df = df.copy()
    df['anomaly'] = df['average_temperature'] - baseline
    return df
