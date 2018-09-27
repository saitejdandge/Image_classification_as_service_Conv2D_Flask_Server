from utils import *
from matplotlib import pyplot
import matplotlib.pyplot as plt
from keras.layers import Dense, Conv2D, Dropout, Activation,MaxPooling2D,Flatten
from sklearn.model_selection import train_test_split
from keras.models import Sequential
import tkinter as tk
from tkinter.filedialog import askdirectory
import numpy as np
from sklearn.metrics import classification_report
import sys
import os


#original_data_dir = askdirectory()



original_data_dir  = sys.argv[1]

# base_folder=os.path.basename(original_data_dir)


	
x=get_value('x',original_data_dir)

y=get_value('y',original_data_dir)

if x is None or y is None:
	
	print("Please run preprocess.py before running model.py ...")
	
	exit()
	
	pass

print('x shape',x.shape)

print('y shape',y.shape)


x_train,x_val,y_train,y_val=train_test_split(x,y)


x_train=x_train.astype('float32')

x_train/=255


x_val_scaled=x_val.astype('float32')

x_val_scaled/=255


#Building model
model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=x.shape[1:]))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.5))
model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.5))
model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.5))
model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(y.shape[1]))
model.add(Activation('softmax'))

print(model.summary())

# model.load_weights(base_folder+'/model_data/model_weights.h5')



model.compile(loss='categorical_crossentropy',optimizer='rmsprop',metrics=['accuracy'])

history=model.fit(x_train,y_train,epochs=10,validation_data=(x_val_scaled,y_val), batch_size=10, verbose=1)

if not (os.path.isdir(original_data_dir+"/model_data")):
	os.makedirs(original_data_dir+"/model_data")
	pass

model_name="model"

model.save_weights(original_data_dir+'/model_data/'+model_name+'_weights.h5')

model.save(original_data_dir+'/model_data/'+model_name+'.h5')

print("Model saved")

model.evaluate(x_val_scaled,y_val)

pyplot.plot(history.history['acc'],label='Training Accuracy')

pyplot.plot(history.history['val_acc'],label='Validation Accuracy')

pyplot.legend()

report =classification_report(convert_to_labels(y_val,original_data_dir),convert_to_labels(model.predict(x_val_scaled),original_data_dir))

print(report)

# show_prediction_images(x_val,y_val,model,original_data_dir)

# pyplot.show()