from peper.buckets import Ingredients

class Jaje:
    @staticmethod
    def komad():
        return Jaje.komada(1)

    @staticmethod
    def komada(x):
        Ingredients.add("jaje", x)
        return "jaje" if x == 1 else f"{x} jajeta"