#### Master's Recipes - IA de suggestion de recettes v1- avec search #####
#Python 3.8.6
#Coding Utf-8

"""
Fonction de suggestion de recettes
@author : Amandine Pinget, PhD
"""

#Initialisation
import os
import sys
fileDir = os.path.dirname(os.path.abspath(__file__))
newPath = os.path.join(fileDir, 'Data_recipes')
sys.path.append(newPath)
os.chdir(newPath)

#Import des packages
import json
import random
from datetime import date
import re
import pickle
import nltk
# import math
from fractions import Fraction
# import pandas
# import numpy

#Import des recettes
with open('recipes_data.json', 'r') as f:
    data = json.load(f)

#Import de la table de conversion cup/grammes
global conversion_table
conversion_table = pickle.load(open("conversion_table.pkl", "rb"))
# print(conversion_table)


#Date du jour 
date_j = date.today()

#Welcome message : personnalisation avec demande du prénom pour futur programme?
print("\n", "Hello Ama, what do you want to cook today?", "\n")



def fonction_master_recipes(data, date_j):
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
                print(data[keys]['RecipeId'], data[keys]['title'])
                found_recipe = True
        print("\n")

        #Choix de la recette + impression / message d'erreur si pas trouvé : nouvelle recherche
        if found_recipe == True:
            numero = input("What recipe number do you want? ")
            print("\n")
            while (numero.isnumeric()!=True or int(numero)>39517):
                numero = input("Recipe number is invalid! Could you please enter another recipe number?")
            num = int(numero)
            recipe = lecture_info_recette(num, data)
            ###Demander si conversion à réaliser ou pas? 
            convers = input("Do you prefer ingredients in metric units (grams,...)? Y/N ")
            print("\n")
            if (convers=='Y' or convers=='y'):
                print("Ingredients will be converted in metric units.", "\n")
                #### fonction de conversion 
                recipe = conversion_metric(recipe)
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


    def conversion_metric(recipe):
        """
        Fonction de conversion des cup/ounces...en grammes 
        """
    #     # Boucle sur les ingrédients? 
    #     # si unknown => pas de conversion mais identique 
    #     conversion_table
    # si nombre + fraction : calcul à faire
    # si contenu paquet + unité entre parenthèses : négliger premier nombre?
    # si unité à convertir : conversion sinon ignorer ne pas changer les quantités?
    # considérer les unités au singulier? "cup" au lieu de "cups"
    # catégories liquide pour cup: "milk", "water"
    # impression de la recette au fur et à mesure des conversions

        for el in recipe['ingredients']:
            tokens = nltk.word_tokenize(el)
            j = 0
            quant = []
            for j in range(len(tokens)): #int ou float : quantité
                try:
                    float(tokens[j])
                    quant.append(float(tokens[j]))
                    print(quant) #stockage sous forme de string
                except ValueError:
                    if tokens[j] == '(': ### introduire si '(' et ')' avec nombre et unité 
                        try:
                            quant = [] #: négliger le premier nombre : supprimer de quant
                        except ValueError:
                            continue
                    else: #si fraction : calcul et float en résultat
                        values = tokens[j].split('/')
                        if len(values) == 2 and all(i.isdigit() for i in values) :
                            resultat = float(Fraction(int(values[0]), int(values[1])))
                            quant.append(resultat) # append float 
                            print (values, resultat, quant)
                            res = 0
                            res = sum(quant)
                            print(res)
        
    # recherche sur unités + ingrédients à convertir? => correspondance avec conversion_table
    # Différents cas : int, fraction, texte

    # Return : recette avec quantités + unités modifiées
        return recipe

    
    def print_recette(num, recipe):
        """
        Impression de la recette choisie
        """    
        #Impression titre puis ingrédients avec tirets et instructions
        #Tenir compte du jour pour versions futures au niveau des suggestions


        today = f'{date_j:%d/%m/%Y}'


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

        ##### Export à voir sous un certain format? Modalités? Mail? Historique à garder? 
        #### Carnet de recettes avec historique? Rating si recette testée? A voir...

    def ask_another_recipe():
        """
        Demande si besoin d'une autre recette
        """
        #Boucle et suggère d'autres recettes si besoin sinon exit
        choice = input(" \n Do you want another recipe? Y/N ")
        print("\n")
        if (choice=='Y' or choice=='y'):
            fonction_master_recipes(data,date_j)    
        else:
            print("Have a nice cooking time and meal! Good bye, see you later ;)", "\n")


    ####Exécution du programme
    
    #Demande si recherche d'ingrédient/recette particulière
    search = input("Do you want to search a special recipe? Y/N ")
    print("\n")

    #Si oui: fonction de search
    if (search=='Y' or search=='y'):
        search_recipe(data)
    else:   #Si non: recette choisie au hasard
        num = choix_recette()
        recipe = lecture_info_recette(num, data)
        ###Demander si conversion à réaliser ou pas? 
        convers = input("Do you prefer ingredients in metric units (grams,...)? Y/N ")
        print("\n")
        if (convers=='Y' or convers=='y'):
            print("Ingredients will be converted in metric units.", "\n")
            #### fonction de conversion 
            recipe = conversion_metric(recipe)
        print_recette(num, recipe)

    #Demande si besoin d'une autre recette : si oui: boucle programme si non: exit 
    ask_another_recipe()
   

def main():

    fonction_master_recipes(data, date_j)    

if __name__ == "__main__":
    main()
