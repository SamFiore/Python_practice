from logger_base import log
from conexion import Conexion

class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug('Inicio del método with __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor
    
    def __exit__(self,tipo_except,value_except,detalle_except):
        log.debug('Se ejecuta método __exit__')
        if value_except: 
            self._conexion.rollback()
            log.error(f'Ocurrió una excepción, se hace rollback: {value_except}, {tipo_except}, {detalle_except}')
        else:
            self._conexion.commit()
            log.debug('Commit de la transacción')
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)

if __name__ == '__main__':
    with CursorDelPool() as curs:
        log.debug('Dentro del bloque with')
        curs.execute('SELECT * FROM persona')
        log.debug(curs.fetchall())