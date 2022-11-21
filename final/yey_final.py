#20.11.2022
#13.50
#gereksiz kütüphaneleri ve dosyaları sil


import json


def main():

    # get materials that user had
    global materials
    materials = get_ing()

    # get recipes from json file
    fullRecipies = get_recipes()

    # search recipees for materials that user had
    matches = search_recipes(fullRecipies, materials)

    # print that which recipe contains how many ingredients
    global recipe_names
    r_times, recipe_names = recipe_times(matches)

    try:
        # removes the recipe if there are multiple times
        single_matches = check_multiples(r_times)
        for w in single_matches:
            print(w)
    except TypeError:
        print("sorry, try with another ingredient")

    # get yes/no from user
    show_recipe()

    try:
        users_choice = write_recipe(fullRecipies)
        print(users_choice)
    except:
        print("except error")


def write_recipe(recipe_list):
    getting_recipe = []
    for recipe in recipe_list:
        found_recipe = False
        # global recipe_name
        # for recipe_name in recipe["Name"]:
        #     print(recipe_name, end="")
        #     if recipe_name == recipe_names:
        if recipe["Name"] == recipe_names:
            found_recipe = True

        if (found_recipe == True):

            getting_recipe.append(recipe)
    return(getting_recipe)

# get materials that user had
def get_ing():
    materialString = input("enter at least 3 materials in home seperated by comma: ")
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
            for recipe_materials in recipe['Ingredients']:

                one_material=[]
                one_material = recipe_materials.split(" ")

                for material_word in one_material:

                    if(material_word == element):
                        found_material = True

            if(found_material == True):
                matches.append(recipe)
    return matches

# Python code to count the number of occurrences
def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count

# print that which recipe contains how many ingredients
def recipe_times(matches):
    matches_name = []
    for match in matches:
        if match not in matches_name:
            matches_name.append(match['Name'])
    for k in matches:
        global match_times
        match_times = countX(matches, k)
        r_times = []
        if match_times > 2:
            r_times.append("{} has {} entered materials.".format(k["Name"], match_times))

            recipe_names = k["Name"]

            return r_times, recipe_names


# removes the recipe if there are multiple times
def check_multiples(names):
    single_matches = []
    for meal in names:
        if meal not in single_matches:
            single_matches.append(meal)
    return single_matches

def show_recipe():
    answer_ = input("Would you like to see recipe? yes/no \n")
    if answer_ != "yes":
        print("see you another time")
    else:
        return answer_
if __name__ == "__main__":
    main()