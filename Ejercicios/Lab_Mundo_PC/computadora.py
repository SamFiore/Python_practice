from perifericos import *
from monitor import Monitor

class Computadora(Raton,Teclado,Monitor):
    contador_computadoras = 0

    @classmethod
    def sigNum(cls):
        cls.contador_computadoras += 1
        return cls.contador_computadoras
    
    def __init__(self,nombre,marca_perifericos,tipo_entrada,tamanio):
        self.__id_computadora = Computadora.sigNum()
        Raton.__init__(self,marca_perifericos,tipo_entrada)
        Teclado.__init__(self,marca_perifericos,tipo_entrada)
        Monitor.__init__(self,marca_perifericos,tamanio)
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def id_computadora(self):
        return self.__id_computadora

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre

    def __str__(self):
        return f'{self.__nombre}; ID:{self.__id_computadora} \n  Monitor {Monitor.__str__(self)} \n  Teclado {Teclado.__str__(self)} \n  Raton {Raton.__str__(self)} \n'
    
if __name__ == '__main__':
    computadora1 = Computadora('Asus','Logitech','bluetooth',42)
    print(computadora1)