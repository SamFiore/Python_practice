# Bool contiene los valores True / False 
# Tipos numericos, False = 0, True demás valores
valor = 0
resultado = bool(valor)
# print(f'El resultados del valor {valor} es {resultado}')
valor = 20
resultado = bool(valor)
# print(f'El resultados del valor {valor} es {resultado}')

# Tipo str, False para '', True demás valores
valor = ''
resultado = bool(valor)
# print(f'El resultados del valor {valor} es {resultado}')
valor = 'pingüino'
resultado = bool(valor)
# print(f'El resultados del valor {valor} es {resultado}')

# Tipo colecciones, False para colecciones vacías, True para las demás colecciones
# Lista 
valor = []
resultado = bool(valor)
# print(f'El resultados del valor {valor} es {resultado}')
valor = [1,2,3,4]
resultado = bool(valor)
# print(f'El resultados del valor {valor} es {resultado}')
# Tupla
valor = ()
resultado = bool(valor)
# print(f'El resultados del valor {valor} es {resultado}')
valor = (1,)
resultado = bool(valor)
# print(f'El resultados del valor {valor} es {resultado}')
# Diccionario
valor = {}
resultado = bool(valor)
# print(f'El resultados del valor {valor} es {resultado}')
valor = {'id':1}
resultado = bool(valor)
# print(f'El resultados del valor {valor} es {resultado}')

variable = ''

if bool(''):
    print('Es verdadero')
else: 
    print('Es falso')

if variable:
    print('Es verdadero')
else: 
    print('Es falso')
