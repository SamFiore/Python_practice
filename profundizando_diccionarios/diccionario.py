# Los diccionarios guardan un orden (A diferencia de un set)
diccionario = {'Nombre':'Pedro','Apellido':'Gonzales','Edad':30}
# print(diccionario)

# En los diccionarios son mutables pero las llaves son inmutables
# diccionario = {[1,2]:'valor1'}

# Se agrega una llave con su valor si no se encuentra
diccionario['Departamento'] = 'Sistemas'
# print(diccionario)

# Si la llave existe, el valor se modifica
diccionario['Nombre'] = 'Alberto'
# print(diccionario)

# Recuperar un valor indicando una llave
# print(diccionario['Nombre'])
# Si no lo encuentra, arroja una excepción
# print(diccionario['nombre'])

# Método get, recupera una llave y si no existe, NO lanza excepción
# además podemos regresar un valor en caso que no exista la llave
# print(diccionario.get('Nombre', 'No se encontró la llave'))
# print(diccionario.get('Casa', 'No se encontró la llave'))

# Método setdefault si modifica el diccionario en caso que no encuetre la llave y además agrega un valor por default si no llegase a encontrarla
# print(diccionario.setdefault('Nombre','Aconcagua 4532'))
print(diccionario.setdefault('Casa','Aconcagua 4532'))
print(diccionario)

# Imprimir con pprint
from pprint import pprint as pp
# help(pp)
# pp(diccionario)
pp(diccionario, sort_dicts=False)