from urllib.request import Request, urlopen
from ssl import _create_unverified_context

contexto = _create_unverified_context()
r = Request('put_patch',headers={'User-Agent': 'Mozilla'}, data= None, unverifiable=False, method='GET')

palabras=[]

with urlopen(url=r,context=contexto) as mensaje :
    contenido = mensaje.read().decode('utf-8')


titulo = '| *** Curso de Python *** |'

# Reemplazar contenido en un str
# print(contenido.replace(' ',' :D '))

# Eliminar caracteres al inicio o al final de una cadena
print(titulo.strip('|'))
print(titulo.rstrip('|'))
print(titulo.lstrip('|'))
print(titulo.strip('|').strip().strip('*').strip())