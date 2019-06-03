# -*- coding: utf-8 -*-
"""Optimizer definition file.

This file contains definition of optimizer. Optimizer is used
to tune hyperparameters. Used mainly for local tuning and
testing.

Example:
    Parser import is defined as follows:

        from optimizer import Optimizer

        evaluator = Evaluator(configuration)
        optimizer = Optimizer(configuration)

        with optimizer.session_start() as session:
            preprocessor = Preprocessor(session.get_preprocessor_params)
            model = Model(session.get_optimizer_params)
            evaluator.evaluate(model, test_data)

            session.run()

Attributes:
    Parser (class): a command line arguments parser class.
    get_configuration (Configuration): get configuration from arguments.

Todo:
    * Add Parser implementation
    * Add configuration api
    * Add configuration implementation

"""
