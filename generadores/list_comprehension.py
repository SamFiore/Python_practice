numeros = range(10)
lista_pares = []

# Creamos una nueva lista con los valores pares, multiplicados por si mismos
for numero in numeros:
    # Revisamos si es número par
    if numero % 2 == 0:
        lista_pares.append(numero*numero)

print(f'Lista de pares: {lista_pares}')

# Hacemos lo mismo con list comprehensions
# [expresion for var in colección if condicion]
lista_pares = []
lista_pares = [numero*numero for numero in numeros if numero%2==0]
print(f'Lista de pares: {lista_pares}')

# Un ejemplo similar con dos condiciones (las condiciones son opcionales)
# Solo se agrega el valor a la lista cuando el valor cumple ambas condiciones
# Es decir, debe ser un número divisible entre 2 y 6
lista_pares = []
lista_pares = [numero for numero in range(50) if numero%2==0 and numero%6==0]
print(f'Lista divisible por 2 y 6: {lista_pares}')

# Agregamos if else
lista_pares = []
lista_impares = []
for numero in range(9):
    if numero%2==0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

print(f'Lista de pares: {lista_pares} y lista de impares: {lista_impares}')

# El mismo ejercicio usando list comprehension
lista_pares = []
lista_impares = []
# expresion condición expresion for var in colección
[lista_pares.append(numero) if numero%2==0 else lista_impares.append(numero) for numero in range(10)]
print(f'Lista de pares: {lista_pares} y lista de impares: {lista_impares}')

# Listas anidadas con list comprehension
# Lista de listas
lista_listas = [[1,2,3],[4,5,6],[7,8,9,10]]
# Convertimos la lista de listas en una sola lista
lista_simple = [valor for sublista in lista_listas for valor in sublista]
print(f'Lista simple: {lista_simple}')

# Ahora creeamos una lista de números pares a partir de una lista de listas
# Sin list comprehension, ciclos for anidados
lista_pares = []
for sublista in lista_listas:
    for valor in sublista:
        if valor%2==0:
            lista_pares.append(valor)

print(f'Lista pares: {lista_pares}')
# Con list comprehension
lista_pares = []
lista_pares = [valor for sublista in lista_listas for valor in sublista if valor%2==0]
print(f'Lista pares: {lista_pares}')
