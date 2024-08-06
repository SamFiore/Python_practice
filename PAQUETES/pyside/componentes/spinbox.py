from PySide6.QtWidgets import QMainWindow,QApplication,QSpinBox
import sys

class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        # QSpinBox (Solo maneja valores enteros)
        numero = QSpinBox()
        # Establecer el valor mínimo y el máximo por separado
        # numero.setMinimum(-5)
        # numero.setMaximum(8)
        # Lo mismo pero en una sola línea
        numero.setRange(-5,8)

        # Establecemos un prefijo y sufijo
        numero.setPrefix('$')
        numero.setSuffix('c')

        # Establecemos el salto (step)
        numero.setSingleStep(3)

        # Nos conectamos al evento o señal de cambio de valor
        # Envia el valor nuevo en número
        numero.valueChanged.connect(self.cambio_valor)
        # Envía el valor nuevo en texto incluyendo prefijo y sufijo
        numero.textChanged.connect(self.cambio_texto)

        # Publicamos el componentes
        self.setCentralWidget(numero)



if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    sys.exit(app.exec())