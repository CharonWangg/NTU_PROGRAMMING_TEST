import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

trainData = pd.read_csv('./question_3/train_data.txt').values
trainLabel = pd.read_csv('./question_3/train_truth.txt').values
testData = pd.read_csv('./question_3/test_data.txt').values
session = tf.Session()

# Standard
scl = StandardScaler()
scl.fit(trainData)
trainData = scl.transform(trainData)
testData = scl.transform(testData)

# division
trainData,validData = train_test_split(trainData,test_size=0.2)
trainLabel,validLabel = train_test_split(trainLabel,test_size=0.2)

# net
hidden_layer_nodes = 4
batchSize = 32
x_data = tf.placeholder(shape=[None,3],dtype=tf.float32)
y_data = tf.placeholder(shape=[None,1],dtype=tf.float32)
A1 = tf.Variable(tf.random_normal(shape=[3,hidden_layer_nodes]))
b1 = tf.Variable(tf.random_normal(shape=[1,hidden_layer_nodes]))
A2 = tf.Variable(tf.random_normal(shape=[hidden_layer_nodes,hidden_layer_nodes]))
b2 = tf.Variable(tf.random_normal(shape=[1,hidden_layer_nodes]))
A3 = tf.Variable(tf.random_normal(shape=[hidden_layer_nodes,1]))
b3 = tf.Variable(tf.random_normal(shape=[1,1]))

hidden_layer_output_1 = tf.sigmoid(tf.add(tf.matmul(x_data,A1),b1))
hidden_layer_output_2 = tf.sigmoid(tf.add(tf.matmul(hidden_layer_output_1,A2),b2))
final_output = tf.sigmoid(tf.add(tf.matmul(hidden_layer_output_2,A3),b3))

loss = tf.reduce_mean(tf.square(y_data-final_output))

optimization = tf.train.GradientDescentOptimizer(0.0005)
opt = optimization.minimize(loss)
session.run(tf.initialize_all_variables())
saver = tf.train.Saver(tf.global_variables(),max_to_keep=1)
saver.save(session,'model',global_step=1000)

trainLoss = []
validLoss = []
step = 50000


for i in range(step):
    index = np.random.choice(len(trainData),size=batchSize)
    x = trainData[index]
    y = trainLabel[index]
    session.run(opt,feed_dict={x_data:x,y_data:y})
    lossRes = session.run(loss,feed_dict={x_data:x,y_data:y})
    trainLoss.append(np.sqrt(lossRes))
    validLoss.append(np.sqrt(session.run(loss,feed_dict={x_data:validData,y_data:validLabel})))
    if (i+1)%100 == 0:
        print('Generation:{},Train_loss:{},Valid_loss:{}'.format(i+1,trainLoss[-1],validLoss[-1]))

testLabel = session.run(final_output,feed_dict={x_data:testData})
pd.DataFrame(testLabel).to_csv('test_predict.csv')
print(testLabel)








