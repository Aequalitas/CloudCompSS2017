import tensorflow as tf
import numpy as n
import pickle as p

# Both values summarized must not exceed 16
TRAINSAMPLESIZE = 14
TESTSAMPLESIZE = (16 - TRAINSAMPLESIZE)

plants = p.load(open("plants.p", "rb"))
print plants[0].shape
print plants[1].shape
print plants[0].sum()
print plants[1].sum()


d = plants[0]
l = n.argmax(plants[1], axis=1)

# traindata
traind = n.ndarray(shape=(TRAINSAMPLESIZE*100, plants[0].shape[1]), dtype=int)
trainl = n.ndarray(shape=(TRAINSAMPLESIZE*100), dtype=int)

# testdata
testd = n.ndarray(shape=(TESTSAMPLESIZE * 100, plants[0].shape[1]), dtype=int)
testl = n.ndarray(shape=(TESTSAMPLESIZE * 100), dtype=int)

#counter to be able to split
c = 0
cTr= 0
cTe = 0
# distribute data into train and test data
print "Splitting data..."
for x in range(0, 1600):
    if c >= 16:
        c = 0
    
    if TRAINSAMPLESIZE - c > 0:
        traind[cTr] = d[x]
        trainl[cTr] = l[x]
        cTr = cTr + 1
    else:
        testd[cTe] = d[x]
        testl[cTe] = l[x]
        cTe = cTe + 1

    c = c + 1

print "Finished with splitting data..."

print traind[0]
print traind[0].sum()
print trainl.sum()




x = tf.placeholder(tf.float32, [1600, 160*189])

#weigth
W = tf.Variable(tf.zeros([1600, 100]))
#bias
b = tf.Variable(tf.zeros([100]))


y = tf.nn.softmax(tf.matmul(x, W) + b)
y_ = tf.placeholder(tf.float32, [None, 100])
# loss function
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

train_step = tf.train.GradientDescentOptimizer(0.05).minimize(cross_entropy)

# train 1000 times
for x in range(1000):
    sess.run(train_step, feed_dict={x: traind, y_: trainl})

#evaluation
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print(sess.run(accuracy, feed_dict={x: testd, y_: testd}))
