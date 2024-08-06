# Permiten transformar de manera programática nuestra clase, es similar a los decoradores de funciones
# (es metaprogramación)
import inspect

def decorador_repr(cls):
    print('1. Se ejecuta el decorador de nuestra clase')
    print(f'Recibimos el objeto de la clase: {cls.__name__}')

    # Revisamos los atributos de la clase con el método vars
    atributos = vars(cls)
    # Iteramos cada atributo
    # for nombre,atributo in atributos.items():
    #     print(f'{nombre}:{atributo}')

    # Revisamos si se ha sobreescrito el método __init__
    if not '__init__' in atributos:
        raise TypeError(f'{cls.__name__} no ha sobreescrito el método __init__')
    
    firma_init = inspect.signature(cls.__init__)
    print(f'Firma del método __init__: {firma_init}')
    # Recuperamos los parámetros, excepto el primero que es self
    parametros_init = list(firma_init.parameters)[1:]
    print(f'Parámetros __init__: {parametros_init}')

    # Revisamos si cada parámetro tiene un método property asociado
    for parametro in parametros_init:
        # Property es un valor de tipo built-in para preguntar si se está utilizando el decorador property  
        es_metodo_property = isinstance(atributos.get(parametro),property)
        if not es_metodo_property:
            raise TypeError(f'No existe el método property para el parámetro proporcionado')
        
    # Crear el método repr dinámicamente
    def metodo_repr(self):
        # Obtenemos el nombre de clase
        nombre_clase = self.__class__.__name__

        # Obtenemos los nombres de las propiedades y sus valores dinámicamente
        # Expresión generadora, para crear nombre_atr=valor_atr
        generador_arg = (f'{nombre}:{getattr(self,nombre)!r}' for nombre in parametros_init)
        lista_arg = list(generador_arg)
        print(f'Lista del generador: {lista_arg}')

        # Creamos la cadena a partir de la lista de argumentos
        argumentos = ', '.join(lista_arg)
        print(f'Argementos del metodo repr: {argumentos}')

        # Creamos la forma del método __repr__
        resultado_metodo_repr = f'{nombre_clase}({argumentos})'

        print(nombre_clase)
        return resultado_metodo_repr
        
    # Agregar dinámicamente el método repr en la clase
    setattr(cls,'__repr__',metodo_repr)

    return cls

@decorador_repr
class Persona:
    def __init__(self,nombre,apellido, edad):
        print('2. Se ejecuta el inicializador')
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre
    
    @property
    def apellido(self):
        return self._apellido
    
    @property
    def edad(self):
        return self._edad
    
    # @nombre.setter
    # def nombre(self,nombre):
    #     self._nombre = nombre

    # @apellido.setter
    # def apellido(self,apellido):
    #     self._apellido = apellido

persona1 = Persona('Augusto','Rivera',40)
print(persona1)
persona2 = Persona('Carla','Gomez',50)
print(persona2)

# Tiene los métodos de property nombre,apellido, repr
print(dir(Persona))

# Tiene el método repr sobreescrito
codigo_repr = inspect.getsource(persona1.__repr__)
print(codigo_repr)