a1 = 'Hola '
b1 = 'mundo'

print(a1 + b1)

a2 = 20
b2 = 30

print(a2 + b2)

a3 = [1,2,3]
b3 = [4,5,6]
print(a3 + b3)

class Persona: 
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, other):
        return f'{self.nombre} {other.nombre}'
    
    def __sub__(self, other):
        return self.edad - other.edad
    
persona1 = Persona('Alejando',30)
persona2 = Persona('Augusto',20)
print(persona1 + persona2)
print(persona1 - persona2)
