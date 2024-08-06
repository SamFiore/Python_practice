# Signals y slots
from PySide6.QtWidgets import QMainWindow,QPushButton, QApplication
import sys

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Signals y Slots')
        # Botón
        boton = QPushButton('Click aquí')
        # Conectamos el evento check (por default es False)
        boton.setCheckable(True)
        # Conectamos otro slot al evento check
        boton.clicked.connect(self._evento_check)
        # Conectamos el evento (signal) click con el slot (evento_click)
        boton.clicked.connect(self._evento_click)
        # Publicamos el botón
        self.setCentralWidget(boton)

    def _evento_check(self,check):
        self.boton_check = check
        print(f'Check? {self.boton_check}')


    def _evento_click(self):
        print('Has hecho click')
        # Accedemos al estado del botón (check)
        print(f'Botón checkado desde evento click? {self.boton_check}')


if __name__ == '__main__':
    # Creamos el objeto de app
    app = QApplication([])
    # Creamos una instancia de nuestra clase
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
