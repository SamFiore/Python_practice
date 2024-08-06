from disenoDeClase import Producto

class Orden:
    contador_ordenes = 0

    @classmethod
    def siguiente_orden(cls):
        cls.contador_ordenes += 1
        return cls.contador_ordenes

    def __init__(self,productos):
        self._ordenes_id = Orden.siguiente_orden()
        self._productos = list(productos)

    @property
    def ordenes_id(self):
        return self._ordenes_id

    def agregar_producto(self,producto):
        self._productos.append(producto)
    
    def calcular_total(self):
        total = 0
        for producto in self._productos:
            total += producto.precio
        return total
    
    def __str__(self):
        productos_str = ''
        for producto in self._productos:
            productos_str += producto.__str__() + '|'

        return f'Orden: {self._ordenes_id} |\n Productos: {productos_str}'
    
if __name__ == '__main__':
    producto1 = Producto('Aceite',1299.999)
    producto2 = Producto('Azucar',699.999)
    orden1 = Orden([producto1,producto2])
    orden2 = Orden([producto2,producto1])
    print(orden1)
    print(orden2)

        