# File: calcPlant.py 
# Author: Franz Weidmann
# Description: This file takes the uploaded user image file
# object and transforms it then passes it to 
# the trained model for the prediction process
import cv2
import numpy as n

# fixed size for the images
X_SIZE = 160
Y_SIZE = 189

# Predicts plant associated with the given image
def calcPlant(model, image):
    pred = model.predict(prepareImg(image))
    print pred
    return pred[0]

# transforms the image in resolution and pixel values
def prepareImg(image):

    prepImage = n.zeros(shape=(X_SIZE * Y_SIZE,))
    img = cv2.imdecode(n.fromstring(image.read(), n.uint8), cv2.IMREAD_UNCHANGED)
    res = cv2.resize(img, (Y_SIZE, X_SIZE), interpolation = cv2.INTER_CUBIC)

    resC = 0
    for a in range(0, X_SIZE):
            for b in range(0, Y_SIZE):

                print res[a][b]       
                if res[a][b] == 255:
                    # for every white pixel
                    prepImage[resC] = 1
                else:
                    prepImage[resC] = 0
                
                resC += 1

    return prepImage
