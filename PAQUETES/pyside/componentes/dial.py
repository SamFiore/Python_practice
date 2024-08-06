from PySide6.QtWidgets import QMainWindow,QApplication,QDial
import sys

class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        # Qdial es similar al Slider pero es una rueda, utilizada para las aplicaciones de audio
        componente = QDial()

        componente.setRange(-5,50)

        # Conectamos a las señales
        componente.valueChanged.connect(self.cambio_valor)
        componente.sliderMoved.connect(self.slider_cambio_posicion)
        componente.sliderPressed.connect(self.slider_presionado)
        componente.sliderReleased.connect(self.slider_liberado)

        # Publicamos el componentes
        self.setCentralWidget(componente)

    def slider_presionado(self):
        print('Se presiono el dial')

    def slider_liberado(self):
        print('Se liberó el dial')

    def cambio_valor(self,valor):
        print(f'Nuevo valor {valor}')

    def slider_cambio_posicion(self,nueva_posicion):
        print(f'Nueva posicion {nueva_posicion}')

if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    sys.exit(app.exec())