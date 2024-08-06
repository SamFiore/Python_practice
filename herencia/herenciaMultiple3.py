from herenciaMultiple import FiguraGeometrica
from herenciaMultiple2 import Color

class Cuadrado(FiguraGeometrica,Color):
    def __init__(self,lado,color):
        # super().__init__(lado)
        #Se utiliza una forma alternativa
        #   se utiliza "self" ya que utilizamos el método "__init__" pero a nivel de la clase
        #       "lado" únicamente se utiliza para inicializar los atributo de "ancho" y "alto"
        FiguraGeometrica.__init__(self,lado, lado)
        Color.__init__(self,color)

    def calcularArea(self):
        return self.ancho * self.alto