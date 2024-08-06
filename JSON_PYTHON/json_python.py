# Leer archivo JSON
# JSON = JavaScript Object Notation
import urllib.request
import json

# Debido a cambios en la libreria ahora se deben pasar algunos cabeceros html
peticion = urllib.request.Request(
    'http://globalmentoring.com.mx/api/personas.json',
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)
respuesta = urllib.request.urlopen(peticion)
print(respuesta)
cuerpo_respuesta = respuesta.read()
# print(cuerpo_respuesta)
# Procesamos la respuesta
json_respuesta = json.loads(cuerpo_respuesta.decode('utf-8'))
print(json_respuesta)
print(type(json_respuesta))
print(json_respuesta['personas'][0]['nombre'])
# imprimir solo los nombre de las personas
# JSON se convierte a listas y diccionarios en python
for persona in json_respuesta['personas']:
    print(f'Persona: {persona["nombre"]}')
# Accedemos a las variables independientes
print(f'Total de personas: {json_respuesta["total"]}')
print(f'Mensaje de respuesta: {json_respuesta["mensaje"]}')