from PySide6.QtWidgets import QWidget,QMainWindow,QApplication
from PySide6.QtGui import QColor,QPalette

class Color(QWidget):
    def __init__(self,nuevo_color):
        super().__init__()
        # Indicamos que se puede agregar un color de fondo
        self.setAutoFillBackground(True)
        paleta_colores = self.palette()
        # Creamos el componentes de color de fondo aplicando el nuevo color
        paleta_colores.setColor(QPalette.Window,QColor(nuevo_color))
        # Aplicamos el nuevo color al componente 
        self.setPalette(paleta_colores)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Layaouts en PySide')
        componentes_con_color_fondo = Color('blue')
        # El componentes se expande para cubrir el tamaño disponible
        self.setCentralWidget(componentes_con_color_fondo)


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()