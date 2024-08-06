class Producto:
    contador_productos = 0

    @classmethod
    def siguiente_producto(cls):
        cls.contador_productos += 1
        return cls.contador_productos

    def __init__(self, nombre, precio):
        self._id_producto = Producto.siguiente_producto()
        self._nombre = nombre
        self._precio = precio

    @property
    def id_producto(self):
        return self._id_producto
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def precio(self):
        return self._precio
    
    @id_producto.setter
    def id_producto(self,id_producto):
        self._id_producto = id_producto

    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre

    @precio.setter
    def precio(self,precio):
        self._precio = precio

    def __str__(self):
        return f'Producto:[ id:{self._id_producto} , nombre:{self._nombre} , precio:{self._precio:.2f} ]'
    

if __name__ == '__main__':
    producto1 = Producto('Aceite',1299.999)
    print(producto1)
    print(producto1.id_producto)
    print(producto1.nombre)
    print(producto1.precio)
    producto2 = Producto('Azucar',699.999)
    print(producto2)
    print(producto2.id_producto)
    print(producto2.nombre)
    print(producto2.precio)
