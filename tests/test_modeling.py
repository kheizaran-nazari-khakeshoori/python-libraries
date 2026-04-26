import numpy as np
from src.climate_anomaly.modeling import fit_linear_model, residual_sum_of_squares


def test_fit_linear_model_returns_slope_intercept():
    x = np.array([0.0, 1.0, 2.0, 3.0])
    y = np.array([1.0, 2.0, 3.0, 4.0])
    a, b = fit_linear_model(x, y)
    assert np.isclose(a, 1.0)
    assert np.isclose(b, 1.0)


def test_rss_is_zero_for_perfect_fit():
    y_true = np.array([1.0, 2.0, 3.0])
    y_pred = np.array([1.0, 2.0, 3.0])
    assert residual_sum_of_squares(y_true, y_pred) == 0.0
