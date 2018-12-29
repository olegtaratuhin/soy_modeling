# -*- coding: utf-8 -*-

from matplotlib import cm
from matplotlib import gridspec
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics
import random

import tensorflow as tf
import keras
from sklearn.metrics import r2_score as r2_metric
from keras import optimizers
from keras import backend as K
from keras.models import load_model

df_full = pd.read_csv('futura_data.csv')

list_of_groups = pd.unique(df_full['ID'])

print(list_of_groups)
result = df_full.loc[df_full.groupby('ID')['day'].idxmin()]
list_of_acc = result['name']
print(list_of_acc)

for idp, d in zip(list_of_groups, list_of_acc):
#if True:
#    d = list_of_acc[idp]
    print("using:", d)
    df = df_full.loc[df_full['ID'] == idp]
    model = load_model('blossum_model_' + d + '.h5')
    print(model.summary())

    features = ['t_min', 't_max', 'dlen', 'day']
    data = df[features].values
    predicted_blossum = model.predict(data)
    df_predicted = df
    df_predicted.insert(1, 'new', predicted_blossum)
    blossum_dates_predicted = df_predicted.loc[df_predicted['new'] >= 0.6]
    blossum_dates_predicted = blossum_dates_predicted.loc[blossum_dates_predicted.groupby('ID')['new'].idxmin()]
    result.loc[result['ID'] == idp, 'd'] = blossum_dates_predicted['d'].values

print(result)
result.to_csv('futura_prediction.csv')
