# Unir listas
lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = [*lista1,*lista2]
# print(lista3)

# Unir diccionarios
dic1 = {'A':1,'B':2,'C':3}
dic2 = {'D':4,'E':5}
dic3 = {**dic1,**dic2}
# print(dic3)

# Construir una lista a partir de un str
lista = [*'Hola Mundo']
print(lista)
print(*lista, sep='')