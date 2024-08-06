class MiClase:
    variable_clase = 'Valor de variable en clase'

    def __init__(self,variable_instancia):
        self.variable_instancia = variable_instancia

    @staticmethod
    # Estos métodos estáticos no pueden acceder a la variables de instancia, no tiene info relacionada directamente con la clase
    # Ya que no recibe ningún tipo de info directamente de la clase, se tiene que llamar directamente a la clase
    def metodo_estatico():
        print(MiClase.variable_clase)
    
    @classmethod
    # A diferencia del método estático, este si recibe un contexto, 'cls' significa class
    # Si recibe info de la clase en sí misma, podemos acceder a las var de clase o métodos de clase
    def metodo_clase(cls):
        print(cls.variable_clase)

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_clase)
        print(self.variable_instancia)

MiClase.metodo_estatico()
MiClase.metodo_clase()

miObjeto1 = MiClase('Valor variable de instancia')
miObjeto1.metodo_estatico()
miObjeto1.metodo_clase()
miObjeto1.metodo_instancia()