from disenoDeClase import Producto
from disenoDeClase2 import Orden


producto1 = Producto('Aceite',1299.99)
producto2 = Producto('Azucar',699.99)
producto3 = Producto('Leche',980.00)
producto4 = Producto('Galletas',599.99)

orden1 = Orden([producto1,producto2])
orden1.agregar_producto(Producto('Cafe',2080.00))
orden2 = Orden([producto3,producto4])
print(orden1)
print(orden2)
print(f'Total de orden [{orden1.ordenes_id}] : ${orden1.calcular_total():.2f}')
print(f'Total de orden [{orden2.ordenes_id}] : ${orden2.calcular_total():.2f}')
