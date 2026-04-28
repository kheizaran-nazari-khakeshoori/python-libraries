from src.climate_anomaly.analysis import run_analysis
from tests.conftest import sample_temperature_df


def test_run_analysis_returns_dataframe():
    df = sample_temperature_df()
    df = df.reset_index()
    df.to_csv('tests/temp_climate.csv', index=False)
    results = run_analysis('tests/temp_climate.csv')
    assert 'anomaly' in results.columns
