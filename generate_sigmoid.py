# Thif file generated sigmoid function for mapping state
import numpy as np


def sigmoid_skew(x, scale=1.0, transpose=5.0):
    """
    Calculates sigmoid function between 0 and 1
    to simulate plant ready state

    formula: 1 - e^(-e^x)
    """
    return 1 - np.exp(-np.exp((x / scale) * 7 - transpose))


def sigmoid_norm(x, scale=1.0, transpose=5.0):
    """
    Calculates sigmoid function between 0 and 1
    to simulate plant ready state

    formula: 1 / (1 + e^(-x))
    """
    return 1 / (1 + np.exp(-((x/scale) * 9 - transpose)))


def saturate(days, sigmoid=None):
    """
    Generates states as smooth s-curve scaled to
    period of blossoming
    """
    if sigmoid is None:
        sigmoid = sigmoid_norm

    states = []

    for day in days:
        states.append(sigmoid(day, scale=max(days)))

    column = np.array(states)

    return column
