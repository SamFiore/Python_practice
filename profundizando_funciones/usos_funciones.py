# Las funciones en python son ciudadanas de primer clase
# First class citizens

# Definimos una función
def sumar(a,b):
    return a+b

# 1. Asignar una función a una variable (No se usan parentesis)
mi_funcion = sumar

# Verificar el tipo de la variable
print(type(mi_funcion))

# Llamamos la función a través de la variable
print(f'Resultado de sumar: {mi_funcion(5,4)}')

# 2. Función como argumento
def operacion(a,b,sumar_arg):
    print(f'Resultado de sumar: {sumar_arg(a,b)}')

operacion(6,5,sumar)

# 3. Retornar una función desde otras funciones
def retornar_funcion():
    # Retornamos una funcion
    return sumar

mi_funcion_retornada = retornar_funcion()
print(f'Resultado de la función retornada: {mi_funcion_retornada(8,9)}')