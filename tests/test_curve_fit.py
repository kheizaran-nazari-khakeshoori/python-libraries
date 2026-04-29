import numpy as np
from src.climate_anomaly.modeling import fit_exponential_model


def test_fit_exponential_model_returns_three_parameters():
    x = np.linspace(0, 3, 4)
    y = np.exp(x)
    params = fit_exponential_model(x, y)
    assert len(params) == 3
