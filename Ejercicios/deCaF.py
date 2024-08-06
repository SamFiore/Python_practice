def deCAF(c=0,f=0):
    if c>0:
        return (c * 9/5) + 32
    elif f>0:
        return (f - 32) * 5/9
    elif c>0 and f>0:
        return ('Ingresaste los dos, solo soportamos uno')
    
celcius = int(input('Marcar grados celcius: ') or '0')
fahrenheit = int(input('Marcar grados fahrenheit: ') or '0')

if celcius > 0 and fahrenheit > 0:
    print('Debes ingresar solo uno')
elif celcius > 0:
    total = deCAF(c=celcius)
    print(f'Tus grados fahrenheit son: %.2f °F ' %total)
elif fahrenheit > 0:
    total = deCAF(f=fahrenheit)
    print(f'Tus grados celcius son: %.2f °C ' %total)