from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow,QLabel,QApplication
from PySide6.QtGui import QPixmap
import sys

class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        self.setFixedSize(500,600)
        # Creamos un componentes de tipo etiqueta (label)
        etiqueta = QLabel('Hola')
        etiqueta.setPixmap(QPixmap('layla.jpg'))
        etiqueta.setScaledContents(True)

        # Publicamos este componente
        self.setCentralWidget(etiqueta)

if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    sys.exit(app.exec())