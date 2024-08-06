from polimorfismo.polimorfismo import *

def imprimir_detalles(obj):
    # print(obj)
    print(obj.mostrar_detalles())
    print(type(obj))
    if isinstance(obj,Gerente):
        print(obj.departamento)

empleado1 = Empleado('Fausto',200000)
imprimir_detalles(empleado1)
gerente1 = Gerente('Agustin',350000,'General')
imprimir_detalles(gerente1)
