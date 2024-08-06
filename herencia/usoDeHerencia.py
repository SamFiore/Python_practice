class Vehiculo:
    def __init__(self,vehiculo,color,ruedas):
        self.vehiculo = vehiculo
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f'{self.vehiculo} de color {self.color}, con {self.ruedas} ruedas'
    
class Coche(Vehiculo):
    def __init__(self,vehiculo,color,ruedas,velocidad):
        super().__init__(vehiculo,color,ruedas)
        self.velocidad = velocidad
    
    def __str__(self):
        return f'{super().__str__()}, con una velocidad de {self.velocidad}/h'
    
class Bicicleta(Vehiculo):
    def __init__(self, vehiculo, color, ruedas, tipo):
        super().__init__(vehiculo, color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f'Tipo {self.tipo} de {super().__str__()}'