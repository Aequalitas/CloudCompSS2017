import pickle as p
import numpy as n
import gzip
import urllib2


response = urllib2.urlopen('https://github.com/Aequalitas/CloudCompSS2017/blob/master/plantsModel.p.gz?raw=true/')
gzipFile = 
#modelData = response.read()

# with gzip.open(modelData) as pl:
#      model = p.load(pl)

gunzip_response = gzip.GzipFile(fileobj=response)
model = p.load(gunzip_response)

pred = model.predict(n.zeros(shape=(160*189)))
print pred
#return pred[0]