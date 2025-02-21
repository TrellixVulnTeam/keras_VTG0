#有点费资源

from mxnet import gluon,init,nd
from mxnet.gluon import data as gdata,nn
import os
import sys
import Tools

net = nn.Sequential()
net.add(nn.Conv2D(96,kernel_size=11,strides=4,activation='relu'),
        nn.MaxPool2D(pool_size=3,strides=2),
        nn.Conv2D(256,kernel_size=5,padding=2,activation='relu'),
        nn.MaxPool2D(pool_size=3,strides=2),
        nn.Conv2D(384,kernel_size=3,padding=1,activation='relu'),
        nn.Conv2D(384,kernel_size=3,padding=1,activation='relu'),
        nn.Conv2D(384,kernel_size=3,padding=1,activation='relu'),
        nn.MaxPool2D(pool_size=3,strides=2),
        
        
        nn.Dense(4096,activation='relu'),nn.Dropout(0.5),
        nn.Dense(4096,activation='relu'),nn.Dropout(0.5),
        
        nn.Dense(10))

X = nd.random.uniform(shape=(1,1,224,224))
net.initialize()

for layer in net:
    X = layer(X)
    print(layer.name,' shape:',X.shape)
    
batch_size = 128
train_iter,test_iter = Tools.load_data_fashion_mnist(batch_size,resize=224)

lr,num_epochs,ctx = 0.01,5,Tools.try_gpu()
net.initialize(force_reinit=True,ctx=ctx,init=init.Xavier())
trainer = gluon.Trainer(net.collect_params(),'sgd',{'learning_rate':lr})
Tools.train_ch5(net,train_iter,test_iter,batch_size,trainer,ctx,num_epochs)
