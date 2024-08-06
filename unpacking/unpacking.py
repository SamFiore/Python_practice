# Unpacking - Desempaquetado
# Podemos de lado derecho podemos asignar una lista o tupla de valores y de lado izquierdo podemos asignar esos valores en variables independientes
valores = 1,2,3
# print(valores)
# print(type(valores))

valor1, valor2, valor3 = 1,2,3
# print(f'valor1: {valor1}, valor2: {valor2}, valor3: {valor3}')

# Como asignar un valor que no se usará, el '_' omite su uso
valor1, _, valor3 = 1,2,3
# print(f'valor1: {valor1}, valor3: {valor3}')

valor1, valor2, *valor3 = 1,2,3,4,5,6,7,8,9
# print(f'valor1: {valor1}, valor2: {valor2}, valor3: {valor3}')

valor1, valor2, *valor3, valor4, valor5 = 1,2,3,4,5,6,7,8,9
# print(f'valor1: {valor1}, valor2: {valor2}, valor3: {valor3}, valor4: {valor4}, valor5: {valor5}')

def regresa_varios_datos():
    return 1,2,3

valor1,valor2,valor3 = regresa_varios_datos()
# print(f'valor1: {valor1}, valor2: {valor2}, valor3: {valor3}')

# help(str.partition)

hora, _, minutos = '17:20'.partition(':')
print(f'Hora: {hora}, minutos: {minutos}')
