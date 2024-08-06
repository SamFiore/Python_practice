# Set es una lista desordenada a la cual no se puede modificar elementos ni repetir, pero si agregar o eliminar´
planetas = {'Marte','Jupiter','Urano'}
for planeta in planetas:
    print(planeta)

# Revisar si el item esta en el set
print('Marte' in planetas)

#Agregar un elemento
planetas.add('Tierra')
print(planetas)
# planetas.add('Tierra')
# print(planetas) no se vuelve a repetir

#Eliminar un elemento
planetas.remove('Marte')
print(planetas)
#Eliminar un elemento sin error si no esta
planetas.discard('Luna')
print(planetas)

#Limpiar el set
planetas.clear()
print(planetas)

#Eliminar de la memoria el set
del planetas
print(planetas)
