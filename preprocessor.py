# -*- coding: utf-8 -*-
"""Preprocessor definition file.

This file contains definition of preprocessor, this class enriches
label data with detailed data for temperature, rain and other features.
This class also transforms data into form for the ML model.

Example:
    Preprocessor import is defined as follows:

        from preprocessor import enrich, transform

        enriched_data = enrich(label_data, database)
        transformed = transform(enriched_data, configuration)

Attributes:
    enrich (pd.DataFrame): data frame with data.
    transform (pd.DataFrame): transform enriched data to ML ready
        format.

Todo:
    * Add enrich
    * Add transform

"""

import pandas as pd


def enrich(label_data, database):
    """
    Enrich data with database data.

    Creates a new pd.DataFrame with initial data
    as labels for database data organized by date.

    Args:
        label_data (pd.DataFrame): dataframe with labeled data
        database (pd.DataFrame): dataframe with database data
    Returns:
        new pd.DataFrame enriched from both sources.
    """
    return pd.DataFrame([])


def transform(enriched_data, configuration):
    """
    Transform data with configured functions.

    Args:
        enriched_data (pd.DataFrame): dataframe with data
    """
    return pd.DataFrame([])
