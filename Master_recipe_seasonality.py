#### Master Cook - IA de suggestion de recettes v0 #####
#Python 3.7.1
#Coding Utf-8

"""
Fonction de suggestion de recettes
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
from datetime import date
# import pandas as pd
# import numpy as np

#Welcome message
today = date.today()
print("\n", "Hello Ama, what do you want to cook today?", "\n")

#Import des recettes
with open('recipes_raw_result.json', 'r') as f: ####bonne db à importer
    data = json.load(f)

#Import de la bdd saisonalité des fruits et légumes
# global table_season
# table_season = pickle.load(open("table_season.pkl", "rb"))
# print(table_season)


def fonction_master_cook(data, today):
    """
    Fonction principale 
    """

    def seasonality(today):
        """
        Prise en compte de la date du jour et de la saison pour la suggestion de recette
        """
        #today de la forme 2021-03-11
        thisYear = today.year

        #Def des saisons
        seasons =  [('winter', (date(thisYear, 1, 1), date(thisYear, 3, 20))),
                    ('spring', (date(thisYear, 3, 21), date(thisYear, 6, 20))),
                    ('summer', (date(thisYear, 6, 21), date(thisYear, 9, 20))),
                    ('autumn', (date(thisYear, 9, 21), date(thisYear, 12, 20))),
                    ('winter', (date(thisYear, 12, 21), date(thisYear, 12, 31)))]

        current_season = next(season for season, (start, end) in seasons if start <= today <= end)

        return current_season
       

    def choix_recette():
        """
        Première version avec choix aléatoire de recette suivant ID/numéro de recette
        """
        num = 0
        num = random.randint(1,39517)
        return num

    # def check_seasonality(table_season, current_season, recipe): To improve : voir comment gérer
        # ###Check avec 'Season' de la recette si all season : ok sinon comparaison de saison
        # """
        # Vérification si la recette est de saison
        # """
        # for el in recipe['ingredients']:
        #     for subelem in el:
        #         search = table_season.query('Fruit_Vegetable==@subelem')
                # if search not null:
                #     result = search['Season']
                #     if result == current_season:
                #         continue
                #     else:
                #         num=choix_recette()
                # else:
                #     continue
            #check si dans table season :
            #si présent : check si meme saison si oui suivant
            #si non : cherche une autre recette au hasard
            #si absent : passe à l'ingrédient suivant

     #choix d'une recette au hasard puis check si ingrédients de saison 
        ## si oui : impression de la recette
        ## si non : ingrédient hors saison : cherche une autre recette
        
        #interrogation de la base de données recette :
        # passage en revue de chaque recette au niveau des ingrédients
        # si fruit et légumes id à base table_season : recette de la saison des fruits/légumes
        # écrire la saison dans le fichier JSON?

        #choix d'une recette au hasard puis check si ingrédients de saison 
        ## si oui : impression de la recette
        ## si non : ingrédient hors saison : cherche une autre recette

    def search_recipe(data):
        """
        Recherche de recette par mot clé
        """
        found_recipe = False
        key_w = input("What are you looking for? Please enter a recipe key-word: ")
        for keys in data:
            if key_w in data[keys]['title']:
                print(data[keys]['title'])
                found_recipe = True
                # print(data[keys])
        if found_recipe == False:
            search = input("\n", "I'm sorry, I haven't found what you're looking for. Another try? (Y/N)", "\n")
            if (search=='Y' or search=='y'):
                search_recipe(data)
        #     else:
        #         print("Good bye, see you later ;)", "\n")
        ### Impression + export éventuel à améliorer

    def lecture_info_recette(num, data):
        """
        Identification et lecture des infos liées aux recettes
        """
        recipe = {}
        for keys in data:
            if num == data[keys]['RecipeId']:
                recipe = data[keys]
                break
        return recipe

    def print_recette(num, recipe, current_season):
        """
        Impression de la recette choisie
        """    
        print("As today is,",today,", I suggest you a",current_season,"recipe : ",recipe['title'])
        print("Recipe Number : ", num)
        print("\n")
        print("Ingredients :")
        for el in recipe['ingredients']:
            print("- ", el)
        print("\n")
        print("Instructions :")
        print(recipe['instructions'])
        print("\n")

    def ask_another_recipe():
        """
        Demande si besoin d'une autre recette
        """
        choice = input(" \n Do you want another recipe? Y/N ")
        print("\n")
        if (choice=='Y' or choice=='y'):
            fonction_master_cook(data,today)    
        else:
            print("Good bye, see you later ;)", "\n")

    search = input("Do you want to search a special recipe? Y/N ")
    print("\n")
    if (search=='Y' or search=='y'):
        search_recipe(data)
    else:   
        current_season = seasonality(today)
        num = choix_recette()
        recipe = lecture_info_recette(num, data)
        # check_seasonality(table_season, current_season, recipe)
        print_recette(num, recipe, current_season)
    ask_another_recipe()
   

def main():

    fonction_master_cook(data, today)    

if __name__ == "__main__":
    main()
