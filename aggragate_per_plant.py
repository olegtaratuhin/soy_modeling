# File to aggrete data in format grouped by plant
import numpy as np
import pandas as pd
from datetime import date, timedelta

from generate_sigmoid import saturate
from data_transformer import Data_transformer


def convert_to_date(str):
    day, month, year, *_ = str.split(".")

    return date(int(year), int(month), int(day))


def parse_dates(row):
    date_from = row[5]
    date_to = row[6]

    return convert_to_date(date_from), convert_to_date(date_to)


stations_num = {'Kuban': 34927, 'Pushkin': 26063}


def parse_station(row):
    return stations_num[row[0]]

def parse_category_number(row):
    return row[2]

def parse_plant_name(row):
    return row[3]

def generate_subarrays(arr):
    accumulated = list()

    i = 0
    while i < len(arr):
        accumulated.append(arr[:i + 1])
        i += 1

    return accumulated


def create_batch(row, days_frame, transformer):
    date_from, date_to = parse_dates(row)

    event_day = (date_to - date_from).days
    all_samples_duration = 67

    dates_between = [date_from + timedelta(i) for i in range(all_samples_duration + 1)]
    date_to = dates_between[len(dates_between) - 1]
    days = [i for i in range(len(dates_between))]
    plants_state = saturate(days, event_day)

    station_val = parse_station(row)
    station = [station_val] * len(plants_state)
    category_val = parse_category_number(row)
    category = [category_val] * len(plants_state)
    plant_name_val = parse_plant_name(row)
    plant_name = [plant_name_val] * len(plants_state)

    batch_dataframe = days_frame.loc[(days_frame.Date >= str(date_from)) & \
                                     (days_frame.Date <= str(date_to)) & \
                                     (days_frame.Station == station_val)]

    t_min = batch_dataframe['T_min'].tolist()
    t_max = batch_dataframe['T_max'].tolist()
    dlen = batch_dataframe['Photoperiod'].tolist()

    day_max = max(days)

    return pd.DataFrame(np.column_stack([
        list(map(transformer.transform_t_min, generate_subarrays(t_min))),
        list(map(transformer.transform_t_max, generate_subarrays(t_max))),
        list(map(transformer.transform_avg_dlen, generate_subarrays(dlen))),
        [day / day_max for day in days],
        station,
        category,
        plant_name,
        plants_state
    ]), columns=['t_min', 't_max', 'dlen', 'day', 'station', 'category', 'name', 'state'])


def main():
    marked_data = pd.read_csv('dataset/soydata_upto_2010.csv',
        sep=';', parse_dates=False, index_col=0)
    days_frame = pd.read_csv('dataset/daily_data.csv',
        sep=',', parse_dates=False, index_col=0)

    days_frame['Date'] = pd.to_datetime(days_frame['Date'])
    days_frame['Station'] = pd.to_numeric(days_frame['Station'], downcast='integer')

    transformer = Data_transformer()

    dataframes = list()

    counter = 0
    for _, row in marked_data.iterrows():
        dataframes.append(create_batch(row, days_frame, transformer))

        if counter % 20 == 0:
            print(counter, "entries compiled")
        counter += 1

    print("Compiling together")
    d = {i: df for i, df in enumerate(dataframes)}
    super_frame = pd.concat(d.values(), axis=0, keys=d.keys())

    print("Compiled:")
    print(super_frame)

    super_frame.to_csv('dataset/soy_data.csv')


if __name__ == '__main__':
    main()
