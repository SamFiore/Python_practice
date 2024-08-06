import math
from decimal import Decimal

# NaN = Not a Number (No es un número)
# NaN no es sensible a mayúsculas/minúsculas
# NaN es un tipo de dato númerico para representar un valor indefinido
a = float('NaN')
# print(f'a: {a}')
# print(f'¿Es NaN? : {math.isnan(a)}')

a = Decimal('NaN')
print(f'a: {a}')
print(f'¿Es NaN? : {math.isnan(a)}')