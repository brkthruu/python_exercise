import sys


class Recipe:
    def __init__(self, name, lvl, time, ingrds, des, recipe_type):

        if self.check_str(name):
            self.name = name
        else:
            print("name must be a string")
            sys.exit()

        if lvl not in [1, 2, 3, 4, 5]:
            print("cooking_lvl must be an integer between 1 and 5")
            sys.exit()
        else:
            self.cooking_lvl = lvl

        if type(time) != int:
            print("cooking_time must be a positive integer")
            sys.exit()
        elif time < 0:
            print("cooking_time must be a positive integer")
            sys.exit()
        else:
            self.cooking_time = time

        if type(ingrds) != list:
            print("ingredients must be a list type")
            sys.exit()
        else:
            for i in ingrds:
                if not self.check_str(i):
                    print("ingredients must be a string")
                    sys.exit()
            self.ingredients = ingrds

        if self.check_str(des) or des == "":
            self.description = des
        else:
            print("description must be a string")
            sys.exit()

        if recipe_type not in ['starter', 'lunch', 'dessert']:
            print("recipe_type must be 'starter' or 'lunch' or 'dessert'")
            sys.exit()
        else:
            self.recipe_type = recipe_type


    def check_str(self, data):
        try:
            data.isalpha()
        except AttributeError:
            return 0
        for i in data:
            if not i.isalpha() and not i.isspace():
                return 0
            else:
                return 1

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = ""
        txt = "name: {}\ncooking_lvl: {}\ncooking_time: {}\ningredients: {}\ndescription: {}\nrecipe_type: {}"\
        .format(self.name, self.cooking_lvl, self.cooking_time, self.ingredients, self.description, self.recipe_type)
        return txt
