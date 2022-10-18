#make a dictionary about calories
calories = {
    "apple" : "130",
    "avocado" : "50",
    "banana" : "110",
    "cantaloupe" : "50",
    "grapefruit" : "60",
    "grapes" : "90",
    "honeydew melon" : "50",
    "kiwifruit" : "90",
    "lemon" : "15",
    "lime" : "20",
    "nectarin" :"60",
    "orange" : "80",
    "peach" : "60",
    "pear" : "100",
    "pineapple" : "50",
    "plums" : "70",
    "strawberries" : "50",
    "sweet cherries" : "100",
    "tangerine" : "50",
    "watermelon" : "80",
}

#get a fruit from user
fruit = input("Item: ")

#lower the input so it can match with dictionary
fruit1 = fruit.lower()

#loop through fruits dictionary
for i in calories:
    #find the fruit asked
    if i == fruit1:
        print("Calories:", calories[i])

