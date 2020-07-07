class Ingredients:
    bucket = {}

    @staticmethod
    def add(ingr, units):
        if ingr not in Ingredients.bucket.keys():
            Ingredients.bucket[ingr] = 0

        Ingredients.bucket[ingr] += units

class Instructions:
    bucket = []

    step_level = 1
    tip_level = 2

    @staticmethod
    def step(step):
        Instructions.bucket.append({"val":step, "level":Instructions.step_level})

    @staticmethod
    def tip(tip):
        Instructions.bucket.append({"val":tip, "level":Instructions.tip_level})