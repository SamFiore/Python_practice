from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow,QApplication, QCheckBox
import sys

class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        # Creamos un nuevo componente de checkbox
        checkbox = QCheckBox('Este es un checkbox')
        # Activamos el 3er estado
        checkbox.setTristate(True)
        # Conectar la señal de cambio de componente
        checkbox.stateChanged.connect(self.mostrar_estado)
        # Publicamos el componente
        self.setCentralWidget(checkbox)

    def mostrar_estado(self, estado):
        print(f'Estado del checkbox: {estado}')
        # Trabajamos con las contantes
        if estado == Qt.Checked.value: print('Checkbox encendido')
        elif estado == Qt.PartiallyChecked.value: print('Checkbox sin estado o parcialmente checado')
        elif estado == Qt.Unchecked.value: print('Checkbox apagado')
        else: print('Con estado invalido')

if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    sys.exit(app.exec())