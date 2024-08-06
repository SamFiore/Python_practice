from urllib.request import Request, urlopen
from ssl import _create_unverified_context

contexto = _create_unverified_context()
r = Request('put_patch',headers={'User-Agent': 'Mozilla'}, data= None, unverifiable=False, method='GET')

palabras=[]

with urlopen(url=r,context=contexto) as mensaje :
    contenido = mensaje.read().decode('utf-8')

# Contar ocurrencias de una cadena dentro de otra
# print(contenido.count('Universidad'))

# Convierte a mayúsculas un str
# print(contenido.upper())

# Convierte a minúsculas un str
# print(contenido.lower())

# python
# print('python'.lower() in contenido.lower())

# startswith - inicia con...
print(contenido.startswith('aa'))

# endswith - termina con...
print(contenido.lower().endswith('aaa'.lower()))
# print(contenido)