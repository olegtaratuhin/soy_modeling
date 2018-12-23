# Thif file generated sigmoid function for mapping state
import numpy as np


def sigmoid_linearized(x, scale=1.0, transpose=0.0, left_step=0.2, right_step=0.8):
    """
    Calculate sigmoid function between 0 and 1
    to simulate plant ready state

    formula: 0 for x in (-inf, left_step * scale)
             x / ((right_step - left_step) * scale) - left_step / (right_step - left_step)
             1 for x in [right_step * scale, +inf)
    """

    if (x <= left_step * scale):
        return 0.0
    elif (x >= right_step * scale):
        return 1.0
    else:
        inner_step = right_step - left_step
        return x / (inner_step * scale) - left_step / inner_step


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
    Generates states as s-curve scaled to
    period of blossoming
    """
    if sigmoid is None:
        sigmoid = sigmoid_linearized

    states = []

    for day in days:
        states.append(sigmoid(day, scale=max(days)))

    column = np.array(states)

    return column
