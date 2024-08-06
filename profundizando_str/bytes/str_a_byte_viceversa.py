# Convertir strings a bytes

string = 'Programación con python'
print(f'String original: {string}')
bytes1 = string.encode('UTF-8')
print(f'Bytes codificados: {bytes1}')

# Convertir bytes a strings

string2 = bytes1.decode('UTF-8')
print(f'String decodificado: {string2}')
print(string == string2)
