"""Statistical tests for climate trend significance."""

import numpy as np
from scipy import stats


def t_test_against_reference(series: np.ndarray, reference: float = 0.0):
    """Perform a one-sample t-test against a reference anomaly level."""
    return stats.ttest_1samp(series, popmean=reference)
