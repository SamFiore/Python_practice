# GUI - Graphical Usar Interface
# TKINTER - TK interface

import tkinter as tk
from tkinter import ttk

# Creamos un obj usando la class tk
ventana = tk.Tk()
# Modicamos el tamaño de la ventana
ventana.geometry('600x400')
# Cambiamos el nombre de la ventana
ventana.title('Hola Mundo')
# Configuramos el icono
ventana.iconbitmap('icono2.ico')

# Definimos nuestro método evento_click
def evento_click():
    boton1.config(text='Botón presionado')
    print('Ejecución del evento_click')
    # Creamos un nuevo componente y lo mostramos
    boton2 = ttk.Button(ventana, text='Nuevo botón')
    boton2.pack()

# Creamos nuestro botón (componente o widget), el objeto padre es la ventana
boton1 = ttk.Button(ventana, text='Dar click', command=evento_click)
# Utilizar el pack layout manager para mostrar el botón en la ventana
boton1.pack()

# Iniciamos la ventana (esta línea la ejecutamos al final)
# Si la ejecutamos antes, no se mostrarán los cambios
ventana.mainloop()

