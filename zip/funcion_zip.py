# La función zip nos permite unir una o más iterables y mezclarlos
# print(dir(__builtins__))
# help(zip)
# Se va iterar y frenar dependiendo la cantidad de la lista con menor elementos
numeros = [1,2,3]
letras = ['a','b','c','d']
identificadores = 321, 322, 323, 324, 325
conjunto = {6,4,0,9,8,15,10}
mezcla = zip(numeros,letras,identificadores, conjunto)
# print(f'Mezcla: {list(mezcla)}')
# print(f'Mezcla: {tuple(zip(numeros,letras))}')
# print(type(mezcla))

for numero,letra,id,aleatorio in zip(numeros,letras,identificadores,conjunto):
    # print(f'Número: {numero}, letra {letra}, ID {id}, aleatorio; {aleatorio}')
    pass

nueva_lista = []
for numero,letra,id,aleatorio in zip(numeros,letras,identificadores,conjunto):
    nueva_lista.append(f'{id}-{numero}-{letra}-{aleatorio}')

# print(nueva_lista)

letras = ['c','d','a','e','b']
numeros = [3,2,4,1,0]
mezcla = tuple(zip(letras,numeros))
# print(f'Zip sin ordenar: {mezcla}')
# print(f'Zip ordenado por letra: {sorted(zip(letras,numeros))}')
# print(f'Zip ordenado por número: {sorted(zip(numeros,letras))}')

# Crear un diccionario con zip y dos iterables
llaves = ['Nombre','Apellido','Edad']
valores = ['Juan','Perez',18]
diccionario = dict(zip(llaves,valores))
print(f'Diccionario con zip: {diccionario}')
# print(type(diccionario))

# Actualizar un elemento del diccionario 
# Se puede actualizar siempre algún contenido de los diccionario con la función 'update', si el elemento existe los modifica y si el elemento no existe lo crea
llave = ['Edad']
nuevas_edad = [28]
diccionario.update(zip(llave,nuevas_edad))
print(f'Diccionario actualizado: {diccionario}')
