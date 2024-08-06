class Persona:
    def __init__(self,nombre,apellido,edad): 
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        print('Llamando metodo GET nombre')
        return self._nombre

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

    #Método destructor
    def __del__(self):
        print(f'Persona: {self._nombre} {self._apellido}')

if __name__ == '__main__':
    person1 = Persona('Francisco','Lopez',23)

    print(person1.nombre)

    person1.nombre = 'Fausto'

    print(person1.nombre)

    person1.apellido = 'Gonzales'

    person1.edad = 22

    person1.showDetails()

    print(__name__)