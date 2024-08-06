from dispositivoEntrada import dispositivoEntrada

class Raton(dispositivoEntrada):
    contador_ratones = 0

    @classmethod
    def sigNumero(cls):
        cls.contador_ratones += 1
        return cls.contador_ratones
    
    def __init__(self, marca, tipo_entrada):
        dispositivoEntrada.__init__(self,marca,tipo_entrada)
        self.__id_raton = Raton.sigNumero()

    @property
    def id_raton(self):
        return self.__id_raton

    def __str__(self):
        return f'ID:{self.__id_raton} {dispositivoEntrada.__str__(self)}'
    
class Teclado(dispositivoEntrada):
    contador_teclados = 0

    @classmethod
    def sigNum(cls):
        cls.contador_teclados += 1
        return cls.contador_teclados
    
    def __init__(self,marca,tipo_entrada):
        dispositivoEntrada.__init__(self,marca,tipo_entrada)
        self.__id_teclado = Teclado.sigNum()

    @property
    def id_teclado(self):
        return self.__id_teclado

    def __str__(self):
        return f'ID:{self.__id_teclado} {dispositivoEntrada.__str__(self)}'

if __name__ == '__main__':
    raton1 = Raton('Logitech','Bluetooth')
    raton2 = Raton('Genius','Bluetooth')
    print(raton1)
    print(raton2)
    teclado1 = Teclado('Logitech','Bluetooth')
    teclado2 = Teclado('Genius','Bluetooth')
    print(teclado1)
    print(teclado2)



