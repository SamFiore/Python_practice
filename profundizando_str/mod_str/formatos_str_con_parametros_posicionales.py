# Dar formato a un string
nombre = 'Arturo'
edad = 32

mensaje_con_formato = 'Mi nombre es %s y tengo %d años'%(nombre,edad)
# print(mensaje_con_formato)

persona = ('Michael','Jackson',2000000.00)
# mensaje_con_formato = 'Hola %s %s, tu sueldo es de %.2f'%persona
# print(mensaje_con_formato)

mensaje_con_formato = 'Hola %s %s, tu sueldo es de %.2f'
print(mensaje_con_formato%persona)
