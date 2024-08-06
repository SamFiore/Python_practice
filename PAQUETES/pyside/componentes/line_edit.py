from PySide6.QtWidgets import QMainWindow,QApplication,QLineEdit
import sys

class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        # Componente QLineEdit
        linea_texto = QLineEdit()
        # Establecemos el máximo de cáracteres a captura
        linea_texto.setMaxLength(15)
        # Establecemos un texto de ayuda
        linea_texto.setPlaceholderText('Introduce tu nombre: ')
        # Modo solo lectura
        # linea_texto.setReadOnly(True)
        # Validación aplicando Mask (El 0 es para solo números)
        linea_texto.setInputMask('000-000-0000')
        # Evento enter, cambio seleccion de texto, cambio de texto
        # Evento enter
        linea_texto.returnPressed.connect(self.enter_presionado)
        # Evento cambio de seleccion
        linea_texto.selectionChanged.connect(self.cambio_seleccion)
        # Evento cambio de texto
        linea_texto.textChanged.connect(self.cambio_texto)
        # Publicamos el componentes
        self.setCentralWidget(linea_texto)

    def enter_presionado(self):
        print('Se presionó el enter')
        self.centralWidget().setText('000-000-0000')

    def cambio_seleccion(self):
        print('Cambio seleccion de texto')
        print(self.centralWidget().selectedText())

    def cambio_texto(self,nuevo_texto):
        print(f'Nuevo texto: {nuevo_texto}')



if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    sys.exit(app.exec())