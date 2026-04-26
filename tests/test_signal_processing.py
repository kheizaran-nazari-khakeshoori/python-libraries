import numpy as np
from src.climate_anomaly.signal_processing import butterworth_filter


def test_butterworth_filter_smooths_noise():
    signal = np.array([0.0, 1.0, 0.5, 1.5, 0.2, 1.0, 0.8])
    filtered = butterworth_filter(signal, cutoff=0.3, order=2)
    assert filtered.shape == signal.shape
    assert np.all(np.isfinite(filtered))
