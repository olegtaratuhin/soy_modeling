# This file prepares day time data for 2 locations using
# custom implemented module
from math import tan, sin, cos, pi, acos
import datetime
import pandas as pd
from functools import reduce


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
    deg_to_rad = lambda x: x * pi / 180
    rad_to_deg = lambda x: x * 180 / pi

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
        hour_angle = rad_to_deg(acos(tan(lat_in_rad) * tan(deg_to_rad(declination))))
        angle_increment = 15.0

        return 2.0 * hour_angle / angle_increment


latitude_dict = {
    '26063': 59.7176,
    '34927': 45.0393
}

to_latitude = lambda x: latitude_dict[x]


def construct_data(dataframe):
    """
    Function to calculate day length data and attach it to main
    data
    """
    day_length = []

    def calculate_daylen(row):
        """
        Hepler function to generate series with day length data
        """
        station, year, month, day = row[0], row[1], row[2], row[3]
        date = str(int(day)) + '.' + str(int(month)) + '.' + str(int(year))
        station = str(int(station))

        return pd.Series(get_daylength(to_latitude(station), date), index=['Photoperiod'])

    day_len_frame = dataframe.apply(calculate_daylen, axis=1)

    return pd.concat([dataframe, day_len_frame], axis=1)


def format_date(dataframe):
    """
    Function to convert date representation in different column to date
    in a single column in format: yyyy.mm.dd so that they can be compared
    """
    formated_header = ["Station", "Date", "T_min", "T_avg",
                       "T_max", "Precipitation", "Photoperiod"]

    def format_date(row):
        station, year, month, day, *other = row
        date = '{}.{:02}.{:02}'.format(int(year), int(month), int(day))
        content = [station, date, *other]

        return pd.Series(content, index=formated_header)

    return dataframe.apply(format_date, axis=1)


def main():
    frame = pd.read_csv('dataset/daily_temp_precip.csv', index_col=0)
    print("Dataframe loaded from csv")

    print("Before:")
    print(frame[0:5])
    frame_with_daylen = construct_data(frame)
    print("After:")
    print(frame_with_daylen[0:5])

    frame_with_daylen.to_csv('dataset/daily_data.csv')
    print("Photoperiod calculated and attached to dataframe")


def main1():
    frame = pd.read_csv('dataset/daily_data.csv', index_col=0)
    print("Dataframe loaded")

    print("Before:")
    print(frame[0:5])
    modified = format_date(frame)
    print("After:")
    print(modified[0:5])

    modified.to_csv('dataset/daily_data.csv')
    print("Modified data saved")


if __name__ == '__main__':
    main1()
