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

list_of_acc = pd.unique(df_full['name'])
print(list_of_acc)

for d in list_of_acc:
    print("using:", d)
	model = load_model('blossum_model_' + d + '.h5')
    print(model.summary())
    df = df_full.loc[df_full['name'] == d]
    features = ['t_min', 't_max', 'dlen', 'day']
    data = df[features].values
    predicted_blossum = model.predict(data)
    df.insert(1, 'new', predicted_blossum)
	df = df.loc[df['new'] >= 0.6]
	df = df.loc[df.groupby('ID')['new'].idxmin()]
    df.to_csv('futura_prediction_' + d + '.csv')
