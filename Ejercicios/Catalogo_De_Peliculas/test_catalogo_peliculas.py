from servicio.catalogo_peliculas import CatalogoPeliculas as cp
from dominio.pelicula import Pelicula
import os

menu = None
while menu != 4:
    try:
        print('''
        Opciones: 
              1_ Agregar pelicula
              2_ Listar peliculas
              3_ Eliminar catalogos
              4_ Salir
''')
        menu = int(input('Elegir opción: '))
        if menu == 1:
            nombre_pelicula = str(input('Escriba el nombre: '))
            pelicula = Pelicula(nombre_pelicula)
            cp.agregarPelicula(pelicula)
        elif menu == 2:
            cp.listarPeliculas()
        elif menu == 3:
            cp.eliminarCatalogo()
    except Exception as e:
        print(e)
        menu = None
else:
    print('Saliendo del programa...')