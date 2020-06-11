import cuisine.recepies
import cuisine.bucket
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="Compile a snippet.")
    parser.add_argument('recepie', type=str,
                        help='Recepie name')

    args = parser.parse_args()

    if args.recepie not in cuisine.recepies.l.keys():
        print("Recepie not found")
        exit()

    print("Instructions: ", cuisine.recepies.l[args.recepie]().instructions())
    print("Ingredients: ", cuisine.bucket.bucket)
