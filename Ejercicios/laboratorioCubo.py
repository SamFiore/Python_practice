class Cubo:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    
    def calcularVolumen(self):
        return self.x * self.y * self.z
    
anchura = int(input('Colocar el ancho: '))
altura = int(input('Colocar el alto: '))
profundida = int(input('Colocar la profundidad: '))

cubo1 = Cubo(anchura,altura,profundida)
print(f'El volumen del cubo es: {cubo1.calcularVolumen()}')