from PySide6.QtWidgets import QMainWindow,QApplication,QDoubleSpinBox
import sys

class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        # QDoubleSpinBox (Solo valores flotantes)
        numero = QDoubleSpinBox()

        numero.setRange(-5.2,8.1)
        numero.setPrefix('$')
        numero.setSuffix('c')
        numero.setSingleStep(0.5)
        # Nos conectamos al evento o señal de cambio de valor
        # Envia el valor nuevo en número
        numero.valueChanged.connect(self.cambio_valor)
        # Envía el valor nuevo en texto incluyendo prefijo y sufijo
        numero.textChanged.connect(self.cambio_texto)


        # Publicamos el componentes
        self.setCentralWidget(numero)

    def cambio_valor(self,nuevo_valor):
        print(f'Nuevo valor: {nuevo_valor}')

    def cambio_texto(self,nuevo_texto):
        print(f'Nuevo texto: {nuevo_texto}')

if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    sys.exit(app.exec())