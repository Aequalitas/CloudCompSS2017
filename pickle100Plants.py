# File: pickle100Plants.py 
# Author: Franz Weidmann
# Description: This file takes every image
# and transforms, scale it and finaly serialize
# it with pickle
import cv2
import numpy as n
import pickle as p
from sklearn import preprocessing
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# fixed size for the images
X_SIZE = 160
Y_SIZE = 189

# create image array which contains the new images
# training data
images = n.array([], n.int32)
images.resize((3200, X_SIZE * Y_SIZE, 3))

# create the target data array
targetData = n.array([])
targetData.resize((3200, 100))

# list of plant names to walk through every folder and get the images
plants = ["Acer_Campestre", "Ilex_Aquifolium", "Quercus_Ilex", "Acer_Capillipes",	
"Ilex_Cornuta"	,	   "Quercus_Imbricaria",
"Acer_Circinatum",	"Liquidambar_Styraciflua", "Quercus_Infectoria_sub",
"Acer_Mono", "Liriodendron_Tulipifera", "Quercus_Kewensis",
"Acer_Opalus", "Lithocarpus_Cleistocarpus", "Quercus_Nigra",
"Acer_Palmatum", "Lithocarpus_Edulis", "Quercus_Palustris",
"Acer_Pictum", "Magnolia_Heptapeta", "Quercus_Phellos",
"Acer_Platanoids",		"Magnolia_Salicifolia",	   "Quercus_Phillyraeoides",
"Acer_Rubrum",		"Morus_Nigra",		   "Quercus_Pontica",
"Acer_Rufinerve",		"Olea_Europaea"	,	   "Quercus_Pubescens",
"Acer_Saccharinum",	"Phildelphus"		,   "Quercus_Pyrenaica",
"Alnus_Cordata"	,	"Quercus_Rhysophylla",
"Alnus_Maximowiczii",	"populus_adenopoda"	,   "Quercus_Rubra",
"Alnus_Rubra"	,	"populus_grandidentata"	,   "quercus_semecarpifolia",
"Alnus_Sieboldiana",	"Populus_Nigra"	,	   "Quercus_Shumardii",
"Alnus_Viridis"	,	"Prunus_Avium"	,	   "Quercus_Suber",
"arundinaria_simonii",	"Prunus_X_Shmittii"	  , "Quercus_Texana",
"Betula_Austrosinensis"	,"Pterocarya_Stenoptera",	   "quercus_trojana",
"Betula_Pendula"	,	"quercus_afares"	,	   "quercus_variabilis",
"callicarpa_bodinieri",	"Quercus_Agrifolia"	  , "Quercus_Vulcanica",
"Castanea_Sativa"	,	"quercus_alnifolia",	   "Quercus_x_Hispanica",
"celtis_koraiensis",	"Quercus_Brantii"		,   "quercus_x_turneri",
"cercis_siliquastrum",	"Quercus_Canariensis",	   "Rhododendron_x_Russellianum",
"Cornus_Chinensis",	"Quercus_Castaneifolia"	 ,  "salix_fragilis",
"cornus_controversa",	"quercus_cerris"	,	   "Salix_Intergra",
"Cornus_Macrophylla",	"quercus_chrysolepis",	   "sorbus_aria",
"cotinus_coggygria",	"Quercus_Coccifera"	  , "Tilia_Oliveri",
"crataegus_monogyna",	"quercus_coccinea",	   "Tilia_Platyphyllos",
"Cytisus_Battandieri"	,"quercus_crassifolia"	,   "tilia_tomentosa",
"Eucalyptus_Glaucescens",	"Quercus_Crassipes"	 ,  "Ulmus_Bergmanniana",
"eucalyptus_neglecta"	,"quercus_dolicholepis"	 ,  "Viburnum_Tinus",
"Eucalyptus_Urnigera"	,"Quercus_Ellipsoidalis"	,   "viburnum_x_rhytidophylloides",
"Fagus_Sylvatica"		,"Quercus_Greggii"	,	   "Zelkova_Serrata",
"ginkgo_biloba"		,"quercus_hartwissiana"
]

print "Creating targetdata"

tarC = 0
for x in range(0, 100):
    for i in range(0, 32):
        targetData[tarC][x] = 1 
        tarC += 1

print "Finished reading targetData"

# save all images with one value for 1 or 0 instead the three values of rgbs
# flatten it to a one dimensional array for the machine learning algorithm
c = 0
for x in plants:
    for i in range(1, 33):
        ii = ""
        if i < 10 :
            ii = "0"
        
        if 17 - i > 0:
            path = "../data/%s/%s_%s%d.ab.jpg" % (x,x,ii,i)
        else:
            iii = i-16
            if ( iii < 10):
                ii = "0"
            path = "../data/%s/%s_%s%d.ab.jpg.flop.jpg" % (x,x,ii,i-16)

        #print "Reading %s..." % path
        img = cv2.imread(path)
        res = cv2.resize(img, (Y_SIZE, X_SIZE), interpolation = cv2.INTER_CUBIC)

        resC = 0
        for a in range(0, X_SIZE):
                for b in range(0, Y_SIZE):
                    if res[a][b][0] == 255:
                        # if the pixel is white
                        images[c][resC] = 1
                    else:
                        images[c][resC] = 0

                    
                    resC += 1

        c += 1
        print "Image %d finished" % c

print "Finished reading images"
print images.sum()

# feature scaling
images = preprocessing.scale(images)

export = [images, targetData]

p.dump( export, open( "plants.p", "wb" ) )