import psycopg2 as db
from logger_base import log
import sys

class Conexion:
    _DATABASE = 'put_database'
    _USERNAME = 'put_username'
    _PASSWORD = 'put_password'
    _DB_PORT = 7777
    _HOST = 'put_host'
    _conn = None
    _curs = None

    @classmethod
    def obtenerConexion(cls):
        if cls._conn is None:
            try:
                cls._conn = db.connect(dbname=cls._DATABASE,user=cls._USERNAME,password=cls._PASSWORD,host=cls._HOST,port=cls._DB_PORT)
                log.debug(f'Conexion exitosa: {cls._conn}')
                return cls._conn
            except Exception as e:
                log.debug(f'Ocurrió una excepción al obtener una conexión: {e}')
                sys.exit()
        else:
            return cls._conn
    @classmethod
    def obtenerCursor(cls):
        if cls._curs is None:
            try:
                cls._curs = cls.obtenerConexion().cursor()
                log.debug(f'Se abrió correctamente el cursor: {cls._curs}')
                return cls._curs
            except Exception as e:
                log.error(f'Ocurrió una excepción al obtener el cursor: {e}')
                sys.exit()

if __name__ == '__main__':
    Conexion().obtenerConexion()
    Conexion().obtenerCursor()