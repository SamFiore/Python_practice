# Funciones anidadas

def calculadora(a,b, operacion='sumar'):
    # Función anidada
    # Primero: definir
    def sumar(a,b):
        return a+b
    
    def restar(a,b):
        return a-b

    # Segundo:
    # Llamar a la función anidada
    # Tercero:
    # Retornar el resultado
    if operacion == 'sumar':
        return f'Resultado de sumar: {sumar(a,b)}'
    elif operacion == 'restar':
        return f'Resultado de restar: {restar(a,b)}'

r = 'restar'
s = 'sumar'

print(calculadora(5,6,s))
print(calculadora(7,9,r))