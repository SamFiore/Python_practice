# Simulación de sobrecarga de constructores en python
# Otras formas de crear objetos
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    @classmethod
    def crear_persona_vacia(cls):
        return cls(None,None) #Indirectamente llama al método __init__()
    
    @classmethod
    def crear_persona_valores(cls, nombre, apellido):
        return cls(nombre,apellido)
    
    def __str__(self):
        return f'Nombre: {self.nombre} | Apellido: {self.apellido}'

# Primer forma de crear objetos
persona1 = Persona('Arturo','Vidal')
persona_vacia = Persona.crear_persona_vacia()
print(persona_vacia)
print(persona1)
persona_valor = Persona.crear_persona_valores('Manuel','Arzobispo')
print(persona_valor)

