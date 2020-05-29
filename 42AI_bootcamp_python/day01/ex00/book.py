import sys
import datetime
from recipe import Recipe

class Book:
    def __init__(self, name):
        self.name = name
        self.last_update = ""
        self.creation_date = datetime.datetime.now()
        self.recipes_list = {'starter': [], 'lunch': [], 'dessert': []}

    def get_recipe_by_name(self, name):
        """Print a recipe with the name 'name' and return the insatance"""
        for key in self.recipes_list:
            for recipe in self.recipes_list[key]:
                if recipe.name == name:
                    print(recipe)
                    return recipe

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type"""
        for recipe in self.recipes_list[recipe_type]:
            print(recipe.name)

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if not isinstance(recipe, Recipe):
            print("You can only add instance of Recipe")
            sys.exit()
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.datetime.now()
