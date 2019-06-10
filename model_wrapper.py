"""Model wrapper file.

This file contains definition of model wrapper. Arguments
are configured externally.

Usage:
    python3 model_wrapper.py --mode fit --target protein --data data.hd5
"""

import argparse
import pandas as pd
import keras


def train_on_dataset(data, target):


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Simple command line wrapper on model training.")

    parser.add_argument('--mode',
        metavar='-M',
        choices=['fit', 'predict'],
        nargs=1,
        required=True,
        help="""Mode selector, to train a model pass 'fit', to use existing model pass 'predict'""")

    parser.add_argument('--target',
        metavar='-T',
        choices=['crop', 'bloom', 'protein', 'oil'],
        nargs='+',
        required=True,
        help="""Target specifier, if more than one is specified result is calculated for each separately""")

    parser.add_argument('--data',
        metavar='-D',
        nargs=1,
        required=True,
        help="""Path to file with dataset. Csv and hd5 are supported""")

    config = parser.parse_args()
    path_to_data = str(config.data)
    data = None

    if path_to_data.endswith('.csv'):
        data = pd.read_csv(path_to_data)
    else:
        data = pd.read_hdf(path_to_data, mode='r')

    filtered_columns = ['I1', 'I2', 'I3', 'I4', 'state', 'event_day']
    filtered_data = data[filtered_columns]

    for target in config.target:
        pass

        error = 0
        print(error)
