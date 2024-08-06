# Función principal
def operacion(a,b):
    # 1. Definimos una función lambda interna o anidada y la retornamos
    return lambda: a+b

mi_funcion_closure = operacion(2,3)
print(f'Resultado lambda y closure: {mi_funcion_closure()}')

print(f'Resultado lambda y closure, al momentos: {operacion(2,3)()}')