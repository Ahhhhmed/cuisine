sastojci = {}

class Jaje:
    @staticmethod
    def komad():
        return Jaje.komada(1)

    @staticmethod
    def komada(x):
        if "jaje" not in sastojci.keys():
            sastojci["jaje"] = 0
        sastojci["jaje"] += x
        return "jaje" if x == 1 else f"{x} jajeta"

class Jajca:
    @staticmethod
    def instructions():
        return f"Sprzi {Jaje.komad()} i onda jos {Jaje.komada(2)} i cepaj."

print("Instructions: ", Jajca().instructions())
print("Ingredients: ", sastojci)