from keras.datasets import reuters
(train_data,train_labels),(test_data,test_labels) = reuters.load_data(num_words=10000)

#Back to words
word_index = reuters.get_word_index()
reverse_word_index = dict([(value,key) for (key,value) in word_index.items()])
decoded_newswire = ' '.join([reverse_word_index.get(i-3,'?') for i in train_data[0]])


#vectorize data
import numpy as np

def vectorize_sequences(sequences,dimension=10000):
    reults = np.zeros((len(sequences),dimension))
    for i,sequence in enumerate(sequences):
        reults[i,sequence] = 1.
    return reults

x_train = vectorize_sequences(train_data)
x_test = vectorize_sequences(test_data)

def to_one_hot(labels,dimension=46):
    results = np.zeros((len(labels),dimension))
    for i,label in enumerate(labels):
        results[i,label] = 1.
        return results

one_hot_train_labels = to_one_hot(train_labels)
one_hot_test_labels = to_one_hot(test_labels)

from keras.utils.np_utils import to_categorical

one_hot_train_labels = to_categorical(train_labels)
one_hot_test_labels = to_categorical(test_labels)
 
from keras import models
from keras import layers

#model.add(layers.Dropout(0.5))
 
model = models.Sequential()
model.add(layers.Dense(4, activation='relu', input_shape=(10000,)))
model.add(layers.Dense(4, activation='relu'))
model.add(layers.Dense(46, activation='sigmoid'))
 
'''
model = models.Sequential()
model.add(layers.Dense(4, activation='relu', input_shape=(10000,)))
model.add(layers.Dense(4, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))
'''
'''
model = models.Sequential()
model.add(layers.Dense(512, activation='relu', input_shape=(10000,)))
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))
'''

'''
from keras import regularizers

model = models.Sequential()
model.add(layers.Dense(16, kernel_regularizer=regularizers.12(0.001),
                       activation='relu'), input_shape=(10000,)))
model.add(layers.Dense(16, kernel_regularizer=regularizers.12(0.001),
                       activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

'''

model.compile(optimizer='rmsprop',
          loss='categorical_crossentropy',
          metrics=['accuracy'])
 
x_val = x_train[:1000]
partial_x_train = x_train[1000:]
 
y_val = one_hot_train_labels[:1000]
partial_y_train = one_hot_train_labels[1000:]
 
history = model.fit(partial_x_train,
            partial_y_train,
            epochs=20,
            batch_size=512,
            validation_data=(x_val,y_val))
 
import matplotlib.pyplot as plt
 
loss = history.history['loss']
val_loss = history.history['val_loss']
 
epochs = range(1, len(loss)+1)
 
plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
 
plt.show()
 
 #Accuracy

plt.clf()
 
acc = history.history['acc']
val_acc = history.history['val_acc']
 
plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation acc')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
 
plt.show()

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

