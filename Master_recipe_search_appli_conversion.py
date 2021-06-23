#### Master Cook - IA de suggestion de recettes v1- avec search #####
#Python 3.9.5
#Coding Utf-8

"""
Fonction de suggestion de recettes
@author : Amandine Pinget, PhD
"""

#Initialisation
import os
import sys
import ssl

import pywebio
from pywebio.input import *
from pywebio.output import *
from pywebio import start_server

fileDir = os.path.dirname(os.path.abspath(__file__))
newPath = os.path.join(fileDir, 'Data_recipes')
sys.path.append(newPath)

os.chdir(newPath)
entries = os.listdir(newPath)

#Import des packages
import json
import random
from datetime import date
import re
import pickle
# import pandas as pd
# import numpy as np

#Import des recettes
with open('recipes_raw_result.json', 'r') as f:
    data = json.load(f)

#Import de la table de conversion cup/grammes
global conversion_table
conversion_table = pickle.load(open("conversion_table.pkl", "rb"))

#Date du jour 
today = date.today()

#####Titles
put_markdown('## Welcome to Master Recipes!')

os.chdir(newPath)
img = open('chief1.jpg', 'rb').read() #or 'cook_hat.jpg' / 'chief1.jpg'
put_image(img, width='200px')

# for im in entries:
#     if im.endswith(".jpg"):
#         image = random.choice(entries)
#         img = open(image, 'rb').read()
#         put_image(img, width='200px')
#         break
#     else :
#         continue

#Welcome message : personnalisation avec demande du prénom pour futur programme?
put_text("\n", "Hello Ama, what do you want to cook today?", "\n")



def fonction_master_recipe(data, today):
    """
    Fonction principale 
    """

    def choix_recette():
        """
        Première version avec choix aléatoire de recette suivant ID/numéro de recette
        """
        num = 0
        # Recettes numérotée de 1 à 39517
        num = random.randint(1,39517)
        return num

    def search_recipe(data):
        """
        Recherche de recette par mot clé dans le titre uniquement
        """
        found_recipe = False
        key_words = input("What are you looking for? Please enter a recipe key-word: ")
        
        # Vérifier si la première lettre est en majuscule : sinon : mettre en majuscule
        # Vérifier si tout en majuscule : si c'est cas : mettre juste première lettre
        # Boucle for pour recherche avec des plusieurs mots : "sweet potato"

        key_sep = key_words.split()
        key_w = ''

        for word in key_sep:
            if word.islower()==True:
                key_w += word.capitalize()
            elif word.isupper()==True:
                key_w += word.capitalize()
            else:
                key_w += word
        key_w = re.sub(r"(\w)([A-Z])", r"\1 \2", key_w)

        #Recherche du/des mots-clés dans le titre et impression des recettes résultats
        for keys in data:
            if key_w in data[keys]['title']:
                put_text(data[keys]['RecipeId'], data[keys]['title'])
                found_recipe = True
        put_text("\n")

        #Choix de la recette + impression / message d'erreur si pas trouvé : nouvelle recherche
        if found_recipe == True:
            numero = input("What recipe number do you want?")
            put_text("\n")
            while (numero.isnumeric()!=True or int(numero)>39517):
                numero = input("Recipe number is invalid! Could you please enter another recipe number?")
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
        #Recette identifiée avec composants et mise dans le dictionnaire pour affichage
        for keys in data:
            if num == data[keys]['RecipeId']:
                recipe = data[keys]
                break
        return recipe

    # def read_quantity():
    #     """
    #     Lecture des quantité et transformation en float si fraction
    #     """
    
    # return 

    def print_recette(num, recipe):
        """
        Impression de la recette choisie
        """    
        #Impression titre puis ingrédients avec tirets et instructions
        #Tenir compte du jour pour versions futures au niveau des suggestions
        
        put_text("As today is,",today,", I suggest you : ",recipe['title'])
        put_text("Recipe Number : ", num)
        put_text("\n")
        put_text("Ingredients :")
        for el in recipe['ingredients']:
            put_text("- ", el)
        put_text("\n")
        put_text("Instructions :")
        put_text(recipe['instructions'])
        put_text("\n")

        ##### Export à voir sous un certain format? Modalités? Mail? Historique à garder? 
        #### Carnet de recettes avec historique? Rating si recette testée? A voir...

    def ask_another_recipe():
        """
        Demande si besoin d'une autre recette
        """
        #Boucle et suggère d'autres recettes si besoin sinon exit
        choice = input(" \n Do you want another recipe? Y/N ")
        put_text("\n")
        if (choice=='Y' or choice=='y'):
            fonction_master_recipe(data,today)    
        else:
            put_text("Good bye, see you later ;)", "\n")


    ####Exécution du programme
    
    #Demande si recherche d'ingrédient/recette particulière
    search = input("Do you want to search a special recipe? Y/N ")
    put_text("\n")

    #Si oui: fonction de search
    if (search=='Y' or search=='y'):
        search_recipe(data)
    else:   #Si non: recette choisie au hasard
        num = choix_recette()
        recipe = lecture_info_recette(num, data)
        print_recette(num, recipe)

    #Demande si besoin d'une autre recette : si oui: boucle programme si non: exit 
    ask_another_recipe()
    
    ### Improve print
    ### Rating recipes?
    ### Random choice when special ingredient or ask another complementary?elcome

def main():

    pywebio.start_server(fonction_master_recipe(data, today), port=80)    #AssertionError : application type NoneType

if __name__ == "__main__":
    main()
