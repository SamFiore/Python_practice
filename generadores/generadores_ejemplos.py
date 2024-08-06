# Generador de números del 1 al 5
def generador_numeros():
    for numero in range(1,6):
        yield numero
        print('Se reanuda la ejecución')

# Utilizamos el generador
generador = generador_numeros()
print(f'Objeto generado: {generador}')
print(type(generador))

# Consumimos los valores del generador
print(generador)
for valor in generador:
    print(f'Número producido: {valor}')

# Consumir a demanda 
generador = generador_numeros()
try:
    print(f'Consumimos a demanda: {next(generador)}')
    print(f'Consumimos a demanda: {next(generador)}')
    print(f'Consumimos a demanda: {next(generador)}')
except StopIteration as si:
    print(f'Error a consumir generador: {si}')

print('')
# Otra forma de consumir un generador 
generador = generador_numeros()
while True:
    try:
        valor = next(generador)
        print(f'Consumimos generador: {valor}')
    except StopIteration as si:
        print(f'Se terminó de iterar el generador')
        break