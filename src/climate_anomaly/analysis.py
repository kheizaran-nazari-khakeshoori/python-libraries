"""High-level workflow orchestration for climate anomaly analysis."""

from .data_processing import load_dataset, clean_dataset
from .signal_processing import remove_seasonal_noise
from .utils import compute_anomalies


def run_analysis(csv_path: str):
    df = load_dataset(csv_path)
    df = clean_dataset(df)
    df = remove_seasonal_noise(df)
    return compute_anomalies(df)
