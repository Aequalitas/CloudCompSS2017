import cv2
import numpy as n

X_SIZE = 160
Y_SIZE = 189


# Predicts plant associated with the given image
def calcPlant(model, image):
    pred = model.predict(prepareImg(image))
    print pred
    return pred[0]

def prepareImg(image):

    prepImage = n.zeros(shape=(X_SIZE * Y_SIZE,))
    img = cv2.imdecode(n.fromstring(image.read(), n.uint8), cv2.IMREAD_UNCHANGED)
    res = cv2.resize(img, (Y_SIZE, X_SIZE), interpolation = cv2.INTER_CUBIC)

    print res
    print res.shape

    resC = 0
    for a in range(0, X_SIZE):
            for b in range(0, Y_SIZE):

                print res[a][b]       
                if res[a][b] == 255:
                    prepImage[resC] = 1
                else:
                    prepImage[resC] = 0
                
                resC += 1

    return prepImage
