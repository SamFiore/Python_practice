# Una función closure, es una función que encapsula otra función, manteniendo un estado, es decir que las variables locales que definamos en la función principal, van a poder accedidas por la función anidada o más interna
# define a otra función, y además la regresa

# Función principal
def operacion(a,b):
    # Definimos una función interna o anidada
    def sumar():
        return a+b
    
    # Retornar la función
    return sumar

mi_funcion_closure = operacion(5,2)
print(f'Resultado de la función closure: {mi_funcion_closure()}')

# Llamar la función regresada al momento, con '()' al final ejecuta la función anidada 'sumar'
print(f'Resultado de la función closure, pero ejecutada al momento: {operacion(2,3)()}')