# -*- coding: utf-8 -*-
"""Parser definition file.

This file contains definition of parser. Parser is used to read
command-line arguments and configure launch.

Example:
    Parser import is defined as follows:

        from parser import Parser

        parser = Parser(sys.argv)
        configuration = parseer.get_configuration

Attributes:
    Parser (class): a command line arguments parser class.
    get_configuration (Configuration): get configuration from arguments.

Todo:
    * Add Parser implementation
    * Add configuration api
    * Add configuration implementation

"""


class Parser(object):

    def __init__(self, *args, **kwargs):
        pass

    def get_configuration(self):
        pass
