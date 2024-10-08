# Signals y slots
from PySide6.QtWidgets import QMainWindow,QPushButton, QApplication
import sys

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Signals y Slots')
        self.boton = QPushButton('Click aquí')
        # Asociamos la señal de click al slot evento_click
        self.boton.clicked.connect(self.evento_click)
        self.setCentralWidget(self.boton)

    def evento_click(self):
        # Cambiar el texto del botón y el título de la ventana 
        self.boton.setText('Nuevo texto botón')
        self.boton.setEnabled(False)
        self.setWindowTitle('Nuevo título de la app')


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
