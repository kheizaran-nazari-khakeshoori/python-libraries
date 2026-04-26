import pandas as pd
from src.climate_anomaly.data_processing import clean_dataset, aggregate_decades


def test_clean_dataset_removes_null_rows():
    df = pd.DataFrame({
        'date': ['2000-01-01', '2000-02-01', '2000-03-01'],
        'average_temperature': [15.0, None, 16.0],
    })
    df['date'] = pd.to_datetime(df['date'])
    df = df.set_index('date')
    cleaned = clean_dataset(df)
    assert cleaned['average_temperature'].notnull().all()


def test_aggregate_decades_groups_by_decade():
    df = pd.DataFrame({
        'date': ['1990-01-01', '1995-01-01', '2000-01-01'],
        'average_temperature': [14.5, 15.0, 15.5],
    })
    df['date'] = pd.to_datetime(df['date'])
    df = df.set_index('date')
    decades = aggregate_decades(df)
    assert 1990 in decades.index and 2000 in decades.index
