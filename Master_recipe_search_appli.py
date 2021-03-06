#### Master's Recipes - IA de suggestion de recettes v1- avec search #####
#Python 3.9.6
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

#Import des recettes
with open('recipes_data.json', 'r') as f:
    data = json.load(f)

#Date du jour 
today = date.today()

#####Titles
put_markdown("## Welcome to Master's Recipes!")

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



def fonction_master_recipes(data, today):
    """
    Fonction principale 
    """

    def choix_recette():
        """
        Première version avec choix aléatoire de recette suivant ID/numéro de recette
        """
        # Modifier avec demande du type de plat? et tirage aléatoire mais vérif que t-recipe correspond? A voir
        num = 0
        # Recettes numérotée de 1 à 39517
        num = random.randint(1,39517)
        return num

    def search_recipe(data, kind_dish):
        """
        Recherche de recette par mot clé dans le titre uniquement
        """
        found_recipe = False

        # Ajout du type de plat? t_recipe => restreindre le nombre de résultats
        # Demander le type de plat

        # kind_dish = input("What kind of dish go you want to cook? Please provide you choice between: Dish with meat, Dessert, Dessert with fruit, Dish with veggies, Dish with Sea Food/fish, Pasta, Side Dish, Pizza, Drink, Sandwich, Dish with egg, Recipes for dogs")

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

        lres = []
        #Recherche du/des mots-clés dans le titre et impression des recettes résultats
        for keys in data:
            if key_w in data[keys]['title'] and kind_dish == data[keys]['t_recipe']:
                lres.append(data[keys]['RecipeId'])
                put_text(data[keys]['RecipeId'], "-", data[keys]['title'], "-", data[keys]['t_recipe'])
                found_recipe = True
        put_text("\n")

        #Choix aléatoire sur les recettes solution? proposer autre choix sinon si premeir choix aléatoire pas satisfaisant?
        if found_recipe == True:
            alea = input("Do you want a random choice for your recipe? (Y/N)")
            while (alea=='Y' or alea=='y'): #Boucle pour random choice
                num = random.choice(lres)
                recipe, dish_type = lecture_info_recette(num, data)
                print_recette(num, recipe, dish_type)
                alea = input("Do you want another random choice for your recipe? (Y/N)") #autres choix aléatoire? Utile ou pas?
            #Choix de la recette + impression / message d'erreur si pas trouvé : nouvelle recherche
            else :
                numero = input("What recipe number do you want?")
                put_text("\n")
                while (numero.isnumeric()!=True or int(numero)>39517):
                    numero = input("Recipe number is invalid! Could you please enter another recipe number?")
                num = int(numero)
                recipe, dish_type = lecture_info_recette(num, data)
                print_recette(num, recipe, dish_type)
        elif found_recipe == False:
            search = input("\n I'm sorry, I haven't found what you're looking for. Another try? (Y/N) \n")
            if (search=='Y' or search=='y'):
                search_recipe(data, kind_dish)

    def lecture_info_recette(num, data):
        """
        Identification et lecture des infos liées aux recettes
        """
        recipe = {}
        #Recette identifiée avec composants et mise dans le dictionnaire pour affichage
        for keys in data:
            if num == data[keys]['RecipeId']:
                recipe = data[keys]
                dish_type = recipe['t_recipe']# lecture du type de recette
                break
        return recipe, dish_type

    def print_recette(num, recipe, dish_type):
        """
        Impression de la recette choisie
        """    
        #Impression titre puis ingrédients avec tirets et instructions
        #Tenir compte du jour pour versions futures au niveau des suggestions
        
        put_text("As today is,",today,", I suggest you : ", recipe['title'], "-", dish_type)
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
            fonction_master_recipes(data,today)    
        else:
            put_text("Have a nice cooking time and meal! Good bye, see you later ;)", "\n")


    ####Exécution du programme
    
    #Demande si recherche d'ingrédient/recette particulière
    search = input("Do you want to search a special recipe? Y/N ")
    put_text("\n")

    # Demande du type de recette
    kind_dish = input("What kind of dish go you want to cook? Please provide you choice between: Dish with meat, Dessert, Dessert with fruit, Dish with veggies, Dish with Sea Food/fish, Pasta, Side Dish, Pizza, Drink, Sandwich, Dish with egg, Recipes for dogs")


    #Si oui: fonction de search
    if (search=='Y' or search=='y'):
        search_recipe(data, kind_dish)
    else:   #Si non: recette choisie au hasard
        num = choix_recette()
        recipe, dish_type = lecture_info_recette(num, data)
        #test si bon type de recette  == type demandé
        while kind_dish != dish_type:
            num = choix_recette()
            recipe, dish_type = lecture_info_recette(num, data)
        else:
            print_recette(num, recipe, dish_type)

    #Demande si besoin d'une autre recette : si oui: boucle programme si non: exit 
    ask_another_recipe()
    
    ### Improve print
    ### Rating recipes?
    ### Random choice when special ingredient or ask another complementary?

def main():

    pywebio.start_server(fonction_master_recipes(data, today), port=80)    #AssertionError : application type NoneType

if __name__ == "__main__":
    main()
