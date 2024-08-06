pelo_negro = {'Juan','Carla','Pedro','María'}
pelo_rubio = {'Lorenzo','Laura','Marco'}
ojos_cafe = {'Carla','Laura'}
menores_30 = {'Juan','María'}
mayores_50 = {'Laura','Carla'}

# Subset
# Si un conjunto es subconjunto del 1er conjunto
# Revisamos si los elementos del primer set están contenidos en el segundo set
print(menores_30.issubset(pelo_negro)) #True

# Superset
# Si el conjunto es superset
# Si un set contiene a otro set, revisamos si los elementos del primer set estan contenido el segundo set
# Con todos sus elementos
print(mayores_50.issuperset(ojos_cafe))

# Disjoint
# Si un conjunto no tiene relación con el otro
print(menores_30.isdisjoint(pelo_rubio))
