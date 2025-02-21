from __future__ import absolute_import, division, print_function

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

#不用Session
tf.enable_eager_execution()
tfe = tf.contrib.eager

#初始化训练数据
train_X = np.asarray([3.3,4.4,5.5,6.71,6.93,4.168,9.779,6.182,7.59,2.167,
                         7.042,10.791,5.313,7.997,5.654,9.27,3.1])
train_Y = np.asarray([1.7,2.76,2.09,3.19,1.694,1.573,3.366,2.596,2.53,1.221,
                         2.827,3.465,1.65,2.904,2.42,2.94,1.3])
#训练数据的数量
n_samples = train_X.shape[0]

#设置学习率，迭代次数，每次迭代包含的数量
lr,num_epochs,batch_size = 0.01,1000,50

W = tf.Variable(np.random.randn(),name='weight')
b = tf.Variable(np.random.randn(),name='bias')

def linear_regression(inputs):
    return inputs*W+b

def mean_square_fn(model_fn,inputs,labels):
    return tf.reduce_sum(tf.pow(model_fn(inputs)-labels,2))/(2*n_samples)

optimizer = tf.train.GradientDescentOptimizer(learning_rate=lr)
grad = tfe.implicit_gradients(mean_square_fn)

#初始化
print("Initial cost= {:.9f}".format(
    mean_square_fn(linear_regression, train_X, train_Y)),
    "W=", W.numpy(), "b=", b.numpy())

#训练
for step in range(num_epochs):

    optimizer.apply_gradients(grad(linear_regression, train_X, train_Y))

    if (step + 1) % batch_size == 0 or step == 0:
        print("Epoch:", '%04d' % (step + 1), "cost=",
              "{:.9f}".format(mean_square_fn(linear_regression, train_X, train_Y)),
              "W=", W.numpy(), "b=", b.numpy())
        
plt.plot(train_X, train_Y, 'ro', label='Original data')
plt.plot(train_X, np.array(W * train_X + b), label='Fitted line')
plt.legend()
plt.show()






