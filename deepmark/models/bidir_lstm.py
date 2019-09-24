'''Trains a Bidirectional LSTM on the IMDB sentiment classification task.
Output after 4 epochs on CPU: ~0.8146
Time per epoch on CPU (Core i7): ~150s.
'''

import numpy as np
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Dropout, Embedding, LSTM, Bidirectional
from keras.datasets import imdb

def bidir_lstm():

    #load dataset
    (x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)

    # prepare data
    x_train = sequence.pad_sequences(x_train, maxlen=maxlen)
    x_test = sequence.pad_sequences(x_test, maxlen=maxlen)
    y_train = np.array(y_train)
    y_test = np.array(y_test)

    # define model
    model = Sequential()
    model.add(Embedding(20000, 128, input_length=100))
    model.add(Bidirectional(LSTM(64)))
    model.add(Dropout(0.5))
    model.add(Dense(1, activation='sigmoid'))

    # compile model
    model.compile('adam', 'binary_crossentropy', metrics=['accuracy'])

    # TEST BEGINS
    t0 = time.time()
    model.fit(x_train, y_train,
              batch_size=32,
              epochs=4,
              validation_data=[x_test, y_test], verbose=0)
    t1=time.time()
    # TEST ENDS 

    # evaluate results
    test_loss, test_acc = model.evaluate(x_test, y_test)

    print(t1-t0)
    print('test_acc:', test_acc)
