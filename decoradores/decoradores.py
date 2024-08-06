# Los decoradores, nos permite extender funcionalidad, recibiendo una función como parámetro y regresando otra función

# 1. Función decorador (a)
# 2. Función a decorar (b)
# 3. Función decorada (c)

def funcion_decorador_a(funcion_a_decorar_b):
    def funcion_decorada_c():
        print('Antes de ejecutar la función')
        funcion_a_decorar_b()
        print('Después de ejecutar la función')

    return funcion_decorada_c

@funcion_decorador_a
def mostrar_mensaje():
    print('Hola desde la función mostrar_mensaje')

mostrar_mensaje()