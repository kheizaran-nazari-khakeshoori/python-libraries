# Global Climate Anomaly & Predictive Trend Analysis

A Python package for detecting climate anomalies and modeling long-term temperature trends using scientific computation.

This project is designed for real-world weather analysis, not simple tutorial data. It combines data ingestion, signal cleaning, statistical validation, modeling, and visualization.

## Why this project works

- Uses `pandas` for time-series cleaning, indexing, and aggregation.
- Uses `numpy` for vectorized anomaly detection and rolling statistics.
- Uses `scipy` for noise reduction and statistical validation.
- Uses `matplotlib` for multi-panel dashboards and trend visualizations.

## Project structure

- `src/climate_anomaly/`: package modules for ingestion, filtering, statistics, modeling, and plotting.
- `run_analysis.py`: analysis entrypoint for running the full workflow.
- `requirements.txt`: scientific Python dependencies.
- `tests/`: lightweight unit tests for core functions.

## Mathematical context

The analysis uses statistical formulas such as standard deviation:

$$\sigma = \sqrt{\frac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^2}$$

This makes the methodology clear for recruiters and reviewers.
