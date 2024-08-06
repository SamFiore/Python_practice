# Las tuplas son inmutables

# Declarar variables
a,b = 'Hola','Adios'
print(a,b)

# Swap (intercambio) de estas variables
a,b = b,a
print(a,b)

# Regresar múltiples valores en una función
def minmax(elementos):
    return min(elementos), max(elementos)

min,max = minmax(list(range(1,6)))
print(f'Valor mínimo: {min}, valor máximo: {max}')

# Regresar la suma de una tupla
resultado = sum((1,2,3,4,5))
print(f'Resultado: {resultado}')

def sumar(*args):
    return sum(args)

resultado = sumar(1,2,3,4,5,6)
print(f'Resultado: {resultado}')


