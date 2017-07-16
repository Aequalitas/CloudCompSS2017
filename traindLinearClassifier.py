from sklearn import *
from sklearn.multiclass import *

import numpy as n
import pickle as p

import numpy as n
import pickle as p

SAMPLESIZE = 3200
# Both values summarized must not exceed 32
TRAINSAMPLESIZE = 30
TESTSAMPLESIZE = (32 - TRAINSAMPLESIZE)

plants = p.load(open("plants.p", "rb"))

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
for x in range(0, SAMPLESIZE):
    if c >= 32:
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

classifier = linear_model.SGDClassifier(loss="hinge",penalty="none",
                                        learning_rate="constant", eta0=0.0005, n_iter=15)
print "Training data..."
classifier.fit(traind, trainl)
print "Finished training..."


p.dump( classifier, open( "plantsModel.p", "wb" ) )