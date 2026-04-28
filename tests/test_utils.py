import pandas as pd
from src.climate_anomaly.utils import ensure_datetime_index, compute_anomalies


def test_ensure_datetime_index_sets_index():
    df = pd.DataFrame({'date': ['2020-01-01'], 'average_temperature': [12.0]})
    result = ensure_datetime_index(df)
    assert result.index.name == 'date'


def test_compute_anomalies_creates_anomaly_column():
    df = pd.DataFrame({'average_temperature': [10.0, 12.0, 14.0]})
    result = compute_anomalies(df)
    assert 'anomaly' in result.columns
