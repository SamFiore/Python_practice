from logger_base import log

class Usuario:
    def __init__(self,id_usuario = None,user = None,password = None):
        self._id_usuario = id_usuario
        self._user = user
        self._password = password

    def __str__(self):
        return f'''
        id = {self._id_usuario}
            user= {self._user}
            psw= {self._password}
'''
    
    @property
    def id_usuario(self):
        return self._id_usuario
    
    @property
    def user(self):
        return self._user
    
    @property
    def password(self):
        return self._password
    
    @id_usuario.setter
    def id_usuario(self,id_usuario):
        self._id_usuario = id_usuario

    @user.setter
    def user(self,user):
        self._user = user

    @password.setter
    def password(self,password):
        self.password = password

if __name__ == '__main__':
    usuario1 = Usuario(user='XxEmaxX',password='superema123')
    log.debug(usuario1)
    