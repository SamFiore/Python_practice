# Es una colección de elemento únicos y mutable
# Los elementos deben ser inmutables
# conjunto = {[1,2],[3,4]} No se puede
conjunto = {'Juan',True,18.0,(1,2,3)}
# print(f'Set: {conjunto}')

# Set vacío
# conjunto = {} Así no, genera un dict
conjunto = set()
# print(conjunto)
# print(type(conjunto))

# Es mutable
conjunto.add('Juan')
# print(conjunto)

# contiene valores únicos
conjunto.add('Juan')
# print(conjunto)

# Crear un set a partir de un iterable
conjunto = set([4,5,7,8,4])
# print(conjunto)

conjunto2 = {100,200,300,300}
conjunto.update(conjunto2)
# print(conjunto)
conjunto.update([20,30,40,40])
print(conjunto)

# Copiar un set a otro set (Copia poco profundas, solo se copia las referencias)
conjunto_copia = conjunto.copy()
print(conjunto_copia)
print(conjunto_copia in conjunto) # No tiene las mismas referencias
print(conjunto_copia == conjunto) # Tiene el mismo de contenido
