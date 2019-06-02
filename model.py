# -*- coding: utf-8 -*-
"""Model definition file.

This file contains model declaration and definition. Used to get
model from other modules. As well as loading it from saved model.

Example:
    Model import is defined as follows:

        from model import get_model, saved_model, load_model

        model = get_model(model_parameters)
        ...
        save_model(model)
        ...
        loaded_model = load_model(file)

Attributes:
    get_model (keras.model): function to get parameterized model.
    save_model (None): function to save model
    load_model (keras.model): function to load model from file.

Todo:
    * Add hyperopt-compatible parametes in API

"""
from __future__ import absolute_import, division, print_function

import tensorflow as tf
from tensorflow import keras
from keras import layers, models


def get_model(model_parameters, optimizer='sgd', loss='mse', metrics=['mse', 'mae']):
    """
    Get parameterized model.

    Args:
        model_parameters (list): non empty list of tuples for each layer.
            Each layer tuple contains number of neurons and activation.
        optimizer (str): optimizer to use, default is stochastic gradient descend.
        loss (str): loss to use in optimizer, default is MSE
        metrics (list): metrics to collect, default metrics are MSE and MAE
    Returns:
        compiled model
    """

    model = keras.Sequential()

    for size, activation in model_parameters:
        model.add(layers.Dense(size, activation=activation))

    model.compile(optimizer=optimizer, loss=loss, metrics=metrics)

    return model


def load_model(file_weights, file_model=None):
    """
    Load model from given file.

    Args:
        file_weights (str): prefix to a file with weights. Expected file
            name to load is f"{file}_weights.h5".
        file_model (str): path to load model. Is used if
            model is not saved and can have different naming.
    Returns:
        keras.model loaded from file.
    """

    if file_model is None:
        file_model = file_weights

    json_file = open(f"{file_model}_model.json", 'r')
    loaded_model_json = json_file.read()
    json_file.close()

    loaded_model = models.model_from_json(loaded_model_json)
    loaded_model.load_weights(f"{file_weights}_weights.h5")


def save_model(model, file, save_model=True):
    """
    Save model to file.

    Args:
        model (str): model to save.
        file (str): file prefix to save model to.
            example: file = 123
            files created are: 123_model.json, 123_weights.h5
        save_model (bool): flag to turn off model saving. To
            prevent arbitrary model copies. Default is True.
    Returns:
        None
    """
    if save_model:
        model_json = model.to_json()

        with open(f"{file}_model.json", "w") as json_file:
            json_file.write(model_json)

    model.save_weights(f"{model}_weights.h5")

