#Una función recursiva es una función que se llama a si misma para completar una tarea
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)
    
numero = 5
resultado = factorial(int(numero))
print(f'El resultado del factorial de {numero} es {resultado}')

def cuentaRegresiva(num):
    if num == 1:
        print(1)
    elif num <= 0:
        print("Valor incorrecto")
    else:
        print(num)
        return cuentaRegresiva(num - 1)
    
    
cuentaRegresiva(5)