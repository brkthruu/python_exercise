from recipe import Recipe
from book import Book

tourte = Recipe("tourte", 3, 50, ['egg','bread','butter'], "This is a recipe for sandwich", "dessert")
to_print = str(tourte)
print(to_print)

pizza = Recipe("pizza", 4, 40, ['flour', 'tomato', 'olive'], "standard pizza", "lunch")
salad = Recipe("salad", 2, 10, ['lettuce', 'onion', 'sauce'], "diet salad", "starter")
bacon = Recipe("bacon", 1, 5, ['bacon', 'egg'], "easy breakfast", "starter")

# Make Recipe Book
ob = Book('cookbook')

# Add recipe tourte
ob.add_recipe(tourte)
ob.add_recipe(pizza)
ob.add_recipe(salad)
ob.add_recipe(bacon)

# Print tourte recipe
ob.get_recipe_by_name('pizza')

# Print all dessert name
ob.get_recipes_by_types('starter')

# Checking timestamp
print(ob.creation_date)
print(ob.last_update)
