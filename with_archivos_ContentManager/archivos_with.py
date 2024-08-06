from manejo_recursos import ManejoArchivos

# 'with' abre y cierra automáticamente los archivos
#   esto se conoce como Context Manage o Administrador de Recursos

# with open('C:\\users\\franc\\Escritorio\\Programacion\\PythonUdemy\\manejo_archivos\\prueba.txt','r',encoding='utf8') as archivo:
#     print(archivo.read())

with ManejoArchivos('C:\\users\\franc\\Escritorio\\Programacion\\PythonUdemy\\manejo_archivos\\prueba.txt') as archivos:
    print(archivos.read())
