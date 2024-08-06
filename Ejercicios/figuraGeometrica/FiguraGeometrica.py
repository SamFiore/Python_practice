#ABC = Abstract Base Clase
from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, alto, ancho):
        if self._validarValor(alto):
            self._alto = alto
        else:
            self._alto = 0
        if self._validarValor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0

    def __str__(self):
        return f'el alto es {self._alto} y su ancho es {self._ancho}'

    @property
    def alto(self):
        return self._alto

    @property
    def ancho(self):
        return self._ancho

    @alto.setter
    def alto(self, alto):
        if self._validarValor(alto):
            self._alto = alto
        else:
            self._alto = 0

    @ancho.setter
    def ancho(self, ancho):
        if self._validarValor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0

    @abstractmethod
    def calcularArea(self):
        pass

    def _validarValor(self, valor):
        return True if 0 < valor <= 10 else False
    
