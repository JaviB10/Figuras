
from cuadrado import Cuadrado
from rectangulo import Rectangulo
from triangulorecto import TrianguloRecto



tipo = int(input("Ingrese la figura: 1. Cuadrado 2. Rectangulo 3.TrianguloRecto"))

if tipo == 1:
    lado = int(input("Ingrese el valor del lado: "))
    figura = Cuadrado(lado)
elif tipo == 2:
    base = int(input("Ingrese el valor de la base: "))
    altura = int(input("Ingrese el valor de la altura: "))
    figura = Rectangulo(base, altura)
elif tipo == 3:
    base = int(input("Ingrese el valor de la base: "))
    altura = int(input("Ingrese el valor de la altura: "))
    figura = TrianguloRecto(base, altura)
else:
    print("Error: ingrese el tipo 1, 2 o 3")
    exit()

print ("La figura pertecene a la clase " + type(figura).__name__)
print ("Su base es " + str(figura.base) + " y su altura es " + str(figura.altura))
print ("La superficie es " + str(figura.superficie()))
print ("Su perimetro es " + str(figura.perimetro()))