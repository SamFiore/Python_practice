class MiClase:
    # Esta es una variable de clase, si se comparte con todos los objetos, se asocia con la clase en sí
    variable_clase = 'Valor de variable en clase'

    def __init__(self,variable_instancia):
        # Esta es una variable de instancia, no se comparte con distintos objetos, se asocia con los objetos en sí
        self.variable_instancia = variable_instancia


print(MiClase.variable_clase)
miClase = MiClase('Valor variable de instancia')
print(miClase.variable_instancia)
print(miClase.variable_clase)
miClase2 = MiClase('Valor variable 2 de instancia')
print(miClase2.variable_instancia)
print(miClase2.variable_clase)


