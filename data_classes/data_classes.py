from dataclasses import dataclass
from typing import ClassVar

@dataclass(eq=True,frozen=True)
class Domicilio:
    calle: str
    numero: int = 0


@dataclass(frozen=True)
class Persona:
    nombre: str
    apellido: str
    domicilio: Domicilio
    contador_personas: ClassVar[int] = 0

    def __post_init__(self):
        if not self.nombre:
            raise ValueError(f'Valor de nombre vacío: {self.nombre}')

domicilio1 = Domicilio('Saturno',15)
persona1 = Persona('Sam','Fiore',domicilio1)
print(f'{persona1!r}')
# Variable de clase
print(f'Variable de clase: {Persona.contador_personas}')
# Variables de instancia
print(f'Variables de instancia: {persona1.__dict__}')
# Variables con valores vacíos
# persona_vacia = Persona('','')
# print(persona_vacia)
# Recibir igualdad entre objetos (__eq__)
persona2 = Persona('Juan Carlos','Bodoque',Domicilio('Jupiter',30))
print(f'Son iguales?: {persona1 == persona2}')
# Agregar clase a una colección
coleccion = {persona1,persona2}
print(f'Coleccón: {coleccion}')