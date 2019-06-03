# -*- coding: utf-8 -*-
"""Evaluator definition file.

This file contains definition of evaluation of
model procedure. Once evaluation is done it gives away
specified metrics.

Example:
    Model is evaluated as follows:

        from evaluator import evaluate

        evaluate(model, test_data, metrics=['MSE'], target=['protein'])

Attributes:
    evaluate (list): calculate given metrics on test data with given model.

Todo:
    * Add evaluation procedure

"""


def evaluate(model, test_data, metrics):
    """
    Evaluate given model on test data with given metrics.

    Args:
        model (keras.Model): model.
        test_data (pd.DataFrame): test data.
        metrics (list): metrics to evaluate model with.
    Returns:
        metrics shown by model on given test_data in same order as
            metrics were in argument list.
    """
    return []
