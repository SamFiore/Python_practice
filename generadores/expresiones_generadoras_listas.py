# También podemos usar una lista o cualquier otro iterador
lista = ['Juan','Perez']
generador = (valor for valor in lista)
print(f'Valor de generador en lista: {next(generador)}')
print(f'Valor de generador en lista: {next(generador)}')

# Crear un str a partir de un generador y este creado a partir de una lista
lista = ['Karla','Gomez', 22]
contador = 0
# Definimos una función para incrementar el contador
def incrementar():
    global contador
    contador += 1
    return contador

# La primera parte es el yiel de nuestro generador y la segunda parte es el for, entre parentesis
generador = (f'{incrementar()}. {nombre}' for nombre in lista)
lista = list(generador)
print(lista)
cadena = ', '.join(lista)
print(f'Cadena generada: {cadena}')