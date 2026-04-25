"""Statistical tests for climate trend significance."""

import numpy as np
from scipy import stats


def t_test_against_reference(series: np.ndarray, reference: float = 0.0):
    """Perform a one-sample t-test against a reference anomaly level."""
    return stats.ttest_1samp(series, popmean=reference)

def mann_kendall_test(series: np.ndarray):
    """Perform a simple Mann-Kendall trend test on the series."""
    n = len(series)
    s = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            s += np.sign(series[j] - series[i])
    var_s = (n * (n - 1) * (2 * n + 5)) / 18
    z = (s - np.sign(s)) / np.sqrt(var_s) if s != 0 else 0
    return {'S': s, 'z': z, 'n': n}
