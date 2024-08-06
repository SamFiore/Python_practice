# Son funciones anónimas, y son pequeñas (De una sola línea)

# No es posible asignar una función a una variable
# mi_funcion = def sumar(): return a+b

# Con una función lambda ( Anónima, sin nombre, y una sola línea de código)
# No se necesita agregar paréntesis para los parámetros
# No se necesita usar la palabra return, pero si debe regresar una expresión
mi_funcion_lambda = lambda a,b: a+b
print(f'Resultado: {mi_funcion_lambda(42,22)}')

# Función lambda que no recibe argumentos, pero si una expresión válida
mi_funcion_lambda = lambda: 'Función sin argumentos'
print(f'Llamar función lambda sin argumentos: {mi_funcion_lambda()}')

# Función lambda con parámetros por default
mi_funcion_lambda = lambda a=2,b=3: a+b
print(f'Resultado con valores por default: {mi_funcion_lambda()}')

# Función lambda con argumentos variables con *args y *kwargs
mi_funcion_lambda = lambda *args, **kwargs: len(args) + len(kwargs)
print(f'Resultado argumentos variables: {mi_funcion_lambda(1,2,3, a=4,b=5,c=6)}')

# Funciones lambda con argumentos, argumentos variables y valores por default
mi_funcion_lambda = lambda a,b,c=3,*args,**kwargs: a+b+c+len(args)+len(kwargs)
print(f'Resultado de la función lambda: {mi_funcion_lambda(1,2,4, 5,6,7,e=5,f=7)}')