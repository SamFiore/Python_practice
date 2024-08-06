from PySide6.QtWidgets import QMainWindow,QApplication,QSlider
import sys

class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        # QSlider
        # Horizontal
        # componente = QSlider(Qt.Horizontal)
        # Vertical
        # componente = QSlider(Qt.Vertical)
        # Normal
        componente = QSlider()
        # componente.setMinimum(-5)
        # componente.setMaximum(8)
        componente.setRange(-5,8)

        # Conectamos a las señales
        componente.valueChanged.connect(self.cambio_valor)
        componente.sliderMoved.connect(self.slider_cambio_posicion)
        componente.sliderPressed.connect(self.slider_presionado)
        componente.sliderReleased.connect(self.slider_liberado)

        # Publicamos el componentes
        self.setCentralWidget(componente)

    def slider_presionado(self):
        print('Se presiono el slider')

    def slider_liberado(self):
        print('Se liberó el slider')

    def cambio_valor(self,valor):
        print(f'Nuevo valor {valor}')

    def slider_cambio_posicion(self,nueva_posicion):
        print(f'Nueva posicion {nueva_posicion}')

if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    sys.exit(app.exec())