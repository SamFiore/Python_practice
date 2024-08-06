class Aritmetica: 
    """ 
    DocString: Documentación de la clase en python
    """
    def __init__(self,operandoA,operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB
    
    def restar(self):
        return self.operandoA - self.operandoB
    
    def multiplicar(self):
        return self.operandoA * self.operandoB
    
    def dividir(self):
        return self.operandoA / self.operandoB
    
    def potenciar(self):
        return self.operandoA ** self.operandoB
    
aritmetica1 = Aritmetica(20,300)
print(aritmetica1.sumar())
print(aritmetica1.restar())
print(aritmetica1.multiplicar())
print(f"{aritmetica1.dividir():.2f}")
print(aritmetica1.potenciar())