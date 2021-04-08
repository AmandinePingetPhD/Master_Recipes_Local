#### Master Cook - IA de suggestion de recettes v0 #####
#Python 3.7.1
#Coding Utf-8

"""
Interrogation de la nouvelle base de données Data_recipe
@author : Amandine Pinget, PhD
"""

import os
import sys

fileDir = os.path.dirname(os.path.abspath(__file__))
newPath = os.path.join(fileDir, 'Data_recipes')
sys.path.append(newPath)
os.chdir(newPath)

####Import packages

import json
import pickle
import random
import pandas as pd
import numpy as np
from json.decoder import JSONDecodeError
from collections import Counter

#Import des recettes
with open('recipes_raw_result_season_kaggle.json') as jsonfile:
    try:
        Rawdata = jsonfile.read()
        data = json.loads(Rawdata)
    except JSONDecodeError as e:
        print('Decoding JSON has failed', e)

#Import de la bdd saisonalité des fruits et légumes
global table_season
table_season = pickle.load(open("table_season_veg_fr.pkl", "rb"))
# print(table_season)


for keys in data:
    c = Counter(data[keys]['Season'])
    print(c)

####Similarité des recettes?

### Compter les différentes catégories avec counter : t_recipe
### Idem avec "cold"/"hot"

###Champs non renseignés?