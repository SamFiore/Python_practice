var_global = 'Variable global'

def imprimir():
    # Así trabajamos en una variable global tanto para escritura como lectura
    global var_global
    var_global = 'Nuevo valor de la variable global'

print(f'Variable Global fuera de la función: {var_global}')