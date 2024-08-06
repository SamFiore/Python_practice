x = int(input('Como estuvo tu dia? (en numeros): '))

try:
    if(x <= 10):
        if(x == 10):
            print('Tu dia estuvo excelente')
        elif(10 > x >= 6):
            print('Tu dia estuvo nice')
        elif(6 > x >= 4):
            print('Tu dia estuvo intermedio')
        else:
            print('Tu dia te fue para el culo, anda y buscate un psicologo lpm')
    else:
        print('El numero no es el pedido, debe ser del 1 al 10')
except ValueError:
    print('El dato no es valido, pt')
