"""Entry point for climate anomaly analysis workflows."""

import argparse
from src.climate_anomaly.data_processing import load_dataset, clean_dataset
from src.climate_anomaly.signal_processing import remove_seasonal_noise
from src.climate_anomaly.visualization import plot_raw_data, plot_smoothed_trend, plot_anomaly_distribution


def parse_args():
    parser = argparse.ArgumentParser(description='Run climate anomaly analysis.')
    parser.add_argument('--data', required=True, help='Path to the climate dataset CSV file.')
    parser.add_argument('--output', default='output', help='Directory for saving results.')
    return parser.parse_args()


def main():
    args = parse_args()
    df = load_dataset(args.data)
    df = clean_dataset(df)
    df = remove_seasonal_noise(df)
    plot_raw_data(df).savefig(f'{args.output}/raw_data.png')
    plot_smoothed_trend(df).savefig(f'{args.output}/smoothed_trend.png')
    plot_anomaly_distribution(df).savefig(f'{args.output}/anomaly_distribution.png')


if __name__ == '__main__':
    main()
