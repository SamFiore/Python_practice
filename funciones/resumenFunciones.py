def suma(x,y):
    return x+y

#No hace falta asignar el resultado a una variable
print(f'El resultado de la suma es {suma(3,4)}')

#Valores default de la función 
#Podemos usar una función tipo flecha para indicar que el tipo de dato a regresar es indicado (solo es una pista pero no lo regresa de manera estricta)
def suma2(x = 0,y = 5) -> int:
    return x+y

#Si no se asigna ningún número el valor por determinado es 0 u otro número índicado
print(f'El resultado de la suma es {suma2(2,)}')

#Argumentos variables en las funciones
#El *args (en la doc de python es común encontrarlo así pero no es requerido usar ese nombre como argumento) genera una tupla donde se contendran las variables (no sabemos cuantas son)
def listNombres(*nombres):
    for nombre in nombres:
        print(nombre)

listNombres('Pablo','Ariel','Benja','Escarlata','Anais')

def sumar(*args):
    resultado = 0
    for x in args:
        resultado += int(x)
    return resultado

print(f'La suma de los números es {sumar(2,4,8,8,12)}')

def sumar2(*args):
    resultado = 1
    for x in args:
        resultado *= int(x)
    return resultado

print(f'La suma de los números es {sumar2(2,4,8,8,12)}')

#Como pasar dict en vez de tuplas en args de las funciones
#En la doc de python se suelen llamar kwargs, pero no es obligatorios
def listarTerminos(**terminos):
    for llave,valor in terminos.items():
        print(f'{llave}:{valor}')

listarTerminos(Pato='Animal',Vaso='Objeto',Hola='Saludo')
