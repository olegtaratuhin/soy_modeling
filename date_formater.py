# This file is for change of formatting for date in csv file
import pandas as pd


def change_format(frame):
    """
    Function for changing date format so it is comparable lexicographicaly
    """
    frame_header = frame.columns.values

    def inverse_date(date):
        day, month, year = date.split(".")
        return '{}.{:02}.{:02}'.format(int(year), int(month), int(day))

    def inverse_dates(row):
        loc, year, kat, name, date_sow, date_spr, date_blos, *other = row

        return pd.Series([loc, year, kat, name, inverse_date(date_sow),
                          inverse_date(date_spr), inverse_date(date_blos),
                          *other], index=frame_header)

    new_frame = frame.apply(inverse_dates, axis=1)

    return new_frame


def main():
    dataframe = pd.read_csv('dataset/soydata_upto_2010.csv', index_col=0, sep=';')
    print("Data loaded")

    print("Before:")
    print(dataframe[0:5])

    formatted = change_format(dataframe)

    print("After:")
    print(formatted[0:5])

    formatted.to_csv('dataset/soydata_tmp.csv')
    print("Saved")


if __name__ == '__main__':
    main()
