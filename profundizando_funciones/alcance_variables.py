# Alcance de viariable (Scope), son los lugares donde podemos utilizar una variables, o sea, el tiempo de vida de una variable

# Una VARIABLE GLOBAL es una variables que se define fuera de la función 
var_global = 'Variable global'

def imprimir():
    # Acceder a una variable global
    # Así trabajamos en una variable global tanto para escritura como lectura
    global var_global
    print(f'Variable global desde una función: {var_global}')
    
    # Una variable definida dentro de un bloque de función, solo existe dentro del bloque
    # O sea, es una VARIABLE LOCAL
    var_local = 'Variable local'
    print(f'Variable local desde la función: {var_local}')
    var_global = 'Nuevo valor de la variable global'

    def funcion_anidada():
        print(f'Variable local desde la función anidada: {var_local}')
    funcion_anidada()

imprimir()
print(f'Variable Global fuera de la función: {var_global}')
# print(f'Variable Local fuera de la función: {var_local}') Este da error, porque solo existe de manera local en la función
