def funcion_decorador_a(funcion_a_decorar_b):
    def funcion_decorada_c(*args,**kwargs):
        print('Antes de ejecutar la función')
        resultado = funcion_a_decorar_b(*args, **kwargs)
        print('Después de ejecutar la función')
        return resultado

    return funcion_decorada_c

@funcion_decorador_a
def sumar(a,b):
    return a+b

resultado = sumar(4,5)
print(f'Resultado: {resultado}')