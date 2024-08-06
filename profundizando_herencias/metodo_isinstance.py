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

lista_enteros_ordenados = ListaEnterosOrdenados([2,5,4,2,1,7,3])

print(f'Es entero?: {isinstance(10,int)}')
print(f'Es cadena?: {isinstance("Hola Mundo",str)}')
print(f'Es list ent ord: {isinstance(lista_enteros_ordenados,ListaEnterosOrdenados)}')
print(f'Es list ent: {isinstance(lista_enteros_ordenados,ListaEnteros)}')
print(f'Es lista simple: {isinstance(lista_enteros_ordenados,ListaSimple)}')
print(f'Es object: {isinstance(lista_enteros_ordenados,object)}')
print(f'Es de varios tipo: {isinstance(lista_enteros_ordenados,(ListaEnteros,ListaSimple))}')