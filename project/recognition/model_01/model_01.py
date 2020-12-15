# imports for array-handling and plotting
import numpy as np
import matplotlib
#matplotlib.use('agg') when this line is active the matplotlib won't show anything
import matplotlib.pyplot as plt
import cv2
import glob
import os, os.path

# let's keep our keras backend tensorflow quiet
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='3'

# keras imports for the dataset and building our neural network
from keras.datasets import mnist
from keras.models import Sequential, load_model
from keras.layers.core import Dense, Dropout, Activation
from keras.utils import np_utils

(X_train, y_train), (X_test, y_test) = mnist.load_data()

# let's print the shape before we reshape and normalize
#print("X_train shape", X_train.shape)
#print("y_train shape", y_train.shape)
#print("X_test shape", X_test.shape)
#print("y_test shape", y_test.shape)

# building the input vector from the 28x28 pixels
#print(X_test[0].shape)
X_train = X_train.reshape(60000, 784)
X_test = X_test.reshape(10000, 784)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
#print(X_test[0].shape)
# normalizing the data to help with the training
X_train /= 255
X_test /= 255

# print the final input shape ready for training
#print("Train matrix shape", X_train.shape)
#print("Test matrix shape", X_test.shape)

# one-hot encoding using keras' numpy-related utilities
n_classes = 10
#print("Shape before one-hot encoding: ", y_train.shape)
Y_train = np_utils.to_categorical(y_train, n_classes)
Y_test = np_utils.to_categorical(y_test, n_classes)
#print("Shape after one-hot encoding: ", Y_train.shape)

# building a linear stack of layers with the sequential model
model = Sequential()
model.add(Dense(512, input_shape=(784,)))
model.add(Activation('relu'))                            
model.add(Dropout(0.2))

model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.2))

model.add(Dense(10))
model.add(Activation('softmax'))
'''
# compiling the sequential model
model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adam')

# training the model and saving metrics in history
history = model.fit(X_train, Y_train,
          batch_size=128, epochs=20,
          verbose=2,
          validation_data=(X_test, Y_test))

from keras.models import load_model

model.save('keras_mnist.h5')
'''
def res():
    # load the model and create predictions 
    mnist_model = load_model('/home/medamine/Desktop/project/recognition/model_01/keras_mnist.h5')
    loss_and_metrics = mnist_model.evaluate(X_test, Y_test, verbose=2)

    img = cv2.imread('note_00.png', 0)

    img = img.reshape(1,784)
    img = img / 255
    prediction = mnist_model.predict_classes(img)
    print(prediction[0])

res()
