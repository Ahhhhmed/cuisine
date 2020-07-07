from peper.ingredients import *
from peper.buckets import Instructions

class Jajca:
    @staticmethod
    def exec():
        Instructions.step(f"Sprzi {Jaje.komad()} i onda jos {Jaje.komada(2)} i cepaj.")
        Instructions.tip("pazi da ne zagore.")

