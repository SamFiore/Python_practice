from cursor_del_pool import CursorPool
from logger_base import log
from usuario import Usuario

class UsuarioDAO:
    _SELECCIONAR = 'SELECT * FROM usuarios ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuarios(username,password) VALUES(%s,%s)'
    _ACTUALIZAR = 'UPDATE usuarios SET username=%s,password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuarios WHERE id_usuario=%s'

    @classmethod
    def seleccionar(cls):
        with CursorPool() as curs:
            curs.execute(cls._SELECCIONAR)
            registros = curs.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0],registro[1],registro[2])
                usuarios.append(usuario)
            return usuarios
        
    @classmethod
    def insertar(cls,usuario):
        with CursorPool() as curs:
            valores = (usuario.user,usuario.password)
            curs.execute(cls._INSERTAR,valores)
            log.debug(f'Usuario insertado: {usuario}')
            return curs.rowcount
        
    @classmethod
    def actualizar(cls,usuario):
        with CursorPool() as curs:
            valores = (usuario.user,usuario.password,usuario.id_usuario)
            curs.execute(cls._ACTUALIZAR,valores)
            log.debug(f'Usuario actualizado: {usuario}')
            return curs.rowcount
        
    @classmethod
    def eliminar(cls,usuario):
        with CursorPool() as curs:
            valores = (usuario.id_usuario,)
            curs.execute(cls._ELIMINAR,valores)
            log.debug(f'Usuario eliminado: {usuario}')
            return curs.rowcount
        
if __name__ == '__main__':
    # usuario1 = Usuario(user='BornThisWay',password='juanito123')
    # UsuarioDAO.insertar(usuario1)
    # usuario1 = Usuario(1,'SenseiFacha','tobito')
    # UsuarioDAO.actualizar(usuario1)
    usuario1 = Usuario(2)
    UsuarioDAO.eliminar(usuario1)
    usuarios = UsuarioDAO.seleccionar()
    for usuario in usuarios:
        log.debug(usuario)
