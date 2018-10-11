
import time
import tensorflow as tf
import keras
from keras.backend.tensorflow_backend import set_session
gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.5)
gpu_options.allow_growth = True
gpu_options.force_gpu_compatible = True
sess = tf.Session(config=tf.ConfigProto(inter_op_parallelism_threads = 64,
        gpu_options=gpu_options))
from keras.datasets import mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
from keras import models
from keras import layers
network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
network.add(layers.Dense(10, activation='softmax'))
network.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])
train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255
from keras.utils import to_categorical
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)
t0 = time.time()
network.fit(train_images, train_labels, epochs=10, batch_size=256, verbose=0)
test_loss, test_acc = network.evaluate(test_images, test_labels)
t1=time.time()
print(t1-t0)
print('test_acc:', test_acc)


