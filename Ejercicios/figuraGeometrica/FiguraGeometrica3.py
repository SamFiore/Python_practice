from FiguraGeometrica2 import *
from FiguraGeometrica import FiguraGeometrica

# No se puede instanciar una clase abstracta
# figura = FiguraGeometrica()

print('Creacion Obj Cuadrado'.center(50,'-'))
cuadrado1 = Cuadrado(4,'azul')
print(cuadrado1.alto)
print(cuadrado1.ancho)
print(cuadrado1.calcular_area())
print(cuadrado1)
print('-'.center(70,'-'))
print('Creacion Obj. Rectangulo'.center(50,'-'))
rectangulo1 = Rectangulo(alto=10,ancho=3,color='verde')
print(rectangulo1.alto)
print(rectangulo1.ancho)
rectangulo1.ancho = -23
print(rectangulo1.calcular_area())
print(rectangulo1)
print('-'.center(70,'-'))
