# Es una función especial en python que permite regresar una secuencia de valores, pero no al mismo tiempo, si no, por medio de la palabra yield (producir), vamos a ir regresando poco a poco los valores en una secuencia

# Es una función especial, retorna una secuencia de valores
# suspende la ejecución de la función yield (no se usa return)

def generador():
    yield 1
    print('Se reanuda la ejecución')
    yield 2
    print('Se reanuda la ejecución')
    yield 3

# Consumimos el generador a demanda (solo los que vayamos necesitando)
gen = generador()
# Con cada llamada consumimos un valor
# print(next(gen))
# print(next(gen))
# print(next(gen))
# Si tratamos de consumir más valores de los que produce el generador, se lanza un error de StopIteration
# print(next(gen))
for x in range(1,4):
    print(next(gen))

for x in generador():
    print(f'Numero: {x}')