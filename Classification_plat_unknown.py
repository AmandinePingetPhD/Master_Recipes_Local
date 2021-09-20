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
from json.decoder import JSONDecodeError
import string
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

    
    fruit = ['fruit', 'hazelnuts', 'walnuts', 'chestnuts', 'grapefruit', 'lemon', 'lime', 'orange', 
            'tangerine', 'apricot', 'mango', 'pineapple', 'rhubarb', 'strawberry', 'strawberries',
            'blackberry', 'cherry', 'blueberry', 'nectarine', 'peach', 'plum', 'raspberry', 
            'watermelon', 'apple', 'apples', 'cranberry', 'fig', 'grape', 'pear', 'pomegranate',
            'quince', 'quinces', 'banana', 'bananas', 'kiwi', 'berry', 'applesauce', 'almond', 
            'almonds', 'coconut', 'pecans', 'peaches', 'grapes', 'blueberries']

    vegetable = ['vegetable', 'zucchinis', 'kale', 'leek', 'radicchio', 'radish', 'rutabaga', 'turnip', 'sprouts', 
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
   
    # meat = ['chicken', 'chicken-rotisserie', 'beef', 'turkey', 'rib', 'ribs', 'meatloaf', 'meatloaves', 'meatball',
    #         'meatballs', 'lamb', 'meat', 'pork', 'pig', 'steak', 'steaks', 'quail', 'rabbit', 'poultry', 
    #         'sausage', 'sirloin', 'bacon', 'filet', 'pollo', 'scallops', 'chili', 'taco', 'enchiladas', 
    #         'jambalaya', 'goulash', 'carne', 'stew', 'ham', 'wings', 'osso', 'roast', 'sloppy', 'mahi', 
    #         'duck', 'brisket', 'prosciutto', 'casserole', 'cooker', 'quiche', 'dumplings', 'gravy', 'moussaka']

    # egg = ['egg', 'eggs', 'omelet']

    # fish = ['fish', 'seafood', 'salmon', 'shrink', 'cod', 'halibut', 'trout', 'crab', 'crabs', 'tilapia', 'shrimp', 
    #         'tuna', 'shells', 'clam', 'crabby', 'lobster', 'oysters', 'prawns', 'mussels', 'haddock', 'sea', 'clams', 
    #         'crawfish']

    drink = ['water', 'juice', 'tea', 'lemonade', 'sangria', 'punch', 'cocoa', 'beer', 'eggnog', 'grog', 'shake',
             'margarita', 'margaritas', 'smoothie', 'chai', 'colada', 'hop', 'mojito', 'tequila', 'milk', 'vodka',
             'whiskey', 'vermouth', 'mint', 'wine', 'drink', 'soda', 'rum', 'limeade', 'beverage', 'liqueur', 'champagne',
             'coffee', 'nectar', 'water', 'ale', 'ice']

    dessert = ['creme', 'chocolate', 'Chocolate', 'vanilla', 'granola', 'brownies', 'brownie', 'cookie', 'cookies', 
            'pancake', 'pancakes',
            'bread', 'muffins', 'muffin', 'waffles', 'biscuits', 'pie', 'pies', 'crepes', 'pudding', 'cheesecake', 
            'cake', 'cakes', 'bars', 'snickerdoodles', 'cinnabon', 'truffles', 'smokies', 'scones', 'popcorn', 'fudge', 
            'cinnamon', 'rolls', 'baklava', 'tiramisu', 'gingerbread', 'macaroons', 'cupcakes', 'cupcake', 'toffee', 
            'cheesecakes', 'biscotti', 'flan', 'zuppa', 'frosting', 'icing', 'puffs', 'fondant', 'shortbread', 'brookies',
            'tart', 'flake', 'candy', 'oatmeal', 'french toast', 'cronuts', 'chia', 'oats', 'crookies', 'marshmallow', 'snaps', 
            'doughnuts', 'glaze', 'beignets', 'birthday', 'chocolate', 'sugar', 'honey', 'marshmallows', 'flour', 'cereal', 
            'jellybeans', 'caramels', 'figs']

    # pizza = ['pizza', 'calzones']

    # sandwich = ['sandwich', 'burger', 'burgers', 'hot dog', 'sandwiches', 'wraps', 'hamburger', 'hamburgers', 'buns']

    # pasta = ['mac', 'lasagna', 'pasta', 'spaghetti', 'macaroni', 'noodles', 'noodle', 'fettuccine', 'fettuccini', 'penne', 
    #         'spaetzle', 'ravioli', 'vermicelli', 'ziti', 'tortellini', 'linguine', 'gnocchi', 'manicotti']

    side_dish = ['cornbread', 'naan', 'sauce', 'pretzels', 'pretzel', 'baguettes', 'bread', 'dressing', 'seasoning',
                 'focaccia', 'spread', 'vinaigrette', 'toast', 'crust', 'salsa', 'bruschetta', 'antipasto', 
                 'sticks', 'appetizer', 'dip', 'paprika', 'cheese', 'baguette', 'sesame', 'olive', 'olives']

    doggie = ['doggie', 'doggy', 'dog treats', 'dog biscuits', 'dog food', 'good dog']
                 
    # p = inflect.engine() ####Singular/plural

    for keys in data:
        if data[keys]["t_recipe"] == []:
            # data[keys]["t_recipe"]= []
            list_title = [i for item in data[keys]['ingredients'] for i in item.split()] #Dans les ingrédients
            list_title = [''.join(c for c in s if c not in string.punctuation) for s in list_title]
            title_drink = set(list_title)&set(drink)
            is_drink = sorted(title_drink, key = lambda k : list_title.index(k))
            if len(is_drink)!=0:
                data[keys]["t_recipe"].append("Drink") #Boisson
            elif data[keys]["t_recipe"] == []:
                title_sdish = set(list_title)&set(side_dish)
                is_sdish = sorted(title_sdish, key = lambda k : list_title.index(k))
                if len(is_sdish)!=0:
                    data[keys]["t_recipe"].append("Side Dish") #Accompagnement
                elif data[keys]["t_recipe"] == []:
                    title_fruit = set(list_title)&set(fruit)
                    is_fruit = sorted(title_fruit, key = lambda k : list_title.index(k))
                    if len(is_fruit)!=0:
                        data[keys]["t_recipe"].append("Dessert with fruit") #Fruit
                    title_dessert = set(list_title)&set(dessert)
                    is_dessert = sorted(title_dessert, key = lambda k : list_title.index(k))
                    if len(is_dessert)!=0:
                        data[keys]["t_recipe"].append("Dessert") #Dessert
                    elif data[keys]["t_recipe"] == []:
                        title_veggie = set(list_title)&set(vegetable) 
                        is_veggie = sorted(title_veggie, key = lambda k : list_title.index(k))
                        if len(is_veggie)!=0:
                            data[keys]["t_recipe"].append("Dish with veggies") #Légumes
        list_title = []

    for keys in data:
        list_title = [i for item in data[keys]['title'] for i in item.split()] #Dans les ingrédients
        list_title = [''.join(c for c in s if c not in string.punctuation) for s in list_title]
        title_dog = set(list_title)&set(doggie)
        is_doggie = sorted(title_dog, key = lambda k : list_title.index(k))
        if len(is_doggie)!=0:
            data[keys]["t_recipe"].append("Recipes for dogs") #Recettes pour chien
        list_title = []
    # sys.stdout = open("list_recipe_unknown.txt", "a")
    # if data[keys]["t_recipe"]==["Unknown"]:
    #     print(data[keys]['title'], data[keys]['RecipeId'], data[keys]['t_recipe'])
    
    # sys.stdout.close()
    # sys.stdout.close()
    data2 = data
    # ####classif chaud / froid
    ### : "hot", "oven", "bake"
    ### : "cold", "cool", "fridge"

    # jsonfile.close()

    # ####Export des données modifiées
    # with open('recipes_raw_result_classif2.json', 'w') as outfile:
    #     json.dump(data, outfile)
    # outfile.close()

    #POur unknown - à revoir
    # for word in list_title:
    #     if word.islower()==False:
    #         list_title += word.lower()
            # print(list_title)


    return data2
   

def main():

    data2 = classification_recipe(data)  

    with open('recipes_raw_result.json', 'w', encoding='utf-8') as f:
        json.dump(data2, f, indent=4)  

if __name__ == "__main__":
    main()
