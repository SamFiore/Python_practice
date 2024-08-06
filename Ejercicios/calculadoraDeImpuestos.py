def calculadoraDeImpuestos(monto,impuesto):
    return monto + monto * (impuesto/100)

montoSImpuesto = int(input('Poner valor s/impuesto ($): '))
impuesto = int(input('Poner el impuesto (s/%): '))
total = calculadoraDeImpuestos(montoSImpuesto,impuesto)
print(f'El total a pagar con impuestos es: %.2f' % total)

