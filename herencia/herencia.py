class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona: [NOMBRE: {self.nombre}, EDAD: {self.edad}]'

class Empleado(Persona):
    def __init__(self,nombre,edad,sueldo):
        # super() se utiliza para acceder al constructor de la clase padre
        super().__init__(nombre,edad)
        self.sueldo = sueldo
    
    def __str__(self):
        return f'Empleado: [SUELDO: {self.sueldo}]; {super().__str__()}'

if __name__ == '__main__':
    empleado1 = Empleado('Alberto',23,200000)
    print(empleado1.nombre)