try:
    archivos = open('prueba.txt','w', encoding='utf8') #El método open() nos sirve para crear y abrir archivos, también podemos indicar parámetros para leer info de un archivos o escribir info en un archivo [W: sirve para escribir un archivo - write]
    archivos.write('Escribimos de información en el archivos\n') # Método write() sirve para escribir en el archivo
    archivos.write('Adios')
except Exception as e:
    print(e)
finally:
    archivos.close() # Método close() sirve para cerrar archivos