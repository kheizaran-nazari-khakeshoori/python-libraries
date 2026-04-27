import pandas as pd


def sample_temperature_df():
    df = pd.DataFrame({
        'date': pd.date_range('2021-01-01', periods=4, freq='M'),
        'average_temperature': [10.0, 11.0, 10.5, 11.2],
    })
    df = df.set_index('date')
    return df
