"""Mathematical modeling for climate trend prediction."""

import numpy as np


def fit_linear_model(x: np.ndarray, y: np.ndarray):
    """Fit a linear model y = a*x + b using least squares."""
    a, b = np.polyfit(x, y, deg=1)
    return a, b


def residual_sum_of_squares(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Compute the RSS metric for model quality."""
    return np.sum((y_true - y_pred) ** 2)
