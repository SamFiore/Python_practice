from usuarioDAO import UsuarioDAO
from usuario import Usuario
from logger_base import log

def menu_usuario_app():
    switch = True
    opciones = '''
        Menú
          opciones:
            1) Listar usuarios
            2) Agregar usuario
            3) Actualizar usuario
            4) Eliminar usuario
            5) Salir
'''
    while switch:
        log.debug(opciones)
        opcion = int(input('Elija su opción: '))
        if opcion == 1: 
            usuarios = UsuarioDAO.seleccionar()
            for usuario in usuarios:
                log.debug(usuario)
        elif opcion == 2:
            user = str(input('Ingrese el usuario: '))
            password = str(input('Ingrese la contraseña: '))
            usuario = Usuario(user=user,password=password)
            UsuarioDAO.insertar(usuario)
        elif opcion == 3:
            id_usuario = int(input('Ingrese el id del usuario a actualizar: '))
            user = str(input('Ingrese en nuevo usuario: '))
            password = str(input('Ingresar la nueva contraseña: '))
            usuario = Usuario(id_usuario,user,password)           
            UsuarioDAO.actualizar(usuario)
        elif opcion == 4:
            id_usuario = int(input('Ingrese la id del usuario a eliminar: '))
            usuario = Usuario(id_usuario)
            UsuarioDAO.eliminar(usuario)
        elif opcion == 5:
            switch = False 

menu_usuario_app()     

