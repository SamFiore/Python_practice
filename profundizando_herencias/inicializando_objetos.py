# Orden de inicialización de objetos
class Padre: 
    def __init__(self):
        print('Inicializador padre')

    def metodo(self):
        print('Método padre')

class Hijo(Padre):
    def __init__(self):
        # De manera opcional podemos llamar al método __init__ de la clase padre
        print('Inicializador hijo')
        super().__init__()
    
    # Sobreescribimos el método llamada de la clase padre
    def metodo(self):
        print('Método hijo')
        super().metodo()

# padre1 = Padre()
# padre1.metodo()
# hijo1 = Hijo() La clase hija hereda el inicializar de la clase padre, solo si no tiene inicializador
hijo1 = Hijo()  #Esto se agregó después (Llama directamente el inicializador hijo en vez de padre)
hijo1.metodo()