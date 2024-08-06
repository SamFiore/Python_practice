class Clase1:
    def __init__(self):
        print('Clase1.__init__')

    def metodo(self):
        print('Clase1.metodo')

class Clase2(Clase1):
    def __init__(self):
        print('Clase2.metodo()')
        super().__init__()
    
    def metodo(self):
        print('Clase2.metodo()')
        super().metodo()

class Clase3(Clase1):
    def __init__(self):
        print('Clase3.__init__')
        super().__init__()

    def metodo(self):
        print('Clase3.metodo()')
        super().metodo()

class Clase4(Clase2,Clase3):
    def metodo(self):
        print('Clase4.metodo()')
        super().metodo()

# Relación no válida
# class Clase5(Clase2,Clase4):
#     pass

# Creamos un objeto de la clase4
clase4 = Clase4()
# __bases__
print(Clase4.__bases__)
# __mro__
print(Clase4.__mro__)
# Cuál método se ejecuta
clase4.metodo()

