# Ejemplo de herencia múltiple

class ListaSimple:
    def __init__(self,elementos):
        self._elementos = list(elementos)

    def agregar(self, elemento):
        self._elementos.append(elemento)

    def __getitem__(self,indice):
        return self._elementos[indice]
    
    def ordernar(self):
        return self._elementos.sort()
    
    def __len__(self):
        return len(self._elementos)
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self._elementos!r})'
    
class ListaOrdenada(ListaSimple):
    def __init__(self,elementos=[]):
        super().__init__(elementos)
        self.ordernar()

    def agregar(self, elemento):
        super().agregar(elemento)
        self.ordernar()
    
class ListaEnteros(ListaSimple):
    def __init__(self,elementos=[]):
        for elemento in elementos:
            self._validar(elemento)
        super().__init__(elementos)

    def _validar(self,elemento):
        if not isinstance(elemento,int):
            raise ValueError(f'El número {elemento} no es un valor entero')
        
    def agregar(self, elemento):
        self._validar(elemento)
        super().agregar(elemento)

class ListaEnterosOrdenados(ListaEnteros,ListaOrdenada):
    pass

if __name__ == '__main__':
    lista_simple = ListaSimple([5,3,6,8])
    # print(lista_simple)
    lista_ordenada = ListaOrdenada([9,7,5,3,0,1])
    # print(lista_ordenada)
    lista_ordenada.agregar(6)
    # print(lista_ordenada)
    # print(len(lista_ordenada))
    lista_enteros = ListaEnteros([7,2,23,8,0])
    # print(lista_enteros)
    lista_enteros.agregar(4)
    # print(lista_enteros)

    # Lista de enteros ordenados
    lista_enteros_ordenados = ListaEnterosOrdenados([2,5,4,2,1,7,3])
    print(lista_enteros_ordenados)
    lista_enteros_ordenados.agregar(23)
    print(lista_enteros_ordenados)

    # Saber las clases padres y su orden
    print(ListaEnterosOrdenados.__bases__)
    # MRO (Method Resolution Order)
    print(ListaEnterosOrdenados.__mro__)
