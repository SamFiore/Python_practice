diccionario = {'Hola':'Saludo','Pato':'Animal','Vaso':'Objeto'}

#Recorrer keys y valores
for x,y in diccionario.items():
    print(x, '' , y)

#Recorrer las keys
for x in diccionario.keys():
    print(x)

#Recorrer los valores
for x in diccionario.values():
    print(x)

#Comprobar si existe en el dict
print('Hola' in diccionario)


#Agregar un item
diccionario['Ayuda'] = 'Pedido'
print(diccionario)

#Remover un item
diccionario.pop('Hola')
print(diccionario)

#Limpiar el dict
diccionario.clear()
print(diccionario)
