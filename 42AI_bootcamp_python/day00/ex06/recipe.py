cookbook = {
        'sandwich': {
                'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
                'meal': 'lunch',
                'prep_time': '10'
            },
        'cake': {
                'ingredients': ['flour', 'sugar', 'eggs'],
                'meal': 'dessert',
                'prep_time': '60'
            },
        'salad': {
                'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
                'meal': 'lunch',
                'prep_time': '15'
            },
        'pizza': {
                'ingredients': ['delete', 'in'],
                'meal': 'breakfast',
                'prep_time': '4'
            }
        }

# print(cookbook.keys())
# print(cookbook.values())
# print(cookbook.items())


def showrecipe(dic):
    print("Recipe for cake:")
    for k, val in cookbook.get(dic).items():
        print("{} : {}".format(k, val))


def delrecipe(dic):
    del cookbook[dic]


def addrecipe(name, ingrds, meal, prep):
    cookbook[name] = {'ingredients': ingrds, 'meal': meal, 'prep_time': prep}


def allrecipe():
    print("There are {} recipes in this book".format(len(cookbook)))
    for val in cookbook:
        print(val)


if __name__ == "__main__":
    msg = """
    Please select an option by typing the corresponding number:
    1: Add a recipe
    2: Delete a recipe
    3: Print a recipe
    4: Print the cookbook
    5: Quit
    """
    while(1):
        print(msg)
        num = int(input())
        if num == 1:
            r_name = input("Enter a name: ")
            r_ingrd = input("Enter ingredients(seperated by comma): ")
            r_meal = input("Enter a meal type: ")
            r_time = input("Enter a prep_time: ")
            addrecipe(r_name, r_ingrd.split(","), r_meal, r_time)
        elif num == 2:
            delrecipe(input("Enter the recipe's name you want to delete:"))
        elif num == 3:
            showrecipe(input("Enter the recipe's name to get its details:"))
        elif num == 4:
            allrecipe()
        elif num == 5:
            print("Cookbook closed.")
            break
        else:
            print("This option does not exist, type the corresponding number.")
            print("To exit, enter 5.")
