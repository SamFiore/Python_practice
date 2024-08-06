from PySide6.QtWidgets import QMainWindow,QLabel,QApplication,QLineEdit,QVBoxLayout,QWidget
import sys

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Signals y Slots')
        self.setFixedSize(400,200)
        # Definimos la etiqueta y la línea de edición
        self.etiqueta = QLabel()
        self.entrada_texto = QLineEdit()
        # Conectar el widget de entrada de texto con la etiqueta 
        # La señal es textChanged y el slot es setText
        self.entrada_texto.textChanged.connect(self.etiqueta.setText)
        # Publicamos los componentes utilizando un layout
        disposicion = QVBoxLayout()
        disposicion.addWidget(self.entrada_texto)
        disposicion.addWidget(self.etiqueta)
        # Crear un contenedor 
        contenedor = QWidget()
        contenedor.setLayout(disposicion)
        # Publicamos el contenedor
        self.setCentralWidget(contenedor)

if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
