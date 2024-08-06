from FiguraGeometrica import FiguraGeometrica
from FiguraGeometrica1 import Color

class Cuadrado(FiguraGeometrica,Color):
    def __init__(self,lado,color):
        FiguraGeometrica.__init__(self,lado,lado)
        Color.__init__(self,color)

    def __str__(self):
        return f'Del cuadrado, {FiguraGeometrica.__str__(self)}, {Color.__str__(self)}'
    
    def calcular_area(self):
        return self.alto * self.ancho
    
class Rectangulo(FiguraGeometrica,Color):
    def __init__(self, alto, ancho,color):
        FiguraGeometrica.__init__(self,alto,ancho)
        Color.__init__(self,color)

    def __str__(self):
        return f'Del rectangulo, {FiguraGeometrica.__str__(self)}, {Color.__str__(self)}'
    
    def calcular_area(self):
        return self.alto * self.ancho