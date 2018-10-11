# This file sets tensorflow model to be used in analysis
import tensorflow as tf
from tensorflow import keras
import numpy as np
from data_extractor import extract


def main():
    labels, data, target = extract("soydata.csv")
    border = 200

    data = np.array(data, dtype=np.float32)
    target = np.array(target, dtype=np.float32)

    train_data, train_target = data[:border], target[:border]
    test_data, test_target = data[border:], target[border:]

    print("Extracted", len(data), "observations data with",
          len(data[0]), "features and a target column with",
          len(target), "entries")

    tf.enable_eager_execution()
    model = keras.Sequential()

    # input layer
    model.add(keras.layers.Dense(20, input_dim=4, activation=tf.nn.relu))

    model.add(keras.layers.Dense(10, activation=tf.nn.sigmoid))

    model.add(keras.layers.Dense(1, activation=tf.nn.sigmoid))

    model.compile(loss='mse',
                  optimizer=tf.train.AdamOptimizer(learning_rate=0.6),
                  metrics=['mse', 'mae'])

    print(model.summary())

    print("Training")

    results = model.fit(
        train_data, train_target,
        epochs = 5
    )

    print("Training done")
    print("Testing on test data: ")

    loss, mse, mae = model.evaluate(test_data, test_target)

    print("MSE - ", mse)
    print("MAE - ", mae)


if __name__ == "__main__":
    main()
