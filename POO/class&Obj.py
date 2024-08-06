class Persona:

    #Los atributos que estan fueron de los metodo de tipo dunder son atributos de la clase
    
    #Metodo inicializador (__init__ es un metodo tipo DOUBLE UNDERSCORE/DUNDER, los atributos dentro de este van a pertenecer a los atributos de nuestro objeto)

    def __init__(self,nombre,apellido,edad, *args, **kwargs): 
    
        #Acá se agregan los parametros, esto se llama agregar atributos de intancia o de objetos (intancia = creación de un objeto)
    
        #atributo     parametro
        #   |            |
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = args
        self.terminos = kwargs

    #Se conocen como métodos de intancia a todos los metodos que se asocian con los objetos que creamos, todos estos contienen (self)
        
        #No necesariamente debe llamarse self, pero la documentación lo recomiendo, mientras este como primer parametro

    def showDetails(self):
        print(f'Persona: {self.nombre,self.apellido,self.edad} {self.valores} {self.terminos}')


"""
Estructura de una clase 
                Nombre de la clase
                -----------------
                | Atributo      |
                -----------------
                | Métodos       |
                -----------------
 Buscar UML - Unified Modeling Language (Se utiliza para documentar Clases, Objetos, etc.)
"""
        
person1 = Persona('Francisco','Lopez',23, '53453532', 10, 22, 33, m='manzana',b='banana',p='pera')
# person1.showDetails()
Persona.showDetails(person1) #Otra forma de acceder a los parametros
person1.nombre,person1.edad,person1.apellido = 'Juan Carlos',20,'Magno'
person1.showDetails()
#Se pueden agregar nuevos atributo a las clases pero no se comparten con otros objetos
person1.telefono = '33221144'
print(person1.telefono)


person2 = Persona('Luna','Estellis',23)
person2.showDetails()
# print(person2.telefono)
