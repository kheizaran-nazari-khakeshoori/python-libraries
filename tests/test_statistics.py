import numpy as np
from src.climate_anomaly.statistics import t_test_against_reference, mann_kendall_test


def test_t_test_against_reference_outputs_tstat():
    values = np.array([0.1, 0.2, 0.15, 0.05])
    result = t_test_against_reference(values, reference=0.0)
    assert hasattr(result, 'statistic')


def test_mann_kendall_test_returns_summary():
    values = np.array([1.0, 2.0, 3.0, 4.0])
    result = mann_kendall_test(values)
    assert result['n'] == len(values)
