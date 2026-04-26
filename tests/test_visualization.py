import pandas as pd
from src.climate_anomaly.visualization import plot_raw_data, plot_smoothed_trend, plot_anomaly_distribution


def test_plot_raw_data_returns_figure():
    df = pd.DataFrame({'date': pd.date_range('2020-01-01', periods=3), 'average_temperature': [12, 13, 14]})
    df = df.set_index('date')
    fig = plot_raw_data(df)
    assert fig is not None


def test_plot_anomaly_distribution_returns_figure():
    df = pd.DataFrame({'average_temperature': [12, 13, 14, 13, 12]})
    fig = plot_anomaly_distribution(df)
    assert fig is not None
