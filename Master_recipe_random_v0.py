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
import random

#Welcome message
print("\n", "Hello Ama, what do you want to cook today?", "\n")

#Import des recettes
with open('recipes_raw_result.json', 'r') as f:
    data = json.load(f)

def fonction_master_cook(data):
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

    def lecture_info_recette(num, data):
        """
        Identification et lecture des infos liées aux recettes
        """
        recipe = {}
        for keys, val in data.items():
            if num == val['RecipeId']:
                recipe = data[keys]
                break
        return recipe

    def print_recette(num, recipe):
        """
        Impression de la recette choisie
        """    
        print("Suggested recipe is : ", recipe['title'])
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
        choice = input("Do you want another recipe? Y/N ")
        print("\n")
        if (choice=='Y' or choice=='y'):
            fonction_master_cook(data)    
        else:
            print("Good bye, see you later ;)", "\n")

    num = choix_recette()
    recipe = lecture_info_recette(num, data)
    print_recette(num, recipe)
    ask_another_recipe()
   

def main():

    fonction_master_cook(data)    

if __name__ == "__main__":
    main()
