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

fruit = ["Fruit", "hazelnut", "walnut", "chestnut", "grapefruit", 
            "lemon", "orange", "tangerine", "apricot", "mango",
            "pineapple", "rhubarb", "strawberry", "blackberry",
            "cherry", "blueberry", "nectarine", "peach", "plum",
            "rasperry", "watermelon", "apple", "cranberry", "fig",
            "grape", "pear", "pomegranate", "quince", "banana", "kiwi"]

vegetable = ["Vegetable", "kale", "leek", "radicchio", "radish", "rutabaga", 
            "turnip", "brussel sprout", "beetroot", "red cabbage",
            "avocado", "artichoke", "asparagus", "spinach", "carrot",
            "pepperoni", "celeriac", "chive", "collard", "pea", "fava bean", 
            "fennel", "fiddlehead", "morel", "mustard", "eggplant",
            "tomato", "corn", "broccoli", "cucumber", "green bean", "zucchini",
            "celery", "butternut", "cauliflower", "galic", "mushroom", 
            "potato", "pumpkin", "sweet potato", "swiss chard", "chicory",
            "pak choi", "onion", "salad"]

def classification_recipe(data, table_season, fruit, vegetable):
    """
    Fonction de classification par saison des recettes 
    """

    # interrogation de la base de données recette :
    # passage en revue de chaque recette au niveau des ingrédients
    # si fruit et légumes id à base table_season : recette de la saison des fruits/légumes
    # écrire la saison dans le fichier JSON
    #    'Fruit': str, 'Vegetable': str})
   
    meat = ["Chicken", "Beef", "Turkey", "Meetloaf"]
    # egg = ["Egg"] ####To improve
    # fish = ["fish", "Seafood", "Salmon", "Shrink" ] #####To improve
    # drink = ["water", "juice"]
    dessert = ["Creme", "Chocolate", "Granola", "Brownies",
                 "Cookie","Cookies", "Pancakes", "Bread", "Muffins", "Waffles", 
                 "Biscuits", "Pie", "Crepes", "Pudding","Cheesecake", "Cake", "Bars"]
                 
    # p = inflect.engine() ####Singular/plural

    for keys in data:
        list1 =[i for item in [data[keys]["title"]] for i in item.split()]
        list2 = set(list1)&set(fruit) # we don't need to list3 to actually be a list
        list4 = sorted(list2, key = lambda k : list1.index(k))

        if len(list4)!=0:
            data[keys].update({"t_recipe": "Dessert with fruit"})
        else:
            list3 = set(list1)&set(dessert)
            list5 = sorted(list3, key = lambda k : list1.index(k))
            if len(list5)!=0:
                data[keys].update({"t_recipe": "Dessert"})
            else:
                list6 = set(list1)&set(vegetable)
                list7 = sorted(list6, key = lambda k : list1.index(k))
                if len(list7)!=0:
                    data[keys].update({"t_recipe": "Dish with veggies"})
                else:
                    list8 = set(list1)&set(meat)
                    list9 = sorted(list8, key = lambda k : list1.index(k))
                    if len(list9)!=0:
                        data[keys].update({"t_recipe": "Dish with meat"})
                    else:
                        data[keys].update({"t_recipe": "Unknown"})
                        ####Fish
        
        sys.stdout = open("list_recipe2.txt", "a")
        print(data[keys]['title'], data[keys]['RecipeId'], data[keys]['t_recipe'])
    sys.stdout.close()

    # ####classif chaud / froid
    ### : "hot", "oven", "bake"
    ### : "cold", "cool", "fridge"

    jsonfile.close()

    ####Export des données modifiées
    with open('recipes_raw_result_classif2.json', 'w') as outfile:
        json.dump(data, outfile)
    outfile.close()


def main():

    classification_recipe(data, table_season, fruit, vegetable)    

if __name__ == "__main__":
    main()
