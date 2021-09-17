#### Master Cook - IA de suggestion de recettes v0 #####
#Python 3.9.6
#Coding Utf-8

"""
Fonction de classification des recettes par saison et autre
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
# import pickle
import re
# import pandas as pd
# import numpy as np
from json.decoder import JSONDecodeError
#import inflect #Sing/plur only

#Import des recettes
with open('recipes_raw_result.json') as jsonfile:
    try:
        Rawdata = jsonfile.read()
        data = json.loads(Rawdata)
    except JSONDecodeError as e:
        print('Decoding JSON has failed', e)
####Voir si pgm ok et cause du temps mis à exec

def classification_recipe(data):
    """
    Fonction de classification par type de recettes 
    """

    #Plusieurs classifications/caractérisation des recettes à effectuer:
    ## - type de plat : salé, sucré, boisson
    ## - contenu : végétarien, viande, poisson, fruits...
    ## - chaud/froid
    ## - saison : printemps, été, automne, hiver 

    # interrogation de la base de données recette :
    # passage en revue de chaque recette au niveau du titre/des ingrédients
    # si fruit et légumes id à base table_season : recette de la saison des fruits/légumes
    # écrire la saison dans le fichier JSON

    
    fruit = ['fruit', 'hazelnuts', 'walnuts', 'chestnuts', 'grapefruit', 'lemon', 'orange', 
            'tangerine', 'apricot', 'mango', 'pineapple', 'rhubarb', 'strawberry', 'strawberries',
            'blackberry', 'cherry', 'blueberry', 'nectarine', 'peach', 'plum', 'raspberry', 
            'watermelon', 'apple', 'apples', 'cranberry', 'fig', 'grape', 'pear', 'pomegranate',
            'quince', 'quinces', 'banana', 'bananas', 'kiwi', 'berry', 'applesauce', 'almond', 
            'almonds', 'coconut', 'pecans', 'peaches', 'grapes', 'blueberries']

    vegetable = ['vegetable', 'kale', 'leek', 'radicchio', 'radish', 'rutabaga', 'turnip', 'sprouts', 
                'beetroot', 'red cabbage', 'avocado', 'artichoke', 'asparagus', 'spinach', 'carrot', 
                'carrots', 'pepperoni', 'celeriac', 'chive', 'collard', 'pea', 'fava bean', 'fennel', 
                'fiddlehead', 'morel', 'mustard', 'eggplant', 'tomato', 'tomatoes', 'corn', 'broccoli', 
                'cucumber', 'cucumbers', 'bean', 'beans', 'zucchini', 'celery', 'butternut', 'cauliflower', 
                'garlic', 'mushroom', 'mushrooms', 'potato', 'potatoes', 'pumpkin', 'sweet potato', 'chard', 
                'chicory', 'pak choi', 'onion', 'salad', 'guacamole', 'veggie', 'rice', 'peppers', 'lentil', 
                'hummus', 'lettuce', 'vegetables', 'vegetarian', 'veggies', 'fries', 'cabbage', 'ratatouille', 
                'squash', 'orzo', 'beets', 'quinoa', 'gazpacho', 'soup', 'dahl', 'blt', 'minestrone', 'colcannon', 
                'slaw', 'chickpea', 'romaine', 'coleslaw', 'peas', 'horseradish', 'okra', 'edamame', 'artichokes',
                'kohlrabi', 'beet', 'beets', 'radishes', 'onions', 'yam', 'tempeh', 'plantains', 'plantain', 'fiddleheads']
   
    meat = ['chicken', 'chicken-rotisserie', 'beef', 'turkey', 'rib', 'ribs', 'meatloaf', 'meatloaves', 'meatball',
            'meatballs', 'lamb', 'meat', 'pork', 'pig', 'steak', 'steaks', 'quail', 'rabbit', 'poultry', 
            'sausage', 'sirloin', 'bacon', 'filet', 'pollo', 'scallops', 'chili', 'taco', 'enchiladas', 
            'jambalaya', 'goulash', 'carne', 'stew', 'ham', 'wings', 'osso', 'roast', 'sloppy', 'mahi', 
            'duck', 'brisket', 'prosciutto', 'casserole', 'cooker', 'quiche', 'dumplings', 'gravy', 'moussaka']

    egg = ['egg', 'eggs', 'omelet']

    fish = ['fish', 'seafood', 'salmon', 'shrink', 'cod', 'halibut', 'trout', 'crab', 'crabs', 'tilapia', 'shrimp', 
            'tuna', 'shells', 'clam', 'crabby', 'lobster', 'oysters', 'prawns', 'mussels', 'haddock', 'sea', 'clams', 
            'crawfish']

    drink = ['water', 'juice', 'tea', 'lemonade', 'sangria', 'punch', 'cocoa', 'beer', 'eggnog', 'grog', 'shake',
             'margarita', 'margaritas', 'smoothie', 'chai', 'colada', 'hop', 'mojito', 'tequila', 'milk', 'vodka',
             'whiskey', 'vermouth', 'mint', 'wine', 'drink', 'soda', 'rum', 'limeade', 'beverage', 'liqueur', 'champagne',
             'coffee', 'nectar', 'water', 'ale', 'ice']

    dessert = ['creme', 'chocolate', 'granola', 'brownies', 'brownie', 'cookie', 'cookies', 'pancake', 'pancakes',
            'bread', 'muffins', 'muffin', 'waffles', 'biscuits', 'pie', 'pies', 'crepes', 'pudding', 'cheesecake', 
            'cake', 'cakes', 'bars', 'snickerdoodles', 'cinnabon', 'truffles', 'smokies', 'scones', 'popcorn', 'fudge', 
            'cinnamon', 'rolls', 'baklava', 'tiramisu', 'gingerbread', 'macaroons', 'cupcakes', 'cupcake', 'toffee', 
            'cheesecakes', 'biscotti', 'flan', 'zuppa', 'frosting', 'icing', 'puffs', 'fondant', 'shortbread', 'brookies',
            'tart', 'flake', 'candy', 'oatmeal', 'french toast', 'cronuts', 'chia', 'oats', 'crookies', 'marshmallow', 'snaps', 
            'doughnuts', 'glaze', 'beignets', 'birthday', 'chocolate', 'sugar', 'honey', 'marshmallows', 'flour', 'cereal', 
            'jellybeans', 'caramels', 'figs']

    pizza = ['pizza', 'calzones']

    sandwich = ['sandwich', 'burger', 'burgers', 'hot dog', 'sandwiches', 'wraps', 'hamburger', 'hamburgers', 'buns']

    pasta = ['mac', 'lasagna', 'pasta', 'spaghetti', 'macaroni', 'noodles', 'noodle', 'fettuccine', 'fettuccini', 'penne', 
            'spaetzle', 'ravioli', 'vermicelli', 'ziti', 'tortellini', 'linguine', 'gnocchi', 'manicotti']

    side_dish = ['cornbread', 'naan', 'sauce', 'pretzels', 'pretzel', 'baguettes', 'bread', 'dressing', 'seasoning',
                 'focaccia', 'spread', 'vinaigrette', 'toast', 'crust', 'salsa', 'bruschetta', 'antipasto', 
                 'sticks', 'appetizer', 'dip', 'paprika', 'cheese', 'baguette', 'sesame', 'olive', 'olives']

    doggie = ['doggie', 'doggy', 'dog treats', 'dog biscuits', 'dog food', 'good dog']
                 
    # p = inflect.engine() ####Singular/plural

    for keys in data:
        data[keys]["t_recipe"]= []
        list_title = [i for item in data[keys]['ingredients'] for i in item.split()] #Dans les ingrédients
        title_fruit = set(list_title)&set(fruit)
        is_fruit = sorted(title_fruit, key = lambda k : list_title.index(k))
        if len(is_fruit)!=0:
            data[keys]["t_recipe"].append("Dessert with fruit") #Fruit
        title_dessert = set(list_title)&set(dessert)
        is_dessert = sorted(title_dessert, key = lambda k : list_title.index(k))
        if len(is_dessert)!=0:
            data[keys]["t_recipe"].append("Dessert") #Dessert
        title_veggie = set(list_title)&set(vegetable) 
        is_veggie = sorted(title_veggie, key = lambda k : list_title.index(k))
        if len(is_veggie)!=0:
            data[keys]["t_recipe"].append("Dish with veggies") #Légumes
        title_meat = set(list_title)&set(meat)
        is_meat = sorted(title_meat, key = lambda k : list_title.index(k))
        if len(is_meat)!=0:
            data[keys]["t_recipe"].append("Dish with meat") #Viande
        title_fish = set(list_title)&set(fish)
        is_fish = sorted(title_fish, key = lambda k : list_title.index(k))
        if len(is_fish)!=0:
            data[keys]["t_recipe"].append("Dish with Sea Food/fish") #Poisson
        title_egg = set(list_title)&set(egg)
        is_egg = sorted(title_egg, key = lambda k : list_title.index(k))
        if len(is_egg)!=0:
            data[keys]["t_recipe"].append("Dish with egg") #Oeuf
        title_drink = set(list_title)&set(drink)
        is_drink = sorted(title_drink, key = lambda k : list_title.index(k))
        if len(is_drink)!=0:
            data[keys]["t_recipe"].append("Drink") #Boisson
        title_pizza = set(list_title)&set(pizza)
        is_pizza = sorted(title_pizza, key = lambda k : list_title.index(k))
        if len(is_pizza)!=0:
            data[keys]["t_recipe"].append("Pizza") #Pizza
        title_pasta = set(list_title)&set(pasta)
        is_pasta = sorted(title_pasta, key = lambda k : list_title.index(k))
        if len(is_pasta)!=0:
            data[keys]["t_recipe"].append("Pasta") #Pâtes
        title_sdish = set(list_title)&set(side_dish)
        is_sdish = sorted(title_sdish, key = lambda k : list_title.index(k))
        if len(is_sdish)!=0:
            data[keys]["t_recipe"].append("Side Dish") #Accompagnement
        title_sandwich = set(list_title)&set(sandwich)
        is_sandwich = sorted(title_sandwich, key = lambda k : list_title.index(k))
        if len(is_sandwich)!=0:
            data[keys]["t_recipe"].append("Sandwich") #Sandwich / Burger /Hot Dog
        title_dog = set(list_title)&set(doggie)
        is_doggie = sorted(title_dog, key = lambda k : list_title.index(k))
        if len(is_doggie)!=0:
            data[keys]["t_recipe"].append("Recipes for dogs") #Recettes pour chien
        if  data[keys]["t_recipe"] ==[]: #si incconnu 
            data[keys]["t_recipe"].append("Unknown")                   
        list_title = []
    # sys.stdout = open("list_recipe_prog.txt", "a")
    # print(data[keys]['title'], data[keys]['RecipeId'], data[keys]['t_recipe'])
    sys.stdout = open("list_recipe_unknown.txt", "a")
    if data[keys]['t_recipe']=="Unknown":
        print(data[keys]['title'], data[keys]['RecipeId'], data[keys]['t_recipe'])
    
    # sys.stdout.close()
    sys.stdout.close()
    data2 = data
    # ####classif chaud / froid
    ### : "hot", "oven", "bake"
    ### : "cold", "cool", "fridge"

    # jsonfile.close()

    # ####Export des données modifiées
    # with open('recipes_raw_result_classif2.json', 'w') as outfile:
    #     json.dump(data, outfile)
    # outfile.close()

    return data2
   

def main():

    data2 = classification_recipe(data)  

    with open('recipes_raw_result.json', 'w', encoding='utf-8') as f:
        json.dump(data2, f, indent=4)  

if __name__ == "__main__":
    main()
