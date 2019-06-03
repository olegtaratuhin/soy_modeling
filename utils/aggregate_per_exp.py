# File to aggregate data in format grouped by plant
import numpy as np
import pandas as pd
import datetime
from datetime import date, timedelta

from generate_sigmoid import saturate
from data_transformer import Data_transformer

from prepare_daytime_data import get_daylength


def convert_to_date(str):
    day, month, year, *_ = str.split(".")

    return date(int(year), int(month), int(day))


def parse_dates(row):
    date_from = row[5]
    date_to = row[6]

    return convert_to_date(date_from), convert_to_date(date_to)


data_indices = {'ID': 0, 'STABR': 1, 'god': 2,
                'RCP': 3,	'Name': 4,	'Data.vshodov': 5}


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


def create_batch(row, transformer):
    date_from = convert_to_date(row[data_indices['Data.vshodov']])

    all_samples_duration = 67

    dates_between = [date_from + timedelta(i)
                     for i in range(all_samples_duration + 1)]
    date_to = dates_between[len(dates_between) - 1]
    days = [i for i in range(len(dates_between))]

    station_abr = row[data_indices['STABR']]
    ID = row[data_indices['ID']]
    acc_nam = row[data_indices['Name']]
    year = int(row[data_indices['god']])
    rcp_nam = row[data_indices['RCP']]

    futura_weather_prefix = '/nilmbb/kkozlov/soy-ann'
    futura_weather_model = '11111111111111111'

    futura_weather_file = futura_weather_prefix + '/' + station_abr + '_' + \
        futura_weather_model + '_' + rcp_nam + '_' + \
        str(year) + '/' + station_abr + '0101.WTG'

    fp = open(futura_weather_file, "r")
    str_lat_lon = fp.readline()  # Third line contains lat lon
    str_lat_lon = fp.readline()
    str_lat_lon = fp.readline()

    TMPS1, LAT, LON, *_ = str_lat_lon.split()
    LAT = float(LAT)

    days_frame = pd.read_csv(
        futura_weather_file, delim_whitespace=True, skiprows=3, header=0)
#    print(days_frame.columns)
    days_frame['@DATE'] -= 1001
#    print(days_frame['@DATE'].values)
    days_frame['@DATE'] = pd.to_datetime(
        days_frame['@DATE'], unit='D', origin=pd.Timestamp(str(year) + '-01-01'))
#    print(days_frame['@DATE'].values)
#    batch_dataframe = days_frame.loc[(days_frame.Date >= str(date_from)) & (days_frame.Date <= str(date_to))]
    batch_dataframe = days_frame.loc[(days_frame['@DATE'] >= str(
        date_from)) & (days_frame['@DATE'] <= str(date_to))]
#    print(batch_dataframe['@DATE'].values)

    def calculate_daylen(row):
        dt = datetime.datetime.strptime(str(row[0]), '%Y-%m-%d %H:%M:%S')
        row[0] = str(dt.day) + '.' + str(dt.month) + '.' + str(dt.year)
        row[1] = get_daylength(LAT, row[0])

    batch_dataframe.apply(calculate_daylen, axis=1)

    t_min = batch_dataframe['TMIN'].tolist()
    t_max = batch_dataframe['TMAX'].tolist()
    dlen = batch_dataframe['SRAD'].tolist()

    day_max = max(days)

    return pd.DataFrame(np.column_stack([
        list(map(transformer.transform_t_min, generate_subarrays(t_min))),
        list(map(transformer.transform_t_max, generate_subarrays(t_max))),
        list(map(transformer.transform_avg_dlen, generate_subarrays(dlen))),
        [day / day_max for day in days],
        [station_abr] * len(days),
        [year] * len(days),
        [acc_nam] * len(days),
        [day / day_max for day in days]
    ]), columns=['t_min', 't_max', 'dlen', 'day', 'station', 'category', 'name', 'state'])


def main():
    marked_data = pd.read_csv('futura.csv', sep=',', parse_dates=False)
    marked_data.head(5)
    transformer = Data_transformer()

    dataframes = list()

    counter = 0
    for _, row in marked_data.iterrows():
        dataframes.append(create_batch(row, transformer))

        if counter % 20 == 0:
            print(counter, "entries compiled")
        counter += 1

    print("Compiling together")
    d = {i: df for i, df in enumerate(dataframes)}
    super_frame = pd.concat(d.values(), axis=0, keys=d.keys())

    print("Compiled:")
    print(super_frame)

    super_frame.to_csv('futura_data.csv')


if __name__ == '__main__':
    main()
