#### Master Cook - IA de suggestion de recettes v1- with search #####
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


def fonction_master_cook(data, today):
    """
    Fonction principale 
    """

    def choix_recette():
        """
        Première version avec choix aléatoire de recette suivant ID/numéro de recette
        """
        num = 0
        num = random.randint(1,39517)
        return num

    def search_recipe(data):
        """
        Recherche de recette par mot clé dans le titre uniquement
        """
        found_recipe = False
        key_w = input("What are you looking for? Please enter a recipe key-word: ")
        ###Check if 1st letter in capital / if not: capitalize
        if key_w.islower()==True:
            key_w = key_w.capitalize()

        for keys in data:
            if key_w in data[keys]['title']:
                print(data[keys]['RecipeId'], data[keys]['title'])
                found_recipe = True
        print("\n")
        if found_recipe == True:
            numero = input("What recipe number do you want?")
            print("\n")
            
            num = int(numero)
            recipe = lecture_info_recette(num, data)
            print_recette(num, recipe)

        elif found_recipe == False:
            search = input("\n I'm sorry, I haven't found what you're looking for. Another try? (Y/N) \n")
            if (search=='Y' or search=='y'):
                search_recipe(data)

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

    def print_recette(num, recipe):
        """
        Impression de la recette choisie
        """    
        print("As today is,",today,", I suggest you : ",recipe['title'])
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
        num = choix_recette()
        recipe = lecture_info_recette(num, data)
        print_recette(num, recipe)
    ask_another_recipe()
   

def main():

    fonction_master_cook(data, today)    

if __name__ == "__main__":
    main()
