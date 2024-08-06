class Monitor:
    contador_monitores = 0

    @classmethod
    def sigNum(cls):
        cls.contador_monitores += 1
        return cls.contador_monitores
    
    def __init__(self,marca,tamanio):
        self.__id_monitor = Monitor.sigNum()
        self.__marca = marca
        self.__tamanio = tamanio

    @property
    def marca(self):
        return self.__marca
    
    @property
    def tamanio(self):
        return self.__tamanio
    
    @property
    def id_monitor(self):
        return self.__id_monitor
    
    @marca.setter
    def marca(self,marca):
        self.__marca = marca
    
    @tamanio.setter
    def tamanio(self,tamanio):
        self.__tamanio = tamanio
    
    def __str__(self):
        return f'ID:{self.__id_monitor} [Marca:{self.__marca}; Tamanio: {self.__tamanio} pulgadas]'