lista = [1,2,3,4]
tupla = (4,3,2,1)

#La lista se puede modificar
lista[3] = 5
print(lista)

#La tupla no se puede modificar al menos que se pase a list
# tupla[3] = 0
print(tupla)

#Se puede modificar el print con parametros como end=
for num in lista:
    print(num, end=' ')

#Se puede eliminar de la memoria con del al principio

# del tupla
# del lista
# print(tupla)
# print(lista)