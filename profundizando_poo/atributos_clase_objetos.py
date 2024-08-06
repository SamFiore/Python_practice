class Persona:
    contador_personas = 0

    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

# Mostrar los atributos de un objeto
persona1 = Persona('Alberto','Gimenez',34)
print(persona1.__dict__)

# Crear un atributo al momento
print(persona1.contador_personas) #Accediendo al atributo de clase
# Pero no es posible modificarlo con el objeto, si no, con la clase
persona1.contador_personas = 10
print(persona1.contador_personas) #Atributo de objeto
print(Persona.contador_personas) #Atributo de clase
print(persona1.__dict__)
# Persona.contador_personas = 10

# Un segundo objeto
persona2 = Persona('Mariano','Perez',21)
print(persona2.__dict__)

# variable de clase creada al momento
Persona.contador_personas2 = 20
print(Persona.contador_personas2)