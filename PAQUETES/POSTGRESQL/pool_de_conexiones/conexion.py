from psycopg2 import pool
from logger_base import log
import sys

class Conexion:
    _DATABASE = 'put_database'
    _USERNAME = 'put_username'
    _PASSWORD = 'put_password'
    _DB_PORT = 7777
    _HOST = 'put_localhost'
    _MIN_CONN = 1
    _MAX_CONN = 5
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool == None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CONN,cls._MAX_CONN,dbname=cls._DATABASE,user=cls._USERNAME,password=cls._PASSWORD,port=cls._DB_PORT,host=cls._HOST)
                log.debug(f'Creación del pool exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrió un error al obtener el pool: {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conn = cls.obtenerPool().getconn()
        log.debug(f'Conexión obtenida del pool: {conn}')
        return conn
    
    @classmethod
    def liberarConexion(cls,conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Regresamos el objeto al pool: {conexion} ')

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()



if __name__ == '__main__':
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)
    conexion2 = Conexion.obtenerConexion()
    conexion3 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion3)
    conexion4 = Conexion.obtenerConexion()
    conexion5 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion5)
    conexion6 = Conexion.obtenerConexion()