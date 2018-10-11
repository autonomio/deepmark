'''
BENCHMARKS: 

0.3 seconds on i7-7700k & 1070Ti
0.3 seconds on i7-7700k (force CPU)
1.3 seconds on i3-6100 & 1050Ti

'''

import time
import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
from keras.datasets import mnist

# load dataset
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# prepare data
train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# define model
model = models.Sequential()
model.add(Dense(512, activation='relu', input_shape=(28 * 28,)))
model.add(Dense(10, activation='softmax'))

# compile model
model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

t0 = time.time()
model.fit(train_images, train_labels, epochs=10, batch_size=256, verbose=0)
test_loss, test_acc = network.evaluate(test_images, test_labels)
t1=time.time()
print(t1-t0)
print('test_acc:', test_acc)
