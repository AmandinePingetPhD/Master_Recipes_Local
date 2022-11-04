"""Master Cook - IA de suggestion de recettes v0."""

# Python 3.9.6 # Coding Utf-8

# Function to classify recipe by kind of dish
# @author : Amandine Pinget, PhD


# Import
import os
import sys
import json
from json.decoder import JSONDecodeError

fileDir = os.path.dirname(os.path.abspath(__file__))
newPath = os.path.join(fileDir, 'Data_recipes')
sys.path.append(newPath)
os.chdir(newPath)

# Import recipes
with open('recipes_raw_result.json', encoding='utf8') as jsonfile:
    try:
        Rawdata = jsonfile.read()
        data = json.loads(Rawdata)
    except JSONDecodeError as e:
        print('Decoding JSON has failed', e)


def classification_recipe(data):
    """Classification function by recipes type."""
    # Review strat classification : unsupervised?
    # Modif complexity function : small functions / Ensemble logic

    # Several classification to be made :
    # - kind dof dish : salty / sweet / drink
    # - content/ingredients: vegetarian, meat, fish, egg, fruits,...
    # - hot/cold
    # - seansonality : spring, summer, autumn, winter

    # Ask Db Recipe :
    # Look for content : title / ingredients
    # Seasonality table : search fruit / vegetable => season
    # Write in JSOn output

    fruit = ["Fruit", "Hazelnuts", "Walnuts", "Chestnuts", "Grapefruit",
             "Lemon", "Orange", "Tangerine", "Apricot", "Mango",
             "Pineapple", "Rhubarb", "Strawberry", "Strawberries",
             "Blackberry", "Cherry", "Blueberry", "Nectarine", "Peach", "Plum",
             "Raspberry", "Watermelon", "Apple", "Apples", "Cranberry", "Fig",
             "Grape", "Pear", "Pomegranate", "Quince", "Quinces", "Banana",
             "Bananas", "Kiwi", "Berry", "Applesauce", "Almond", "Almonds",
             "Coconut", "Pecans"]

    vegetable = ["Vegetable", "Kale", "Leek", "Radicchio", "Radish",
                 "Rutabaga", "Turnip", "Sprouts", "Beetroot",
                 "Red Cabbage", "Avocado", "Artichoke", "Asparagus",
                 "Spinach", "Carrot", "Carrots", "Pepperoni",
                 "Celeriac", "Chive", "Collard", "Pea", "Fava Bean",
                 "Fennel", "Fiddlehead", "Morel", "Mustard",
                 "Eggplant", "Tomato", "Tomatoes", "Corn", "Broccoli",
                 "Cucumber", "Cucumbers", "Bean", "Beans", "Zucchini",
                 "Celery", "Butternut", "Cauliflower", "Garlic",
                 "Mushroom", "Mushrooms", "Potato", "Potatoes",
                 "Pumpkin", "Sweet Potato", "Chard", "Chicory",
                 "Pak Choi", "Onion", "Salad", "Guacamole", "Veggie",
                 "Rice", "Peppers", "Lentil", "Hummus", "Lettuce",
                 "Vegetables", "Vegetarian", "Veggies", "Fries",
                 "Cabbage", "Ratatouille", "Squash", "Orzo",
                 "Beets", "Quinoa", "Gazpacho", "Soup", "Dahl",
                 "BLT", "Minestrone", "Colcannon", "Slaw",
                 "Chickpea", "Romaine", "Coleslaw", "Peas"]

    meat = ["Chicken", "Chicken-Rotisserie", "Beef", "Turkey", "Rib", "Ribs",
            "Meatloaf", "Meatloaves", "Meatball", "Meatballs", "Lamb", "Meat",
            "Pork", "Pig", "Steak", "Steaks", "Quail", "Rabbit", "Poultry",
            "Sausage", "Sirloin", "Bacon", "Filet", "Pollo", "Scallops",
            "Chili", "Taco", "Enchiladas", "Jambalaya", "Goulash",
            "Carne", "Stew", "Ham", "Wings", "Osso", "Roast", "Sloppy",
            "Mahi", "Duck", "Brisket", "Prosciutto", "Casserole", "Cooker",
            "Quiche", "Dumplings", "Gravy", "Moussaka"]

    egg = ["Egg", "Eggs", "Omelet"]

    fish = ["Fish", "Seafood", "Salmon", "Shrink", "Cod", "Halibut", "Trout",
            "Crab", "Crabs", "Tilapia", "Shrimp", "Tuna", "Shells", "Clam",
            "Crabby", "Lobster", "Oysters", "Prawns", "Mussels", "Haddock",
            "Sea"]

    drink = ["Water", "Juice", "Tea", "Lemonade", "Sangria", "Punch", "Cocoa",
             "Beer", "Eggnog", "Grog", "Shake", "Margarita", "Margarityas",
             "Smoothie", "Chai", "Colada", "Hop", "Mojito"]

    dessert = ["Creme", "Chocolate", "Granola", "Brownies", "Brownie",
               "Cookie", "Cookies", "Pancake", "Pancakes", "Bread", "Muffins",
               "Muffin", "Waffles", "Biscuits", "Pie", "Pies",
               "Crepes", "Pudding", "Cheesecake", "Cake", "Cakes",
               "Bars", "Snickerdoodles", "Cinnabon", "Truffles", "Smokies",
               "Scones", "Popcorn", "Fudge", "Cinnamon", "Rolls", "Baklava",
               "Tiramisu", "Gingerbread", "Macaroons", "Cupcakes",
               "Cupcake", "Toffee", "Cheesecakes", "Biscotti", "Flan",
               "Zuppa", "Frosting", "Icing", "Puffs", "Fondant",
               "Shortbread", "Brookies", "Tart", "Flake", "Candy",
               "Oatmeal", "French Toast", "Cronuts", "Chia", "Oats",
               "Crookies", "Marshmallow", "Snaps", "Doughnuts",
               "Glaze", "Beignets"]

    pizza = ["Pizza", "Calzones"]

    sandwich = ["Sandwich", "Burger", "Burgers", "Hot Dog", "Sandwiches",
                "Wraps", "Hamburger", "Hamburgers", "Buns"]

    pasta = ["Mac", "Lasagna", "Pasta", "Spaghetti", "Macaroni", "Noodles",
             "Noodle", "Fettuccine", "Fettuccini", "Penne", "Spaetzle",
             "Ravioli", "Vermicelli", "Ziti", "Tortellini", "Linguine",
             "Gnocchi", "Manicotti"]

    side_dish = ["Cornbread", "Naan", "Sauce", "Pretzels", "Pretzel",
                 "Baguettes", "Bread", "Dressing", "Seasoning",
                 "Focaccia", "Spread", "Vinaigrette", "Toast", "Crust",
                 "Salsa", "Bruschetta", "Cream", "Antipasto", "Sticks",
                 "Appetizer", "Dip"]

    doggie = ["Doggie", "Doggy", "Dog Treats", "Dog Biscuits", "Dog Food",
              "Good Dog"]

    for keys in data:
        data[keys]["t_recipe"] = []
        li_title = [i for item in [data[keys]["title"]] for i in item.split()]
        # Search in title only
        title_fruit = set(li_title) & set(fruit)
        is_fruit = sorted(title_fruit, key=lambda k: li_title.index(k))
        if len(is_fruit) != 0:
            data[keys]["t_recipe"].append("Dessert with fruit")    # Fruit
        title_dessert = set(li_title) & set(dessert)
        is_dessert = sorted(title_dessert, key=lambda k: li_title.index(k))
        if len(is_dessert) != 0:
            data[keys]["t_recipe"].append("Dessert")    # Desert
        else:
            title_veggie = set(li_title) & set(vegetable)
            is_veggie = sorted(title_veggie, key=lambda k: li_title.index(k))
            if len(is_veggie) != 0:
                data[keys]["t_recipe"].append("Dish with veggies")  # Veggies
            title_meat = set(li_title) & set(meat)
            is_meat = sorted(title_meat, key=lambda k: li_title.index(k))
            if len(is_meat) != 0:
                data[keys]["t_recipe"].append("Dish with meat")   # Meat
            title_fish = set(li_title) & set(fish)
            is_fish = sorted(title_fish, key=lambda k: li_title.index(k))
            if len(is_fish) != 0:
                data[keys]["t_recipe"].append("Dish with Sea Food/fish")
                # Fish
            title_egg = set(li_title) & set(egg)
            is_egg = sorted(title_egg, key=lambda k: li_title.index(k))
            if len(is_egg) != 0:
                data[keys]["t_recipe"].append("Dish with egg")   # Egg
            title_drink = set(li_title) & set(drink)
            is_drink = sorted(title_drink, key=lambda k: li_title.index(k))
            if len(is_drink) != 0:
                data[keys]["t_recipe"].append("Drink")   # Drink
            title_pizza = set(li_title) & set(pizza)
            is_pizza = sorted(title_pizza, key=lambda k: li_title.index(k))
            if len(is_pizza) != 0:
                data[keys]["t_recipe"].append("Pizza")   # Pizza
            title_pasta = set(li_title) & set(pasta)
            is_pasta = sorted(title_pasta, key=lambda k: li_title.index(k))
            if len(is_pasta) != 0:
                data[keys]["t_recipe"].append("Pasta")   # Pasta
            title_sdish = set(li_title) & set(side_dish)
            is_sdish = sorted(title_sdish, key=lambda k: li_title.index(k))
            if len(is_sdish) != 0:
                data[keys]["t_recipe"].append("Side Dish")    # Side dish
            title_sandwich = set(li_title) & set(sandwich)
            is_sand = sorted(title_sandwich, key=lambda k: li_title.index(k))
            if len(is_sand) != 0:
                data[keys]["t_recipe"].append("Sandwich")
                # Sandwich / Burger /Hot Dog
            title_dog = set(li_title) & set(doggie)
            is_doggie = sorted(title_dog, key=lambda k: li_title.index(k))
            if len(is_doggie) != 0:
                data[keys]["t_recipe"].append("Recipes for dogs")
                # Dog recipes
            if data[keys]["t_recipe"] == []:     # Unknown
                data[keys]["t_recipe"].append("Unknown")

        li_title = []
    data2 = data

    return data2


def main():
    """Execute main function."""
    data2 = classification_recipe(data)
    # Save
    with open('recipes_raw_result.json', 'w', encoding='utf-8') as f:
        json.dump(data2, f, indent=4)


if __name__ == "__main__":
    main()
