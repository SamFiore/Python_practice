class Persona:
    contador_personas = 0

    @classmethod
    def generar_valor_siguiente(cls):
        cls.contador_personas += 1
        return cls.contador_personas

    def __init__(self, nombre, edad):
        self.id_persona = Persona.generar_valor_siguiente()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona: [{self.id_persona} , {self.nombre} , {int(self.edad)}]'
    
persona1 = Persona('Alberto',32)
print(persona1)
persona2 = Persona('Anastasia',19)
print(persona2)
persona3 = Persona('Mauricio',45)
print(persona3)

print(f'Cant. de personas: {Persona.contador_personas}')