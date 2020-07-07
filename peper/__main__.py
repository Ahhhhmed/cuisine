import peper.recepies
import peper.buckets
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="Compile a snippet.")
    parser.add_argument('recepie', type=str, help='Recepie name')

    args = parser.parse_args()

    if args.recepie not in peper.recepies.l.keys():
        print("Recepie not found")
        exit()

    peper.recepies.l[args.recepie]().exec()

    print("Instructions:")
    i = 1
    for x in peper.buckets.Instructions.bucket:
        if x["level"] == peper.buckets.Instructions.step_level:
            print(f"Step {i}: {x['val']}")
            i += 1
        if x["level"] == peper.buckets.Instructions.tip_level:
            print(f"tip: {x['val']}")
    print()
    print("Ingredients:")
    print(peper.buckets.Ingredients.bucket)
