
"""Show GPU info"""

from tensorflow.python.client import device_lib
device_lib.list_local_devices()

"""### Import modules"""

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

from scipy.stats.stats import pearsonr

"""Import data set into pandas dataframe. The dataset contains a missing value on one of the key features the model will be training with, so we need to remove that explicitly"""

df_full = pd.read_csv('dataset/soy_data.csv')
df_full.head(5)


"""Select features and target parameter. As the data is shuffled at this point we no longer need multi-index, and selecting values will truncate that information automatically."""

namnam = pd.unique(df_full['name'])

for d in pd.unique(df_full['name']):
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
##  Model
##	We will use a simple model with input layer of 4 neurons, a single hidden layer with 20 neurons and 1 output neuron
### Keras model definition
	model = keras.Sequential()
	model.add(keras.layers.Dense(20, input_dim=4, activation=tf.nn.sigmoid))
	model.add(keras.layers.Dense(1, activation=tf.nn.sigmoid))
### Keras model compile"""
	sgd = optimizers.SGD(lr=10.06)
	model.compile(loss='mse',
	              optimizer=sgd,
	              metrics=['mse', 'mae'])
##Model summary shows the architecture of the keras model"""
	print(model.summary())
## Results"""
	#@title Hyperparameters { run: "auto", form-width: "30%" }
	epochs = 150 #@param {type:"integer"}
	history = model.fit(
	    train_input, train_output,
	    epochs=epochs,
	    verbose=0,
	    batch_size=25,
	    validation_split=0.001)
	loss, mse, mae = model.evaluate(test_input, test_output)
	print("MSE: ", mse)
	print("MAE: ", mae)
	# print("R2:  ", r2_value)
	print("Loss:", loss)
	model.save('blossum_model_' + d + '.h5')
	blossum_dates_dataset = df.loc[np.logical_and(df['state'] > 0.59, df['state'] < 0.61)]
	blossum_dates_dataset.to_csv('blossum_dates_dataset_' + d + '.csv')
	predicted_blossum = model.predict(data)
	df_predicted = df
	df_predicted.insert(1, 'new', predicted_blossum)
	blossum_dates_predicted = df_predicted.loc[df_predicted['new'] >= 0.6]
	blossum_dates_predicted = blossum_dates_predicted.loc[blossum_dates_predicted.groupby('ID')['new'].idxmin()]
	blossum_dates_predicted.to_csv('blossum_dates_predicted_' + d + '.csv')
	print("Len data:", len(blossum_dates_dataset), "Len model:", len(blossum_dates_predicted))
	if (len(blossum_dates_dataset) == len(blossum_dates_predicted)):
		q=blossum_dates_dataset['ID'].isin(blossum_dates_predicted['ID'])
		print("predicted:", sum(q), " min:", np.max(blossum_dates_dataset['d'].values - blossum_dates_predicted['d'].values), " max:", np.min(blossum_dates_dataset['d'].values - blossum_dates_predicted['d'].values), " abs:", np.mean(np.abs(blossum_dates_dataset['d'].values - blossum_dates_predicted['d'].values)))
		pearsonr(blossum_dates_dataset['d'].values, blossum_dates_predicted['d'].values)

