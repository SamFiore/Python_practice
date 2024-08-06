from PySide6.QtGui import QAction
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QMainWindow,QApplication,QPushButton
import sys

class VentanaPySide(QMainWindow):
    def __init__(self):
        # LLamamos al método __init__ de la clase padre
        super().__init__()
        self.setWindowTitle('POO con PySide')
        # Configuración dínamica de la ventana
        # self.resize(600,400)
        # Configuración fija de la ventana
        self.setFixedSize(QSize(600,400))

        self._agregar_componentes()

    def _agregar_componentes(self):
        # Agregamos un menu
        menu = self.menuBar()
        menu_archivo = menu.addMenu('Archivo')
        # Agregamos algunas opciones
        accion_nuevo = QAction('Nuevo',self)
        menu_archivo.addAction(accion_nuevo)
        # Agregamos un texto a la barra de estado
        accion_nuevo.setStatusTip('Nuevo archivo')
        # Agregamos un mensaje en la barra de estado
        self.statusBar().showMessage('Información de la barra de estado')
        # Agregamos un botón
        boton = QPushButton('Nuevo botón')
        # Publicamos el botón en la ventana
        self.setCentralWidget(boton)

if __name__ == '__main__':
    app = QApplication([])
    # Creamos un objeto de tipo ventana
    ventana1 = VentanaPySide()
    ventana1.show()
    # Ejecutamos la ventana 
    sys.exit(app.exec())