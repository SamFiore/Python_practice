# Representación significa generar un string con el estado del objeto
# tipo '__' (str,repr,format)
# print(dir(object))

class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

    # Repr es más enfocado a programadores
    def __repr__(self):
        return f'{self.__class__.__name__}(nombre={self.nombre},apellido={self.apellido})'
    
if __name__ == '__main__':
    persona1 = Persona('Mauricio','Macri')
    # print(persona1)
    # Con !r indicamos el uso del método repr
    print(f'pesona1 : {persona1!r}')
