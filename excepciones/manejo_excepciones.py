from personalizacion_errores import NumerosIdenticosException

resultado = None
try:
    a = int(input('Colocar 1er número: '))
    b = int(input('Colocar 2do número: '))
    if a == b:
        raise NumerosIdenticosException('Números identicos') #"rasie" nos permite arrojar o lanzar excepciones
    resultado = a/b
except ZeroDivisionError as zde:
    print(f'ZeroDivisionError - Ocurrio un error: {zde}, {type(zde)}')
except TypeError as te:
    print(f'TypeError - Ocurrio un error: {te}, {type(te)}')
except Exception as e:
    print(f'Exception - Ocurrio un error: {e}, {type(e)}')
else: # Se ejecuta solo si no se arroja ninguna excepción
    print('No se arrojo ninguna excepcion')
finally: # Siempre se ejecuta al final
    print('Ejecucion del bloque finally')

print(resultado)
print('continuamos..')

