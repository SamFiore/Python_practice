from herenciaMultiple3 import Cuadrado

cuadrado1 = Cuadrado(25,'Green')
print(cuadrado1.alto)
print(cuadrado1.ancho)
print(cuadrado1.color)
print(cuadrado1.calcularArea())

#Método MRO = Method Resolution Order
print(Cuadrado.mro())