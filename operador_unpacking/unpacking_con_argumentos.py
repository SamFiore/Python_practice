numeros = [1,2,3,4,5,6,7]

# Desempaquetando al momento de pasar un parámetro a un función
def suma(*args):
    resultado = 0
    for x in args:
        resultado += x
    print(f'Resultado de la suma: {resultado}')

suma(*numeros)

# Extraer algunos elementos de una lista

mi_lista = list(range(1,7))
a,*_,c,d = mi_lista
print(a,c,d, sep='-')
