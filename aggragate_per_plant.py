# File to aggrete data in format grouped by plant
import numpy as np
import pandas as pd
from datetime import date, timedelta
from generate_sigmoid import saturate


def convert_to_date(str):
    year, month, day, *_ = str.split(".")
    return date(year, month, day)


def parse_dates(row):
    date_from = row[5]
    date_to = row[7]

    return convert_to_date(date_from), convert_to_date(date_to)


stations_num = {'Kuban': '34927', 'Pushkin': '26063'}


def parse_station(row):
    return stations_num[row[0]]


def create_batch(row, days_frame, predictors):
    date_from, date_to = parse_dates(row)

    dates_between = [date_from + timedelta(i) for i in range((date_ro - date_from).days + 1)]
    plants_state = saturate(dates_between)

    station = parse_station(row)

    batch_dataframe = days_frame.loc[(data_frame.Date >= date_from) &
                                     (data_frame.Data <= date_to)]

    


def main():
    pass


if __name__ == '__main__':
    main()
