class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

    # Repr es más enfocado a programadores
    def __repr__(self):
        return f'{self.__class__.__name__}(nombre={self.nombre},apellido={self.apellido})'
    
    # str, es para el usuario final o para otros sistemas
    # la implementación por default llama al método str
    def __str__(self):
        return f'{self.__class__.__name__}: {self.nombre} {self.apellido}'
    
    def __format__(self, format_spec):
        return f'{self.__class__.__name__} con nombre {self.nombre} y apellido {self.apellido}'


if __name__ == '__main__':
    persona1 = Persona('Mauricio','Macri')
    print(f'pesona1 : {persona1!r}')
    # str se llama de manera automática a través del método print
    print(persona1)
    # format se llama de manera automática con un f-string
    print(f'{persona1}')