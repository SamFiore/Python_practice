from PySide6.QtWidgets import QApplication,QWidget, QPushButton, QMainWindow
import sys

app = QApplication()

# Cualquier componente puede ser una ventana en pyside
# ventana = QPushButton('Botón de PySide')
ventana = QMainWindow()

ventana.resize(600,400)

ventana.setWindowTitle('Hola mundo con PySide6')

ventana.show()

sys.exit(app.exec())