
from rectangulo import Rectangulo

import math

class TrianguloRecto(Rectangulo):

    def superficie (self):
        return super().superficie()/2


    def perimetro (self):
        hipotenusa = math.sqrt(self.base*self.base + self.altura*self.altura)
        return self.base + self.altura + hipotenusa
