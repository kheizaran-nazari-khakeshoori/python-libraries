"""Visualization helpers for climate anomaly dashboards."""

import matplotlib.pyplot as plt


def plot_raw_data(df, field='average_temperature'):
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(df.index, df[field], label='Raw Temperature')
    ax.set_title('Raw Temperature Time Series')
    ax.set_xlabel('Date')
    ax.set_ylabel('Temperature')
    ax.legend()
    return fig
