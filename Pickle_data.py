###### Création des fichiers Pickle utiles #######
#Python 3.7.1
#Coding Utf-8

"""
Fonction de création des fichiers pickle
@author : Amandine Pinget, PhD
"""

import os
import sys

fileDir = os.path.dirname(os.path.abspath(__file__))
newPath = os.path.join(fileDir, 'Data_recipes')
sys.path.append(newPath)
os.chdir(newPath)

####Import packages
import pandas as pd
import pickle

def pickle_season():
    """
    Création du pickle pour les fruits et légumes de saison
    """
    data = pd.read_csv(r'.\Seasons_Veg_Fruits.csv', sep=';', dtype={'Season':str, 'Fruit_Vegetable': str})
    # print(data)
    pickle.dump(data, open("table_season.pkl", "wb"))

def pickle_season_veg_fruit():
    """
    Création du pickle pour les fruits et légumes de saison -- Ajout de vegetable et fruit
    """
    data = pd.read_csv(r'.\Seasons_Veg_Fruits.csv', sep=';', dtype={'Season':str, 'Fruit_Vegetable': str, 'Fruit': str, 'Vegetable': str} )
    pickle.dump(data, open("table_season_veg_fr.pkl", "wb"))
    print(data)

def main():
    
    # pickle_season()
    pickle_season_veg_fruit()

if __name__ == "__main__":
    main()
