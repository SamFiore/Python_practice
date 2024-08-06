from urllib.request import Request, urlopen
from ssl import _create_unverified_context

contexto = _create_unverified_context()
r = Request('path',headers={'User-Agent': 'Mozilla'}, data= None, unverifiable=False, method='GET')

palabras=[]

with urlopen(url=r,context=contexto) as mensaje :
    contenido = mensaje.read().decode('utf-8')


    # for linea in mensaje:
    #     palabras_por_linea = linea.decode('utf-8').split()
    #     # print(palabras_por_linea)
    #     for palabra in palabras_por_linea:
    #         palabras.append(palabra)

# print(palabras)

with open('contenido_online.txt','w', encoding='utf-8') as archivo:
    archivo.write(contenido)