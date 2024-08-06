from clase_conexion import Conexion as conn
from persona import Persona
from logger_base import log
# DAO = Data Acces Object, es un patrón de Diseño para comunicarse con una Base de Datos, tiene las operaciones CRUD(Create,Read,Update y Delete) de una Clase de Entidad (Persona)
class PersonaDAO:
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre,apellido,email) VALUES(%s,%s,%s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s,apellido=%s,email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def seleccionar(cls):
        with conn.obtenerConexion() as conexion:
            with conexion.cursor() as curs:
                curs.execute(cls._SELECCIONAR)
                registros = curs.fetchall()
                personas = []
                for registro in registros:
                    persona = Persona(registro[0],registro[1],registro[2],registro[3])
                    personas.append(persona)
                return personas

    @classmethod
    def insertar(cls,persona):
        with conn.obtenerConexion():
            with conn.obtenerCursor() as curs:
                valores = (persona.nombre,persona.apellido,persona.email)
                curs.execute(cls._INSERTAR,valores)
                log.debug(f'Persona a insertada: {persona}')
                return curs.rowcount
        
    @classmethod
    def actualizar(cls,persona):
        with conn.obtenerConexion():
            with conn.obtenerCursor() as curs:
                valores = (persona.nombre,persona.apellido,persona.email,persona.id_persona)
                curs.execute(cls._ACTUALIZAR,valores)
                log.debug(f'Persona actualizada: {persona}')
                return curs.rowcount
    @classmethod
    def eliminar(cls,persona):
        with conn.obtenerConexion():
            with conn.obtenerCursor() as curs:
                valores = (persona.id_persona,)
                curs.execute(cls._ELIMINAR,valores)
                log.debug(f'Objetos eliminados: {persona}')
                return curs.rowcount

if __name__ == '__main__':
#   Insertar objetos
    # persona1 = Persona(nombre='Agustin',apellido='Anibal',email='aanibal@gmail.com')
    # personas_insertadas = PersonaDAO.insertar(persona1)
    # log.debug(f'Personas insertadas: {personas_insertadas}')

#   Actualizar un registro
    # persona1 = Persona(11,'Perry','Ornitorrinco','peornitorrinco@gmail.com')
    # personas_actualizadas = PersonaDAO.actualizar(persona1)
    # log.debug(f'Personas actualizadas: {personas_actualizadas}')

#   Eliminar un registro
    persona1 = Persona(9)
    personas_eliminadas = PersonaDAO.eliminar(persona1)
    log.debug(f'Personas eliminadas: {personas_eliminadas}')

#   Seleccionar objetos
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)