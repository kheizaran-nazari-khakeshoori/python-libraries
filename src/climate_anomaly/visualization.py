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

def plot_smoothed_trend(df, field='average_temperature_smoothed'):
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(df.index, df[field], color='orange', label='Smoothed Trend')
    ax.set_title('Smoothed Climate Trend')
    ax.set_xlabel('Date')
    ax.set_ylabel('Temperature')
    ax.legend()
    return fig


def plot_anomaly_distribution(df, field='average_temperature'):
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.hist(df[field].dropna(), bins=30, color='skyblue')
    ax.set_title('Distribution of Temperature Anomalies')
    ax.set_xlabel('Temperature')
    ax.set_ylabel('Frequency')
    return fig

def plot_comparison_dashboard(df, raw_field='average_temperature', smooth_field='average_temperature_smoothed'):
    fig, axes = plt.subplots(3, 1, figsize=(10, 12), sharex=True)
    axes[0].plot(df.index, df[raw_field], label='Raw Data', color='blue')
    axes[0].set_title('Raw Temperature Data')
    axes[1].plot(df.index, df[smooth_field], label='Smoothed Trend', color='orange')
    axes[1].set_title('Smoothed Trend')
    axes[2].hist(df[raw_field].dropna(), bins=30, color='skyblue')
    axes[2].set_title('Anomaly Distribution')
    for ax in axes:
        ax.legend()
    fig.tight_layout()
    return fig
