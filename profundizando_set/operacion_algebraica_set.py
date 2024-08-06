# Operaciones de conjunto con set
# Persona con distintas características

pelo_negro = {'Juan','Carla','Pedro','María'}
pelo_rubio = {'Lorenzo','Laura','Marco'}
ojos_cafe = {'Carla','Laura'}
menores_30 = {'Juan','Carla','María'}

# Función de unión
# Todos los elementos de los dos conjuntos (Union) (No se repiten los elementos)
print(ojos_cafe.union(pelo_rubio))

# Función conmutativa
# Invertir el orden con el mismo resultado (conmutativa)
print(pelo_rubio.union(ojos_cafe))

# Función intersección
# Solo los elementos que se encuentren en ambos conjuntos (intersection) (conmutativa)
print(ojos_cafe.intersection(pelo_rubio))

# Función de diferencia
# Solo los elementos que se encuentran en un conjunto, pero si uno se encuentra en otro, no son tomados en cuenta (difference) (No conmutativa)
# Se imprime el Set A pero no el Set B
print(pelo_negro.difference(ojos_cafe))
print(ojos_cafe.difference(pelo_negro))

# Función de diferencia simetrica
# Va a regresar todos los elementos excepto los que se encuentran en común entre los conjuntos (symmetric difference) (conmutativa)
print(pelo_negro.symmetric_difference(ojos_cafe))
print(ojos_cafe.symmetric_difference(pelo_negro))
