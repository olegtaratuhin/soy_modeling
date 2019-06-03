# Temporary file to parse hex data to more convinient csv format
import pandas as pd
import numpy as np


def bytes_from_file(filename, chunksize=8192):
    with open(filename, "rb") as f:
        while True:
            chunk = f.read(chunksize)
            if chunk:
                for b in chunk:
                    yield b
            else:
                break


def to_csv(fileFrom, fileTo):
    """
    Convert files in txt format without delimiters to csv
    """
    content = []

    with open(fileFrom) as f:
        for line in f.readlines():
            content.append(list(filter(lambda x: x != '0', line.split()))[:8])

    frame = pd.DataFrame(content)
    frame.columns = ['Station', 'Year', 'Month', 'Day', 'T_min', 'T_avg', 'T_max', 'Precipitation']
    frame.to_csv(fileTo)
    print("Data frame is writen to csv")


def reformat_data():
    to_csv("dataset/26063.txt", "dataset/26063_csv.csv")
    to_csv("dataset/34927.txt", "dataset/34927_csv.csv")


def merge_data(files, fileTo):
    dataframe = pd.concat([pd.read_csv(file, engine='c', index_col=0) for file in files])

    print(len(dataframe), "entries are collected from", len(files), "sources")
    print(dataframe[0:-5])
    dataframe.to_csv(fileTo)


def main():
    merge_data(["dataset/26063_csv.csv", "dataset/34927_csv.csv"], "dataset/daily_temp_precip.csv")


if __name__ == "__main__":
    main()
