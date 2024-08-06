class ManejoArchivos:
    def __init__(self,nombre):
        self.nombre = nombre

    def __enter__(self):
        print('Obtenemos el recurso'.center(50,'-'))
        self.nombre = open(self.nombre,'r',encoding='utf8')
        return self.nombre
    
    def __exit__(self, tipo_excepcion, valor_excepcion, traza_error): # 'Traceback'(traza): Toda la lista de errores si es que ocurrio alguno
        # La firma del método son los parámetros que tenemos que agregar, de lo contrario marca error
        print('Cerramos el recurso'.center(50,'-'))
        if self.nombre:
            self.nombre.close()