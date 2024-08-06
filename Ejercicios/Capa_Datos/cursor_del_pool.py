from logger_base import log
from conexion import Conexion

class CursorPool():
    def __init__(self):
        self._conn = None
        self._curs = None

    def __enter__(self):
        self._conn = Conexion.obtenerConexion()
        self._curs = self._conn.cursor()
        return self._curs
    
    def __exit__(self,value,tipe,details):
        if value:
            self._conn.rollback()
            log.error(f'Ocurrió un error, se hizo rollback: {value}, {tipe}, {details}')
        else:
            self._conn.commit()
        self._curs.close()
        Conexion.liberarConexion(self._conn)

if __name__ == '__main__':
    with CursorPool() as curs:
        curs.execute('SELECT * FROM usuarios')
        log.debug(curs.fetchall())
        