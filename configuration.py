# -*- coding: utf-8 -*-
"""Configuration holder definition file.

This file contains definition of configuration class.
This class resolves parsed arguments and configures
the rest of the modules with their respectfull run
configurations.

Example:
    Configuration is created as follows:

        from configuration import Configuration

        args = Parser.parse(input_args)
        configuration = Configuration(args)

        ...
        preprocessor = Preprocessor(configuration)
        model = get_model(configuration)
        evaluator = Evaluator(configuration)
        ...

Attributes:
    Configuration (class): configuration holder class.

Todo:
    * Add configuration implementation.

"""


class Configuration(object):
    """Configuration class."""

    def __init__(self, *args, **kwargs):
        pass
