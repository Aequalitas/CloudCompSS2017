import gzip
import urllib2
import pickle as p
import calcPlant as cP
from flask import Flask as f, request as req, render_template as rT

app = f(__name__)

PLANTS = ["Acer_Campestre", "Ilex_Aquifolium", "Quercus_Ilex", "Acer_Capillipes",	
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

@app.route("/")
def mainPage():
        return rT("index.html")

@app.route("/", methods=["POST"])
def calcPlant():
        msg = None

        if 'file' in req.files:
            file = req.files['file']
            if file.filename != '':
                msg = "This leaf belongs to the %s" % PLANTS[cP.calcPlant(MODEL, file)]
            else:
                msg = "No file selected"
        else:
            msg = "No file part"

        return rT("index.html", cp=msg)


print "Server started..."

# fetch trained model once
def fetchModel():
    response = urllib2.urlopen('https://github.com/Aequalitas/CloudCompSS2017/blob/master/plantsModel.p.gz?raw=true/')
    gzipFile = open("modelTmp.gzip", "w")
    gzipFile.write(response.read())

    with gzip.open("modelTmp.gzip", "rb") as pl:
        gzipFile.close()
        f = open("modelTmp.txt", "w")
        f.write(pl.read())
        f.close()
        return p.load(open("modelTmp.txt", "rb"))


# trained model
MODEL = fetchModel()