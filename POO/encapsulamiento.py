class Persona:
    #El objetivo del encapsulamiento es que no podemos acceder directamiente a los atributos de nuestra clase

    def __init__(self,nombre,apellido,edad): 
        #La manera de restringir un atributo para que no se acceda directamente a estos atributos es con un   '_' antes del nombre del atributo, solo pudiendose acceder dentro de la misma clase
        #     ↓ 
        #self._nombre = nombre

        #Para ser mucho más restrictivos, se utiliza 
        #   '__' de esta forma realmente no se podra acceder ni modificar fuera de la clase, pero no es 
        #    ↓↓                                                                                       común
        self.__nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def showDetails(self):
        print(f'Persona: {self.__nombre,self.apellido,self.edad}')

person1 = Persona('Francisco','Lopez',23)

#No deberiamos acceder al atributo de esta manera y menos modificar sus valores
    # person1._nombre = 'Fausto' -> Aunque esto se puede seguir modificando

#Acá el ejemplo que no se va a modificar aunque no dé error
person1.__nombre = 'Fausto'
person1.showDetails()