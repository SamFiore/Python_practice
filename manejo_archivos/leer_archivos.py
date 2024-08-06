try:
    archivos = open('prueba.txt','r',encoding='utf8')
    # print(archivos.read())

    # Leer algunos cáracteres
    # print(archivos.read(5))
    # print(archivos.read(3))

    # Leer líneas completas
    # print(archivos.readline())

    # Iterar el archivo
    # for linea in archivos:
    #     print(linea)

    # Leer todas las líneas
    # print(archivos.readlines())

    # Acceder a una línea específica
    # print(archivos.readlines()[1])

    # Abrimos un nuevo archivo
    # a - anexar información
    archivos2 = open('copia.txt','a',encoding='utf8')
    archivos2.write(archivos.read())
except Exception as e:
    print(e)
finally:
    archivos.close()
    archivos2.close()
    print('Se ha terminado el proceso de leer y copiar archivos')