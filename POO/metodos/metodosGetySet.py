class Persona:

    """
     Metodos Get y Set: 
        Get: Nos va a permiter OBTENER/RECUPERAR los atributos de nuestra clase
        Set: Nos va a permitir COLOCAR/MODIFICAR los atributos de nuestra clase
    """

    def __init__(self,nombre,apellido,edad): 
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    #Los decoradores modificar el comportamiento de nuestro metodo
        #Decorador:
    @property
    #Nos ayuda a acceder al método como si fuera un atributo
    #Metodo Get:
    def nombre(self):
        print('Llamando metodo GET nombre')
        return self._nombre
    #Metodo Set:
    @nombre.setter
    def nombre(self,nombre):
        print('Llamando metodo SET nombre')
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self,apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self,edad):
        self._edad = edad

    def showDetails(self):
        print(f'Persona: {self._nombre,self._apellido,self._edad}')

#Comprobamos si se esta ejecutando solo en este módulo, si es así, se ejecutará el código (aquí se ponen los código de pruebas)
if __name__ == '__main__':
    person1 = Persona('Francisco','Lopez',23)

    print(person1.nombre)

    person1.nombre = 'Fausto'

    print(person1.nombre)

    person1.apellido = 'Gonzales'

    person1.edad = 22

    person1.showDetails()

    #Saber el nombre del módulo que se esta ejecutando
    print(__name__) #El nombre de nuestro archivo, nuestro módulo
