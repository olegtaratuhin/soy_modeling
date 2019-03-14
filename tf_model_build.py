
from scipy.stats.stats import pearsonr
from keras import backend as K
from keras import optimizers
from sklearn.metrics import r2_score as r2_metric
import keras
import tensorflow as tf
import random
from sklearn import metrics
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import gridspec
from matplotlib import cm

# from tensorflow.python.client import device_lib
# device_lib.list_local_devices()

def r2(y_true, y_pred):
    SS_res = K.sum(K.square(y_true-y_pred))
    SS_tot = K.sum(K.square(y_true - K.mean(y_true)))
    return (1 - SS_res/(SS_tot + K.epsilon()))

df_full = pd.read_csv('dataset/soy_data.csv')
df_full.head(5)

list_of_groups = pd.unique(df_full['name'])

for d in list_of_groups:
    #if True:
    #	d = namnam[8]
    print("using:", d)
    df = df_full.loc[df_full['name'] == d]
    #	df.head(5)
    features = ['t_min', 't_max', 'dlen', 'day']
    data = df[features].values
    target = df['state'].values
    #border =
    train_input, train_output = data, target
    test_input, test_output = data, target
    print("Train set contains", len(train_input))
    print("Test set contains", len(test_input))

    model = keras.Sequential()
    model.add(keras.layers.Dense(20, input_dim=train_input.shape[1], activation=tf.nn.sigmoid))
    model.add(keras.layers.Dense(1, activation=tf.nn.sigmoid))

    sgd = optimizers.SGD(lr=10.6)
    model.compile(loss='mae',
	              optimizer=sgd,
	              metrics=['mse', 'mae', r2])
    print(model.summary())
    epochs = 500
    history = model.fit(
	    train_input, train_output,
	    epochs=epochs,
	    verbose=0,
	    batch_size=25,
	    validation_split=0.05)
    loss, mse, mae, r2_score = model.evaluate(test_input, test_output)
    print("MSE: ", mse)
    print("MAE: ", mae)
    print("Loss:", loss)
    print("R2: ", r2_score)
    model.save('blossum_model_' + d + '.h5')
    blossum_dates_dataset = df.loc[np.logical_and(
		df['state'] > 0.59, df['state'] < 0.61)]
    blossum_dates_dataset.to_csv('blossum_dates_dataset_' + d + '.csv')
    predicted_blossum = model.predict(data)
    df_predicted = df
    df_predicted.insert(1, 'new', predicted_blossum)
    blossum_dates_predicted = df_predicted.loc[df_predicted['new'] >= 0.6]
    blossum_dates_predicted = blossum_dates_predicted.loc[blossum_dates_predicted.groupby('ID')[
            'new'].idxmin()]
    blossum_dates_predicted.to_csv('blossum_dates_predicted_' + d + '.csv')
    print("Len data:", len(blossum_dates_dataset),
	      "Len model:", len(blossum_dates_predicted))
    if (len(blossum_dates_dataset) == len(blossum_dates_predicted)):
        q = blossum_dates_dataset['ID'].isin(blossum_dates_predicted['ID'])

        val = np.mean(np.abs(blossum_dates_dataset['d'].values - blossum_dates_predicted['d'].values))
        var = np.std(np.abs(blossum_dates_dataset['d'].values - blossum_dates_predicted['d'].values))
        print("predicted:", sum(q),
            "min:", np.max(blossum_dates_dataset['d'].values - blossum_dates_predicted['d'].values),
            "max:", np.min(blossum_dates_dataset['d'].values - blossum_dates_predicted['d'].values),
            "abs:", val,
            "±",    var)
        pearsonr(blossum_dates_dataset['d'].values,
		         blossum_dates_predicted['d'].values)
