# -*- coding: utf-8 -*-
"""Logger definition file.

This file contains definition of logger. Logger is a custom
wrapper around standart python logger, but allows to write
into custom file each launch of program.

Example:
    Logger import is defined as follows:

        from logger import configure, get_logger

        configure('123.log')
        ...
        module_logger = get_logger(__name__)

Attributes:
    configure_logger (None): file for file handler to write
        complete log to.
    get_logger (Logger): get module-specific logger.

Todo:
    * Add log housekeeping

"""

import logging
import sys


_configured = False
_file = None

def configure(file):
    """
    Logger configuration method.

    Configure logger prior to use.

    Args:
        file (str): a file to append log to.
    Returns:
        None
    """
    global _file
    global _configured

    if _file is not None:
        _file = file
        _configured = True


def get_logger(module_name):
    """
    Getter for logger.

    Get module specific logger. It will log only errors to console,
    full log will be available at file configured.
    """
    global _file
    global _configured

    if not _configured:
        raise Exception("Logger should be configured prior to use")

    logger = logging.getLogger(module_name)
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler(stream=sys.stdout)
    console_handler.setLevel(logging.ERROR)
    console_formatter = logging.Formatter('%(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)

    file_handler = logging.FileHandler(_file, 'a')
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter('[%(asctime)s] %(levelname)8s ---' +
        ' %(message)s (%(filename)s:%(lineno)s)', datefmt='%Y-%m-%d %H:%M:%S')
    file_handler.setFormatter(file_formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
