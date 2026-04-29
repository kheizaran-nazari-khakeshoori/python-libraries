"""Mathematical modeling for climate trend prediction."""

import numpy as np


def fit_linear_model(x: np.ndarray, y: np.ndarray):
    """Fit a linear model y = a*x + b using least squares."""
    a, b = np.polyfit(x, y, deg=1)
    return a, b


def residual_sum_of_squares(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Compute the RSS metric for model quality."""
    return np.sum((y_true - y_pred) ** 2)

from scipy.optimize import curve_fit


def exponential_uv(x, a, b, c):
    return a * np.exp(b * x) + c


def fit_exponential_model(x: np.ndarray, y: np.ndarray):
    """Fit an exponential curve to capture accelerating temperature changes."""
    popt, _ = curve_fit(exponential_uv, x, y, p0=(1.0, 0.01, 0.0), maxfev=10000)
    return popt
