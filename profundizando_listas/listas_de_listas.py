# Lista multiplicación
lista_multiplicacion = 5*[[2,3]]
# print(lista_multiplicacion)
# print(f'Misma referencia? : {lista_multiplicacion[0] is lista_multiplicacion[1]}')
# print(f'Misma contenido? : {lista_multiplicacion[0] == lista_multiplicacion[1]}')
# Modifica todos los objetos de la lista, porque apuntan a las misma referencia
lista_multiplicacion[2].append(10)
# print(lista_multiplicacion)

# Matrices en python
# Las matrices son lista de listas
matriz = [[10, 20],[30,40,50],[60,70,80,90]]
# print(f'Matriz original: {matriz}')
# print(f'Renglón 0, columna 0: {matriz[0][0]}')
# print(f'Renglón 2, columna 2: {matriz[2][3]}')
matriz[2][0] = 100
# print(f'Matriz modificada: {matriz}')

# Ordenar una matriz
lista_listas = [[10,14,87,90,71],[4,5,6,7],[9,0,11,15,45,61,70]]
lista_listas.sort(key=len)
# print(f'Lista de listas ordenada: {lista_listas}')

# Sorted built-in / built-in (que son parte de python)
# help(sorted)
nombres1 = ['Antonella','Maximiliano','Ezequiel','Juan','Ivan', 'Franco']
nombres1 = sorted(nombres1)
print(f'Lista ordenada (ascendente) {nombres1}')
nombres1 = sorted(nombres1, reverse=True)
print(f'Lista ordenada (descendente) {nombres1}')

# Ordenar por cant. carácteres (largo)
nombres1 = sorted(nombres1,key=len)
print(f'Lista ordenada (ascendente con len): {nombres1}')

# built-in tipo reversed
nombres1 = reversed(nombres1)
print(f'Lista ordenada (descendente con reversed): {list(nombres1)}')

