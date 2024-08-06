# Ejemplo de herencia simple

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
        # Ordenamos siempre los elementos una vez inicializados
        self.ordernar()

    def agregar(self, elemento):
        super().agregar(elemento)
        # Ordenamos el nuevo elemento
        self.ordernar()
    
class ListaEnteros(ListaSimple):
    def __init__(self,elementos=[]):
        for elemento in elementos:
            self._validar(elemento)
        # Una vez válidados los elementos los agregamos al atributo definido en la clase padre
        super().__init__(elementos)

    def _validar(self,elemento):
        # Validos si el elemento es de tipo enter
        if not isinstance(elemento,int):
            raise ValueError(f'El número {elemento} no es un valor entero')
        
    # Sobreescribimos el método agregar de la clase padre
    def agregar(self, elemento):
        self._validar(elemento)
        # Una vez válidado, lo agregamos
        super().agregar(elemento)

if __name__ == '__main__':
    lista_simple = ListaSimple([5,3,6,8])
    # print(lista_simple)
    lista_ordenada = ListaOrdenada([9,7,5,3,0,1])
    # print(lista_ordenada)
    lista_ordenada.agregar(6)
    # print(lista_ordenada)
    # print(len(lista_ordenada))
    lista_enteros = ListaEnteros([7,2,23,8,0])
    print(lista_enteros)
    lista_enteros.agregar(4)
    print(lista_enteros)
