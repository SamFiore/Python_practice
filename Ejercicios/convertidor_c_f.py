class ConvertidorTemperatura:
    MAX_CELSIUS = 100
    MAX_FAHRENHEIT = 213

    @classmethod
    def c_f(cls, celcius):
        if celcius > cls.MAX_CELSIUS:
            raise ValueError(f'Temperatura en grados celsius, demasiado alta: {cls.MAX_CELSIUS}°C temperatura máxima')
        return celcius * 9/5 + 32
    
    @classmethod
    def f_c(cls,fahrenheit):
        if fahrenheit > cls.MAX_FAHRENHEIT:
            raise ValueError(f'Temperatura en grados fahrenheit, demasiado alta: {cls.MAX_FAHRENHEIT}°F temperatura máxima')
        return (fahrenheit - 32) * 5/9
    
if __name__ == '__main__':
    resultado = ConvertidorTemperatura.c_f(15)
    # resultado = ConvertidorTemperatura.c_f(150) ValueError
    print(f'15°C son {int(resultado)}°F')
    resultado = ConvertidorTemperatura.f_c(10)
    print(f'10°F son {int(resultado)}°C')
