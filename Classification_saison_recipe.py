#### Master Cook - IA de suggestion de recettes v0 #####
#Python 3.7.1
#Coding Utf-8

"""
Fonction de classification des recettes par saison
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
import inflect

#Import des recettes
with open('recipes_raw_result.json') as jsonfile:
    try:
        Rawdata = jsonfile.read()
        data = json.loads(Rawdata)
    except JSONDecodeError as e:
        print('Decoding JSON has failed', e)

#Import de la bdd saisonalité des fruits et légumes
global table_season
table_season = pickle.load(open("table_season_veg_fr.pkl", "rb"))
# print(table_season)

def classification_recipe(data, table_season):
    """
    Fonction de classification par saison des recettes 
    """

    # interrogation de la base de données recette :
    # passage en revue de chaque recette au niveau des ingrédients
    # si fruit et légumes id à base table_season : recette de la saison des fruits/légumes
    # écrire la saison dans le fichier JSON
    #    'Fruit': str, 'Vegetable': str})
   
    p = inflect.engine()

    for keys in data:
        for el in data[keys]['ingredients']:
            new = el.split()
            for subelem in  new :
                subel = p.singular_noun(subelem)
                if subel == False:
                    subel = subelem
                # search = table_season["Fruit_vegetable"].str.find(subelem, start=0)
                search = table_season.query('Fruit_vegetable==@subel')
                # print(search)
                if not search.empty:  #Add season when fruit/veg match season 
                    # print(search)
                    result = search['Season']
                    data[keys].update({'Season' : result})
                    ### si fruit ou 'sugar' ou 'chocolate' : dessert
                    ## si legume ou 'salt' ou 'chicken'...: dish
                    ## si 'drink ' : drink ##

                else:
                    data[keys].update({'Season' : 'all season'})
        print(data[keys]['RecipeId'], data[keys]['Season'])

####classif chaud / froid
### : "hot", "oven", "bake"
### : "cold", "cool", "fridge"


####Export des données modifiées
with open('recipes_raw_result_season.json', 'w') as outfile:
    json.dump(data, outfile)

def main():

    classification_recipe(data, table_season)    

if __name__ == "__main__":
    main()
