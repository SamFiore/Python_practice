# Join = Unir

# help(str.join)
tupla_palabras = ('Hola','mundo','universidad','Python')
resultado = ' '.join(tupla_palabras)
print(resultado)

lista_palabras = ['Hola','perdida','soyio']
resultado = ', '.join(lista_palabras)
print(resultado)

cadena = 'HolaMundo'
resultado = '.'.join(cadena)
print(resultado)

diccionario = {'nombre':'Jonathan','apellido':'Viale','edad':'42'}
llaves = '-'.join(diccionario.keys())
valores = '-'.join(diccionario.values())
print(f'Llaves: {llaves}')
print(f'Valores: {valores}')