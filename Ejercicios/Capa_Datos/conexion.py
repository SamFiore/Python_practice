from logger_base import log
from psycopg2 import pool
import sys

class Conexion:
    _DATABASE = 'put_db'
    _USERNAME = 'put_user'
    _PASSWORD = 'put_psw'
    _DB_PORT = 7777
    _HOST = 'put_host'
    _MIN_CONN = 1
    _MAX_CONN = 5
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool == None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CONN,cls._MAX_CONN,dbname=cls._DATABASE,user=cls._USERNAME,password=cls._PASSWORD,host=cls._HOST,port=cls._DB_PORT)
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrió un error al obtener el pool: {e}')
                sys.exit()
        else:
            return cls._pool
    
    @classmethod
    def obtenerConexion(cls):
        conn = cls.obtenerPool().getconn()
        return conn
    
    @classmethod
    def liberarConexion(cls,conexion):
        cls.obtenerPool().putconn(conexion)

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()
        log.debug('Se cerraron todas las conexiones')

if __name__ == '__main__':
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)
    conexion2 = Conexion.obtenerConexion()
    conexion3 = Conexion.obtenerConexion()
    conexion4 = Conexion.obtenerConexion()
    conexion5 = Conexion.obtenerConexion()
    conexion6 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion2)
    conexion7 = Conexion.obtenerConexion()
    Conexion.cerrarConexiones()

