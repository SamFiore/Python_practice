from perifericos import *
from monitor import Monitor

class Computadora:
    contador_computadoras = 0

    @classmethod
    def sigNum(cls):
        cls.contador_computadoras += 1
        return cls.contador_computadoras
    
    def __init__(self,nombre,monitor,teclado,raton):
        self.__id_computadora = Computadora.sigNum()
        self.__nombre = nombre
        self.__monitor = monitor
        self.__teclado = teclado
        self.__raton = raton

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def monitor(self):
        return self.__monitor
    
    @property
    def teclado(self):
        return self.__teclado
    
    @property
    def raton(self):
        return self.__raton
    
    @property
    def id_computadora(self):
        return self.__id_computadora

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre

    @monitor.setter
    def monitor(self,monitor):
        self.__monitor = monitor

    @teclado.setter
    def teclado(self,teclado):
        self.__teclado = teclado

    @raton.setter
    def raton(self,raton):
        self.__raton = raton

    def __str__(self):
        return f'''
        {self.__nombre} ; ID: {self.__id_computadora}
                Monitor: {self.__monitor}
                Teclado: {self.__teclado}
                Raton: {self.__raton}

        '''
    
if __name__ == '__main__':
    pass