# Ejemplo atributos públicos, protegidos, privados

class Miclase:
    def __init__(self, publico, protegido, privado):
        self.publico = publico
        self._protegido = protegido
        self.__privado = privado


miclase1 = Miclase('Valor público','Valor protegido','Valor privado')
# Acceso valor público
print(miclase1.publico)
# Modificar valor público
miclase1.publico = 'Nuevo valor público'
print(miclase1.publico)

# Acceso al valor protegido
# Solo dentro de la misma clase o clases hijas
# print(miclase1._protegido)
# Modificar atributos protegidos
# miclase1._protegido = 'Nuevo valor protegido'
# Se puede acceder al valor y modificarlo, pero no es buena práctica, para eso utilizar los métodos get/set

# Acceso al valor privado
# print(miclase1.__privado) Lanza un error
# No se puede acceder directamente, pero python convierte el objeto de la siguiente forma 
# objeto._clase__atributo_privado
# print(miclase1._Miclase__privado) Pero no es recomendable acceder
# Modifica atributos privados
# miclase1.__privado = 'Nuevo valor privado' 
# miclase1._Miclase__privado = 'Nuevo valor privado'
