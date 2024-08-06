class OrdenComputadoras:
    contador_ordenes = 0

    @classmethod
    def sigNum(cls):
        cls.contador_ordenes += 1
        return cls.contador_ordenes
    
    def __init__(self,computadoras):
        self.__id_orden = OrdenComputadoras.sigNum()
        self.__computadoras = list(computadoras)

    def agregarComputadora(self,computadora):
        self.__computadoras.append(computadora)

    @property
    def id_orden(self):
        return self.__id_orden
    
    @property
    def lista_computadoras(self):
        return self.__computadoras
    
    def __str__(self):
        computadora_str = ''
        for computadora in self.__computadoras:
            computadora_str += computadora.__str__()

        return f'Orden:{self.__id_orden} \n Computadoras: \n {computadora_str}'

        


