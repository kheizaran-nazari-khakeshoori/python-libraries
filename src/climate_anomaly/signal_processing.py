"""Signal processing utilities for smoothing climate data."""

import numpy as np
from scipy.signal import butter, filtfilt


def butterworth_filter(signal: np.ndarray, cutoff: float = 0.1, order: int = 2) -> np.ndarray:
    """Apply a low-pass Butterworth filter to remove short-term noise."""
    b, a = butter(order, cutoff, btype='low', analog=False)
    return filtfilt(b, a, signal)
