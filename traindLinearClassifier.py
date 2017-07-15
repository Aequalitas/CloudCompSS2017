from sklearn import *
from sklearn.multiclass import *
import sklearn.neural_network as nn
from sklearn.tree import DecisionTreeClassifier

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


print "LINEAR LEARNING with stochastic gradient descent and hinge loss:"

classifier = linear_model.SGDClassifier(loss="hinge",penalty="none",
learning_rate="constant", eta0=0.001, n_iter=5)
print "Training data..."
classifier.fit(traind, trainl)
print "Finished training..."


p.dump( classifier, open( "plantsModel.p", "wb" ) )

# pred = classifier.predict(testd)

# print "Rightly chosen samples : %d from %d samples" % ((pred == testl).sum(), testl.shape[0])
# #print "Accuracy: %f%%" % (testl.shape[0] / (pred == testl).sum() )


# print "NEURONAL NETWORK:"
# clf = nn.MLPClassifier(solver="lbfgs", alpha=1e-5,
#                        hidden_layer_sizes=(80),
#                        random_state=1, early_stopping=False,
#                        max_iter=120, verbose=False)

# print "Fitting..."
# clf.fit(traind, trainl)
# print "Finished fitting..."

# pred = clf.predict(testd)

# print "Rightly chosen samples : %d from %d samples" % ((pred == testl).sum(), testl.shape[0])
# #print "Accuracy: %f%%" % (testl.shape[0] / (pred == testl).sum() )

# print "DECISIONTREE:"

# dtc = DecisionTreeClassifier(max_depth=5)


# print "Fitting..."
# dtc.fit(traind, trainl)
# print "Finished fitting..."

# pred = dtc.predict(testd)

# print "Rightly chosen samples : %d from %d samples" % ((pred == testl).sum(), testl.shape[0])
# #print "Accuracy: %f%%" % (testl.shape[0] / (pred == testl).sum() )
