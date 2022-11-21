import string
import random
import json
import requests

def main():

    # get materials that user had
    global materials
    materials = get_ing()

    # get recipes from json file
    fullRecipies = get_recipes()

    # search recipees for materials that user had
    matches = search_recipes(fullRecipies, materials)

    # removes the recipe if there are multiple times
    single_matches = check_multiples(matches)

    # print the matched meals name in order
    global number
    number = 0
    for match in single_matches:
        number = number + 1
        print(number, match['Name'])

    if single_matches != []:
        # get users preference of meal
        meal_number = select_meal(single_matches)
        print(meal_number)


# get materials that user had
def get_ing():
    materialString = input("enter materials in home seperated by comma: ")
    materialList = materialString.split(",")
    return materialList

# get recipes from json file
def get_recipes():
    f = open('recipes.json', 'r')
    db = json.load(f)
    return db

# search recipees for materials that user had
def search_recipes(recipe_list, user_materials):
    matches = []
    for recipe in recipe_list:
        for element in user_materials:
            found_material = False
            a = 0
            for recipe_materials in recipe['Ingredients']:

                one_material=[]
                one_material = recipe_materials.split(" ")
                for material_word in one_material:
                    if(material_word == element):
                            found_material = True
                a = a + 1

            if(found_material == True):

                if a > 3:
                    matches.append(recipe)
    return matches

# search for not specified ingredient, but general
def general_ing():
    ...


# removes the recipe if there are multiple times
def check_multiples(matches):
    single_matches = []
    for meal in matches:
        if meal not in single_matches:
            single_matches.append(meal)
    return single_matches

# get users preference of meal
def select_meal(single_matches):
    try:
        preferred_meal = input("what's your preference of meal? ")
        for one_meal in single_matches:
            if one_meal == preferred_meal:
                print("found it!")
    except ValueError:
        pass
    return preferred_meal


if __name__ == "__main__":
    main()