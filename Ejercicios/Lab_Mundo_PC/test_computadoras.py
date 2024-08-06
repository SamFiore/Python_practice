from ordenComputadoras import OrdenComputadoras
from computadora2 import Computadora
from perifericos import *
from monitor import Monitor

monitor1 = Monitor('Samsung',32)
monitor2 = Monitor('Philips',43)
monitor3 = Monitor('Philco',21)

teclado1 = Teclado('Redragon','USB')
teclado2 = Teclado('Logitech','Bluetooth')
teclado3 = Teclado('Genius','USB')

raton1 = Raton('Logitech', 'USB')
raton2 = Raton('Redragon','Bluetooth')
raton3 = Raton('Genius','Bluetooth')

computadora1 = Computadora('HP',monitor1,teclado1,raton1)
computadora2 = Computadora('Asus',monitor2,teclado2,raton2)
computadora3 = Computadora('Gamer',monitor3,teclado3,raton3)

orden_computadoras1 = OrdenComputadoras([computadora1,computadora2])
orden_computadoras2 = OrdenComputadoras([computadora3,computadora1])
print(orden_computadoras1)
print(orden_computadoras2)
