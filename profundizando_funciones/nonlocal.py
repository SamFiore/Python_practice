# Funciones anidadas y alcance de variables
# Palabra reservada nonlocal

def funcion_externa():
    variable_local_externa = 'Variable local externa'
    print(variable_local_externa)
    def funcion_anidada():
        variable_local_anidada = 'Variable local anidada'
        print(variable_local_anidada)
        # Cuando estamos trabajando en una funcion anidada y no queremos que se cree una nueva variable local, podemos trabajar con la variable externa que fue definida dentro de la función
        # Con nonlocal podemos trabajar con ella, accediendo al valor o modificarlo
        nonlocal variable_local_externa
        variable_local_externa = 'Nuevo valor variable local externa'
        print(variable_local_externa)
    funcion_anidada()

funcion_externa()
