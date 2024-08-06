#Polimorfismo: multiples formas en tiempo de ejecución

class Empleado:
    def __init__(self,nombre,sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def __str__(self):
        return f' Empleado: [Nombre: {self.nombre} ; Sueldo: {self.sueldo}]; '
    
    def mostrar_detalles(self):
        return self.__str__()
    
class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento):
        Empleado.__init__(self,nombre,sueldo)
        self.departamento = departamento

    def __str__(self):
        return f'{super().__str__()} Gerente [Departamento:{self.departamento}]; '
    
if __name__ == '__main__':
    empleado1 = Empleado('Resputin',200000)
    gerente1 = Gerente('Vladimir',450000,'General')
    print(gerente1)
