from PySide6.QtWidgets import QApplication,QWidget
import sys

# Clase base de Qt (PySide)
# Se encargan de procesar los eventos (event loop)
app = QApplication()

# Creamos un objeto ventana
ventana = QWidget()

# Modificar el tamaño de la ventana
ventana.resize(600,400)

# Cambiar el titulo
ventana.setWindowTitle('Hola mundo con PySide6')


# Mostramos la ventana
ventana.show()

# Se ejecuta la app
sys.exit(app.exec())