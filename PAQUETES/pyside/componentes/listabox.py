from PySide6.QtWidgets import QMainWindow,QApplication,QListWidget
import sys

class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        # Componente QListWidget
        lista = QListWidget()
        lista.addItem('Uno')
        lista.addItems(['Dos','Tres'])
        # Monitoreamos el cambio del elemento seleccionado, recibimos el elemento y el texto
        lista.currentItemChanged.connect(self.cambio_elemento)
        lista.currentTextChanged.connect(self.cambio_texto)
        # Publicamos el componentes
        self.setCentralWidget(lista)

    def cambio_elemento(self,nuevo_elemento):
        print(f'Nuevo elemento seleccionado: {nuevo_elemento.text()}')
    def cambio_texto(self,nuevo_texto):
        print(f'Nuevo elemento seleccionado: {nuevo_texto}')



if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    sys.exit(app.exec())