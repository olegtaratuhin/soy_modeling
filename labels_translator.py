# coding=<utf-8>
# This file is for functions and classes related to translating labels
from collections import defaultdict, namedtuple
from itertools import count


class ConstantsTranslator(object):
    """
    Class for constants and common structures for translating
    labels of the model.
    """

    # named tuple for easier work woth labeled data
    Label = namedtuple('Label', ['shortname', 'longname'])

    # counter for the shortnames to generate values sequentially
    counter = count()

    # define a counter
    next(counter)
    next(counter)

    # Grammar for shortnames:
    # (MODIFIER)_(VALUE)_(DAYS BEFORE)(EVENT OR INTERVAL)(DAYS AFTER)
    _, LOCATION, YEAR, CATEG, NAME, DATE_SOW, DATE_SPR, DATE_BLOS, TIME_SOWBLOS, \
        TIME_SOWSPR, SUM_TEMP_SOWSPR, SUM_TEMP_SOWBLOS, TEMP_SOW, AVG_TEMP_SOWBLOS, \
        AVG_TEMP_SOWSPR, AVG_TEMP_SOW5, AVG_TEMP_SOW10, AVG_TEMP_SOW15, AVG_TEMP_SOW20, \
        AVG_TEMP_SOW30, AVG_TEMP_SOW40, AVG_TEMP_SOW50, AVG_TEMP_SOW60, AVG_RAIN_5SOW, \
        AVG_RAIN_SOW5, AVG_RAIN_SOW10, AVG_RAIN_SOW15, AVG_RAIN_5SOW5, AVG_RAIN_5SOW10, \
        AVG_RAIN_SOW20, AVG_RAIN_SOW30, AVG_RAIN_SOW40, AVG_RAIN_SOW50, \
        AVG_RAIN_SOW60, TEMP_SPR, AVG_TEMP_SPR30, AVG_TEMP_SPR40, AVG_TEMP_SPR50, \
        AVG_TEMP_SPR60, AVG_RAIN_SPR30, AVG_RAIN_SPR40, AVG_RAIN_SPR50, AVG_RAIN_SPR60, \
        DLEN_SPR, DLEN_BLOS, AVG_DLEN_SPRBLOS, AVG_DLEN_SPR10, AVG_DLEN_SPR20, AVG_DLEN_SPR30, \
        AVG_DLEN_SPR40, AVG_DLEN_SPR50 = [i for i in range(51)]

    # Group for target params
    GROUP_RESULTS = {TIME_SOWSPR, TIME_SOWBLOS}

    # Group for sums of temperature
    GROUP_SUM_TEMP = {SUM_TEMP_SOWSPR, SUM_TEMP_SOWBLOS}

    # Group for temperature data around sowing date
    GROUP_TEMP_SOW = {AVG_TEMP_SOWSPR, AVG_TEMP_SOW5, AVG_TEMP_SOW10,
AVG_TEMP_SOW15, AVG_TEMP_SOW20}

    # Group for rainfall data around sowing date
    GROUP_RAIN_SOW = {AVG_RAIN_5SOW, AVG_RAIN_SOW5, AVG_RAIN_SOW10,
                      AVG_RAIN_SOW15, AVG_RAIN_5SOW5, AVG_RAIN_5SOW10,
                      AVG_RAIN_SOW20, AVG_RAIN_SOW30, AVG_RAIN_SOW40,
                      AVG_RAIN_SOW50, AVG_RAIN_SOW60}

    # Group for temperature data around sprouting date
    GROUP_TEMP_SPR = {TEMP_SPR, AVG_TEMP_SPR30, AVG_TEMP_SPR40,
                      AVG_TEMP_SPR50, AVG_TEMP_SPR60}

    # Group for rain data around sprouting date
    GROUP_RAIN_SPR = {AVG_RAIN_SPR30, AVG_RAIN_SPR40,
                      AVG_RAIN_SPR50, AVG_RAIN_SPR60}

    # Group for day length data between sprouting and blossoming
    GROUP_DLEN_SPRBLOS = {DLEN_SPR, DLEN_BLOS, AVG_DLEN_SPRBLOS,
                          AVG_DLEN_SPR10, AVG_DLEN_SPR20, AVG_DLEN_SPR30,
                          AVG_DLEN_SPR40, AVG_DLEN_SPR50}

    dict = defaultdict(str)
    dict = {
        "kubanloc": Label(LOCATION, "Location"),
        "god": Label(YEAR, "Year"),
        "Kat.No": Label(CATEG, "Category"),
        "Name": Label(NAME, "Plant name"),
        "Data.poseva": Label(DATE_SOW, "Date of sowing"),
        "data.vskhodov": Label(DATE_SPR, "Date of sprouting"),
        "Data.tsveteniya": Label(DATE_BLOS, "Date of blossoming"),
        "Posev.vskhody": Label(TIME_SOWSPR, "Days between sowing and sprouting"),
        "Vskhody.tsveteniye": Label(TIME_SOWBLOS, "Days between sowing and blossoming"),
        "Summa.temperatur.posev..vskhody": Label(SUM_TEMP_SOWSPR, "Sum of temperatures between sowing and sprouting"),
        "Summa.temperatur.vskhody.tsv": Label(SUM_TEMP_SOWBLOS, "Sum of temperatures between sowing and blossoming"),
        "T·sr.p.v": Label(AVG_TEMP_SOWSPR, "Average temperature from sowing to sprouting"),
        "T·sr.v.ts": Label(AVG_TEMP_SOWBLOS, "Average temperature from sowing to blossoming"),
        "Tposeva": Label(TEMP_SOW, "Average temperature on the sowing day"),
        "T·sr5dneyposleposeva": Label(AVG_TEMP_SOW5, "Average temperature within 5 days after sowing"),
        "T·sr1d0neyposleposeva": Label(AVG_TEMP_SOW10, "Average temperature within 10 days after sowing"),
        "T·sr15dneyposleposeva": Label(AVG_TEMP_SOW15, "Average temperature within 15 days after sowing"),
        "T·sr20dneyposleposeva": Label(AVG_TEMP_SOW20, "Average temperature within 20 days after sowing"),
        "T·sr30dneyposleposeva": Label(AVG_TEMP_SOW30, "Average temperature within 30 days after sowing"),
        "T·sr40dneyposleposeva": Label(AVG_TEMP_SOW40, "Average temperature within 40 days after sowing"),
        "T·sr50dneyposleposeva": Label(AVG_TEMP_SOW50, "Average temperature within 50 days after sowing"),
        "T·sr60dneyposleposeva": Label(AVG_TEMP_SOW60, "Average temperature within 60 days after sowing"),
        "srOs5sut.do.poseva": Label(AVG_RAIN_5SOW, "Average rainfall within 5 days prior to sowing"),
        "srOs5sutposle.poseva": Label(AVG_RAIN_SOW5, "Average rainfall within 5 days after sowing"),
        "srOs10sutposleposeva": Label(AVG_RAIN_SOW10, "Average rainfall within 10 days after sowing"),
        "srOs5do5posle": Label(AVG_RAIN_5SOW5, "Average rainfall within 5 days before and 5 days after sowing"),
        "srOs5do.10posle": Label(AVG_RAIN_5SOW10, "Average rainfall within 5 days before and 10 days after sowing"),
        "sr.os15sut.posle.poseva": Label(AVG_RAIN_SOW15, "Average rainfall within 15 days after sowing"),
        "sr.os20sut.posle.poseva": Label(AVG_RAIN_SOW20, "Average rainfall within 20 days after sowing"),
        "sr.os30sut.posle.poseva": Label(AVG_RAIN_SOW30, "Average rainfall within 30 days after sowing"),
        "sr.os40sut.posle.poseva": Label(AVG_RAIN_SOW40, "Average rainfall within 40 days after sowing"),
        "sr.os50sut.posle.poseva": Label(AVG_RAIN_SOW50, "Average rainfall within 50 days after sowing"),
        "sr.os60sut.posle.poseva": Label(AVG_RAIN_SOW60, "Average rainfall within 60 days after sowing"),
        "Tvskhodov": Label(TEMP_SPR, "Average temperature on the sprouting day"),
        "T·sr30dneyposlevskhodov": Label(AVG_TEMP_SPR30, "Average temperature within 30 days after sprouting"),
        "T·sr40dneyposlevskhodov": Label(AVG_TEMP_SPR40, "Average temperature within 40 days after sprouting"),
        "T·sr50dneyposlevskhodov": Label(AVG_TEMP_SPR50, "Average temperature within 50 days after sprouting"),
        "T·sr60dneyposlevskhodov": Label(AVG_TEMP_SPR60, "Average temperature within 60 days after sprouting"),
        "sr.os30sut.posle.vskh": Label(AVG_RAIN_SPR30, "Average rainfall within 30 days after sprouting"),
        "sr.os40sut.posle.vskh": Label(AVG_RAIN_SPR40, "Average rainfall within 40 days after sprouting"),
        "sr.os50sut.posle.vskh": Label(AVG_RAIN_SPR50, "Average rainfall within 50 days after sprouting"),
        "sr.os60sut.posle.vskh": Label(AVG_RAIN_SPR60, "Average rainfall within 60 days after sprouting"),
        "Dlina_dnya_vskhody": Label(DLEN_SPR, "Day length on the sprouting day"),
        "Dlina_dnya_tsveteniye": Label(DLEN_BLOS, "Day length on the blossoming day"),
        "Srednyaya.Dlina_dnya_v_ts": Label(AVG_DLEN_SPRBLOS, "Average day length between sprouting and blossoming"),
        "srednyaya_Dlina_dnya_10dney.posle.vskhodov": Label(AVG_DLEN_SPR10, "Average day length within 10 days after sprouting"),
        "sr_Dlina_dnya_20dney.posle.vskhodov": Label(AVG_DLEN_SPR20, "Average day length within 20 days after sprouting"),
        "sr_Dlina_dnya_30dney.posle.vskhodov": Label(AVG_DLEN_SPR30, "Average day length within 30 days after sprouting"),
        "sr_Dlina_dnya_40dney.posle.vskhodov": Label(AVG_DLEN_SPR40, "Average day length within 40 days after sprouting"),
        "sr_Dlina_dnya_50dney.posle.vskhodov": Label(AVG_DLEN_SPR50, "Average day length within 50 days after sprouting")
    }

    explanation_dict = {value.shortname: value.longname for _, value in dict.items()}


def labels_translator(labels):
    """
    Translate labels into easy-to-read format
    """
    new_labels = list()

    for label in labels:
        new_labels.append(ConstantsTranslator.dict[label].shortname)

    return new_labels


def get_labels_with_index(features):
    return [ConstantsTranslator.explanation_dict[feature] for feature in features]
