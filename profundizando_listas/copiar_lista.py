numeros1 = [10, 40, 15, 4, 20, 90, 4]

# Copiar los elementos de una lista
numeros2 = numeros1.copy()
# print(f'Lista copiada: {numeros2}')
# print(f'Misma referencia? {numeros1 is numeros2}')
# print(f'Mismo contenido? {numeros1 == numeros2}')

# Podemos usar el constructor de la lista
numeros2 = list(numeros1)
# print(f'Lista copiada: {numeros2}')
# print(f'Misma referencia? {numeros1 is numeros2}')
# print(f'Mismo contenido? {numeros1 == numeros2}')

# Slicing
numeros2 = numeros1[:]
print(f'Lista copiada: {numeros2}')
print(f'Misma referencia? {numeros1 is numeros2}')
print(f'Mismo contenido? {numeros1 == numeros2}')