from metodoDestructor import Persona as Ps

print('Creador de objetos'.center(30,'-'))
persona1 = Ps('Ignacio','Caroto',30)
persona1.showDetails()

print('Eliminador de objetos'.center(30,'-'))
del persona1


