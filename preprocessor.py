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

from functools import reduce
import datetime
from math import tan, sin, cos, pi, acos
import pandas as pd
import math


def _heaviside(x):
    return 1 if x >= 0 else 0


def gated_func(c):
    return lambda x: (x - c) * _heaviside(x - c)


def normalization(mu):
    return lambda x: x/mu


def preprocess_func(c, mu):
    return normalization(mu)(gated_func(c))


def get_day_number(date, format='%d.%m.%Y'):
    """
    Accepts date in format: 'dd.mm.yyyy' and returns
    number of the day in year
    """
    date = datetime.datetime.strptime(date, format)
    new_year_day = datetime.datetime(year=date.year, month=1, day=1)
    return (date - new_year_day).days + 1


def get_daylength(latitude, date):
    """
    Calculate day time as difference between sunrise and sunset
    Calculation is made using hour angle using Brock model.
    """
    def deg_to_rad(x): return x * pi / 180
    def rad_to_deg(x): return x * 180 / pi

    lat_in_rad = deg_to_rad(latitude)
    day_of_year = get_day_number(date)
    days_in_year = 365
    full_circle_degrees = 360.0
    magnitude_ha = -23.45

    declination = magnitude_ha * sin(deg_to_rad(full_circle_degrees *
                                                (283.0 + day_of_year)/days_in_year))

    if -tan(lat_in_rad) * tan(deg_to_rad(declination)) <= -1.0:
        return 24.0
    elif -tan(lat_in_rad) * tan(deg_to_rad(declination)) >= 1.0:
        return 0.0
    else:
        hour_angle = rad_to_deg(
            acos(tan(lat_in_rad) * tan(deg_to_rad(declination))))
        angle_increment = 15.0

        return 2.0 * hour_angle / angle_increment

latitude_dict = {
    'Пушкин': 59.7176,
    'КОС': 45.0393
}

def to_latitude(x):
    return latitude_dict[x]


def enrich(label_data_path, meteo_data_path, parsed_args, targets):
    """
    Enrich data with database data.

    Creates a new pd.DataFrame with initial data
    as labels for database data organized by date.

    Args:
        label_data (str): peth to csv dataframe with labeled data
        meteo_data (str): dataframe to csv with database data
    Returns:
        new pd.DataFrame enriched from both sources.
    """

    min_temp_processor = preprocess_func(*parsed_args.min_temp_params)
    max_temp_processor = preprocess_func(*parsed_args.max_temp_params)
    rain_processor = preprocess_func(*parsed_args.rain_params)
    all_sky_rad_processor = preprocess_func(*parsed_args.all_sky_rad_params)
    clear_sky_rad_processor = preprocess_func(*parsed_args.clear_sky_rad_params)
    day_count_processor = normalization(parsed_args.day_count_processor)
    photoperiod_processor = preprocess_func(*parsed_args.photoperiod_params)

    label_data_df = pd.read_csv(label_data_path)
    # logger.debug(f"Opened label data at path: {label_data_path}")

    meteo_data_df = pd.read_csv(meteo_data_path)
    # logger.debug(f"Opened mateo data at path: {meteo_data_path}")

    for i, row in label_data_df.iterrows():
        pass
