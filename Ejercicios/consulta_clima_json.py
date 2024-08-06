import urllib.request
import json

peticion = urllib.request.Request('path_.json',data=None,headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
respuesta = urllib.request.urlopen(peticion)
cuerpo_respuesta = respuesta.read()
json_respuesta = json.loads(cuerpo_respuesta.decode('utf-8'))
# print(json_respuesta)
on = True
while on:
    print('''
        
        Menu
        1- Temperatura máxima
        2- Temperatura mínima
        3- Descripción del día
        4- Salir
        
        ''')
    opcion = int(input('Escribe tu opción: '))
    if opcion == 1:
        print(f'La temperatura máxima es: {json_respuesta["principal"]["temp_max"]}')
    elif opcion == 2:
        print(f'La temperatura máxima es: {json_respuesta["principal"]["temp_min"]}')
    elif opcion == 3:
        print(f'La descripción de la temperatura de hoy es: {json_respuesta["clima"][0]["descripcion"]}')
    elif opcion == 4:
        on = False
    else: 
        print(f'El valor {opcion} no es válido, ingreso un número de las opciones')