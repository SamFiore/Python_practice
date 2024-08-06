import os

class CatalogoPeliculas:
    ruta = 'path_file'

    @classmethod
    def agregarPelicula(cls, pelicula):
        with open(cls.ruta, 'a', encoding='utf8') as archivo:
            archivo.write(f'{pelicula.nombre}\n')

    @classmethod
    def listarPeliculas(cls):
        with open(cls.ruta,'r',encoding='utf8') as archivo:
            print(archivo.read())
    
    @classmethod
    def eliminarCatalogo(cls):
        os.remove(cls.ruta)
