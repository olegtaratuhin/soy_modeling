"""Model wrapper file.

This file contains definition of model wrapper. Arguments
are configured externally.

Usage:
    python3 model_wrapper.py --mode fit --target protein --data data.hd5
"""

import argparse
import pandas as pd
import numpy as np
import keras
import tensorflow as tf


def train_on_dataset(data, target):
    model = keras.Sequential()
    model.add(keras.layers.Dense(
        20, input_dim=data.shape[1], activation=tf.nn.sigmoid))
    model.add(keras.layers.Dropout(0.5))
    model.add(keras.layers.Dense(5, activation='sigmoid'))
    model.add(keras.layers.Dense(1, activation='sigmoid'))

    sgd = optimizers.SGD(lr=0.035)

    model.compile(loss='mse',
                  optimizer=sgd,
                  metrics=['mse', 'mae'])

    model.fit(data, target, epochs=200, batch_size=30,
              validation_split=0.2, verbose=0)

    return model


def evaluate(data, result):
    expected_ends = data.loc[np.logical_and(
        data['state'] > 0.59, data['state'] < 0.61)]
    actual_ends = result.loc[np.logical_and(
        expected['state'] > 0.59, expected['state'] < 0.61)]

    pass


target_names_map = {
    "crop": "state",
    "bloom": "state",
    #    "oil": "",
    #    "protein": ""
}


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

    last3_columns = data.columns[-3:0]
    filtered_columns = ['I1', 'I2', 'I3', 'I4',
                        'd', 'state', 'event_day', 'gr_names']
    filtered_columns.extend(last3_columns)

    filtered_data = data[filtered_columns]

    filtered_data_with_categorical = pd.get_dummies(
        filtered_data, columns=["gr_name"])

    for target_name in config.target:
        target_data = filtered_data_with_categorical[target_names_map[target_name]].values.ravel(
        )
        train_data = filtered_data_with_categorical.drop[[
            target_names_map[target_name]]].values

        model = train_on_dataset(train_data, target_data)

        predicted = model.predict(train_data)

        error = evaluate(data['event_day'], predicted)
        print(error)
