class AreaRectangulo:
    def __init__(self,b,h):
        self.b = b
        self.h = h
    
    def area(self):
        return self.b * self.h
    
base = int(input('Introducir la base del rectangulo: '))
altura = int(input('Introducir la altura del rectangulo: '))

rectangulo = AreaRectangulo(base,altura)

print(rectangulo.area())