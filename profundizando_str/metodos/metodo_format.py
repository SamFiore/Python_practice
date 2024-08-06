# help(str.format)
nombre = 'Alfonso'
edad = 42   
sueldo = 300000
#                          placeholder: marcador de posición
mensaje = 'Nombre {} Edad {} Sueldo {:.2f}'.format(nombre,edad,sueldo)
# print(mensaje)

mensaje = 'Nombre {0} Edad {1} Sueldo {2:.2f}'.format(nombre,edad,sueldo)
# print(mensaje)

mensaje = 'Sueldo {2:.2f} Nombre {0} Edad {1}'.format(nombre,edad,sueldo)
# print(mensaje)

mensaje = 'Nombre {n} Edad {e} Sueldo {s:.2f}'.format(n=nombre,e=edad,s=sueldo)
# print(mensaje)

diccionario = {'nombre': 'Ignacio','edad':30,'sueldo':600000}
mensaje = 'Nombre {persona[nombre]} Edad {persona[edad]} Sueldo {persona[sueldo]:.2f}'.format(persona = diccionario)
print(mensaje)