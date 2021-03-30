#### Master Cook - IA de suggestion de recettes v0 #####
#Python 3.7.1
#Coding Utf-8

"""
Modifications de la base de données recette
@author : Amandine Pinget, PhD
"""
####Import packages
import os
import sys
import json
from json.decoder import JSONDecodeError

fileDir = os.path.dirname(os.path.abspath(__file__))
newPath = os.path.join(fileDir, 'Data_recipes')
sys.path.append(newPath)
os.chdir(newPath)

with open('recipes_raw_clean2.json') as jsonfile:
    try:
        Rawdata = jsonfile.read()
        data = json.loads(Rawdata)
    except JSONDecodeError as e:
        print('Decoding JSON has failed', e)

    n = 1
    for keys in data:
        data[keys].update({'RecipeId': n})
        n += 1
    ####Ajout du numéro de recette n+=1 qui s'incrémente dans RecipeId

with open('recipes_raw_result.json', 'w') as outfile:
    json.dump(data, outfile)

###Nouvelle base source recipe_raw_result 

###Il faut modifier les clés des recettes tel que clé==RecipeId ##A voir


