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

    
    fruit = ["Fruit", "Hazelnuts", "Walnuts", "Chestnuts", "Grapefruit", 
            "Lemon", "Orange", "Tangerine", "Apricot", "Mango",
            "Pineapple", "Rhubarb", "Strawberry", "Strawberries", "Blackberry",
            "Cherry", "Blueberry", "Nectarine", "Peach", "Plum",
            "Raspberry", "Watermelon", "Apple", "Apples", "Cranberry", "Fig",
            "Grape", "Pear", "Pomegranate", "Quince", "Quinces", "Banana", "Bananas", "Kiwi",
            "Berry", "Applesauce", "Almond", "Almonds", "Coconut", "Pecans"]

    vegetable = ["Vegetable", "Kale", "Leek", "Radicchio", "Radish", "Rutabaga", 
            "Turnip", "Sprouts", "Beetroot", "Red Cabbage",
            "Avocado", "Artichoke", "Asparagus", "Spinach", "Carrot", "Carrots",
            "Pepperoni", "Celeriac", "Chive", "Collard", "Pea", "Fava Bean", 
            "Fennel", "Fiddlehead", "Morel", "Mustard", "Eggplant",
            "Tomato", "Tomatoes", "Corn", "Broccoli", "Cucumber", "Cucumbers", "Bean", "Beans", "Zucchini",
            "Celery", "Butternut", "Cauliflower", "Garlic", "Mushroom", "Mushrooms",
            "Potato", "Potatoes", "Pumpkin", "Sweet Potato", "Chard", "Chicory",
            "Pak Choi", "Onion", "Salad", "Guacamole", "Veggie", "Rice", "Peppers", 
            "Lentil", "Hummus", "Lettuce", "Vegetables", "Vegetarian", "Veggies",
            "Fries", "Cabbage", "Ratatouille", "Squash", "Orzo", "Beets", "Quinoa", 
            "Gazpacho", "Soup", "Dahl", "BLT", "Minestrone", "Colcannon", "Slaw", 
            "Chickpea", "Romaine", "Coleslaw", "Peas"]
   
    meat = ["Chicken", "Chicken-Rotisserie", "Beef", "Turkey","Rib", "Ribs", "Meatloaf", "Meatloaves",
    "Meatball","Meatballs", "Lamb", "Meat", "Pork", "Pig", "Steak", "Steaks", "Quail", "Rabbit", "Poultry", "Sausage",
     "Sirloin", "Bacon", "Filet", "Pollo", "Scallops", "Chili", "Taco", "Enchiladas", "Jambalaya", "Goulash", 
     "Carne", "Stew", "Ham", "Wings", "Osso", "Roast", "Sloppy", "Mahi", "Duck", "Brisket", "Prosciutto", 
     "Casserole", "Cooker", "Quiche", "Dumplings", "Gravy", "Moussaka"]

    egg = ["Egg", "Eggs", "Omelet"]

    fish = ["Fish", "Seafood", "Salmon", "Shrink", "Cod", "Halibut", "Trout", "Crab","Crabs",
     "Tilapia", "Shrimp", "Tuna", "Shells", "Clam", "Crabby", "Lobster", "Oysters", "Prawns", 
     "Mussels", "Haddock", "Sea"]

    drink = ["Water", "Juice", "Tea", "Lemonade", "Sangria", "Punch", "Cocoa", "Beer", "Eggnog", "Grog", 
    "Shake", "Margarita", "MArgarityas", "Smoothie", "Chai", "Colada", "Hop", "Mojito"]

    dessert = ["Creme", "Chocolate", "Granola", "Brownies", "Brownie",
                 "Cookie","Cookies", "Pancake", "Pancakes", "Bread", "Muffins", "Muffin", "Waffles", 
                 "Biscuits", "Pie", "Pies", "Crepes", "Pudding","Cheesecake", "Cake", "Cakes",
                  "Bars", "Snickerdoodles", "Cinnabon", "Truffles", "Smokies", "Scones", 
                  "Popcorn", "Fudge", "Cinnamon", "Rolls", "Baklava", "Tiramisu", "Gingerbread",
                 "Macaroons", "Cupcakes", "Cu^pcake", "Toffee", "Cheesecakes", "Biscotti", "Flan", "Zuppa", "Frosting", 
                 "Icing", "Puffs", "Fondant", "Shortbread", "Brookies", "Tart", "Flake", "Candy", "Oatmeal", 
                 "French Toast", "Cronuts", "Chia", "Oats", "Crookies", "Marshmallow", "Snaps", "Doughnuts", 
                 "Glaze", "Beignets"]

    pizza = ["Pizza", "Calzones"]

    sandwich =["Sandwich", "Burger", "Burgers", "Hot Dog", "Sandwiches", "Wraps", "Hamburger", "Hamburgers", "Buns"]

    pasta = ["Mac", "Lasagna", "Pasta", "Spaghetti", "Macaroni", "Noodles", "Noodle", "Fettuccine", "Fettuccini", "Penne", "Spaetzle", 
    "Ravioli", "Vermicelli", "Ziti", "Tortellini", "Linguine", "Gnocchi", "Manicotti"]

    side_dish = ["Cornbread", "Naan", "Sauce", "Pretzels", "Pretzel", "Baguettes", "Bread", "Dressing", "Seasoning", 
    "Focaccia", "Spread", "Vinaigrette", "Toast", "Crust", "Salsa", "Bruschetta", "Cream", "Antipasto", "Sticks", "Appetizer", "Dip"]

    doggie = ["Doggie", "Doggy", "Dog Treats", "Dog Biscuits", "Dog Food", "Good Dog"]
                 
    # p = inflect.engine() ####Singular/plural

    for keys in data:
        if data[keys]['t_recipe'] == "Unknown":
            list_title = [i for item in data[keys]["ingredients"] for i in item.split()] #Dans le titre seulement
            # classification_recipe(data, list_title)
            # data[keys].update({"t_recipe": "Unknown"})
            for word in list_title:
                if word.islower()==True:
                    list_title += word.capitalize()
                else:
                    list_title += word
            list_title = re.sub(r"(\w)([A-Z])", r"\1 \2", list_title)
            title_fruit = set(list_title)&set(fruit)
            is_fruit = sorted(title_fruit, key = lambda k : list_title.index(k))
            if len(is_fruit)!=0:
                data[keys].update({"t_recipe": "Dessert with fruit"}) #Fruit
            else:
                title_dessert = set(list_title)&set(dessert)
                is_dessert = sorted(title_dessert, key = lambda k : list_title.index(k))
                if len(is_dessert)!=0:
                    data[keys].update({"t_recipe": "Dessert"}) #Dessert
                else:
                    title_veggie = set(list_title)&set(vegetable) 
                    is_veggie = sorted(title_veggie, key = lambda k : list_title.index(k))
                    if len(is_veggie)!=0:
                        data[keys].update({"t_recipe": "Dish with veggies"}) #Légumes
                    else:
                        title_meat = set(list_title)&set(meat)
                        is_meat = sorted(title_meat, key = lambda k : list_title.index(k))
                        if len(is_meat)!=0:
                            data[keys].update({"t_recipe": "Dish with meat"}) #Viande
                        else:
                            title_fish = set(list_title)&set(fish)
                            is_fish = sorted(title_fish, key = lambda k : list_title.index(k))
                            if len(is_fish)!=0:
                                data[keys].update({"t_recipe": "Dish with Sea Food/fish"}) #Poisson
                            else:
                                title_egg = set(list_title)&set(egg)
                                is_egg = sorted(title_egg, key = lambda k : list_title.index(k))
                                if len(is_egg)!=0:
                                    data[keys].update({"t_recipe": "Dish with egg"}) #Oeuf
                                else:
                                    title_drink = set(list_title)&set(drink)
                                    is_drink = sorted(title_drink, key = lambda k : list_title.index(k))
                                    if len(is_drink)!=0:
                                        data[keys].update({"t_recipe": "Drink"}) #Boisson
                                    else:
                                        title_pizza = set(list_title)&set(pizza)
                                        is_pizza = sorted(title_pizza, key = lambda k : list_title.index(k))
                                        if len(is_pizza)!=0:
                                            data[keys].update({"t_recipe": "Pizza"}) #Pizza
                                        else:    
                                            title_pasta = set(list_title)&set(pasta)
                                            is_pasta = sorted(title_pasta, key = lambda k : list_title.index(k))
                                            if len(is_pasta)!=0:
                                                data[keys].update({"t_recipe": "Pasta"}) #Pâtes
                                            else:
                                                title_sdish = set(list_title)&set(side_dish)
                                                is_sdish = sorted(title_sdish, key = lambda k : list_title.index(k))
                                                if len(is_sdish)!=0:
                                                    data[keys].update({"t_recipe": "Side Dish"}) #Accompagnement
                                                else:
                                                    title_sandwich = set(list_title)&set(sandwich)
                                                    is_sandwich = sorted(title_sandwich, key = lambda k : list_title.index(k))
                                                    if len(is_sandwich)!=0:
                                                        data[keys].update({"t_recipe": "Sandwich"}) #Sandwich / Burger /Hot Dog
                                                    else:
                                                        title_dog = set(list_title)&set(doggie)
                                                        is_doggie = sorted(title_dog, key = lambda k : list_title.index(k))
                                                        if len(is_doggie)!=0:
                                                            data[keys].update({"t_recipe": "Recipes for dogs"}) #Recettes pour chien
                                                        else:
                                                            data[keys].update({"t_recipe": "Unknown"})
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
