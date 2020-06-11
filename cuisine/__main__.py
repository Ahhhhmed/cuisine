import cuisine.recepies
import cuisine.ingredients
import sys

def main():
    print("Instructions: ", cuisine.recepies.l[sys.argv[1]]().instructions())
    print("Ingredients: ", cuisine.ingredients.bucket)
