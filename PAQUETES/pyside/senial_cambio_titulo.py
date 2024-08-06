# Signals y slots
from PySide6.QtWidgets import QMainWindow,QPushButton, QApplication
import sys

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Signals y Slots')
        self.boton = QPushButton('Click aquí')
        self.boton.clicked.connect(self.evento_click)
        # Conectar a la señal de cambio de título
        self.windowTitleChanged.connect(self.cambio_titulo_app)
        self.setCentralWidget(self.boton)


    def evento_click(self):
        self.boton.setText('Nuevo texto botón')
        self.boton.setEnabled(False)
        self.setWindowTitle('Nuevo título de la app')

    def cambio_titulo_app(self, nuevo_titulo):
        print(f'Nuevo título: {nuevo_titulo}')

if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
