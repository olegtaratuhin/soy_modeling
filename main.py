# -*- coding: utf-8 -*-
"""Main file.

This file contains glue code for other modules and serves
as entry point to pipeline.

Todo:
    * Add Parser implementation
    * Add configuration api
    * Add configuration implementation

"""

from parser import Parser
from logger import LoggerDispatcher
import time
import datetime


if __name__ == "__main__":
    parser = Parser()
    parsed_args = parser.parse_args()

    timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S')
    dispatcher = LoggerDispatcher(f"logs/{timestamp}.log")

    logger = dispatcher.get_logger(__file__)
    logger.info(msg="Parsed arguments: " + str(parsed_args))
