import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('manejo de grid')
ventana.iconbitmap('icono2.ico')

# Configurar el grid
ventana.rowconfigure(0,weight=1)
ventana.rowconfigure(1,weight=5)
ventana.columnconfigure(0,weight=1)
ventana.columnconfigure(1,weight=5)


# Métodos de los eventos
def evento1():
    boton1.config(text='Botón 1 presionado')
def evento2():
    boton2.config(text='Botón 2 presionado')
def evento3():
    boton3.config(text='Botón 3 presionado')
def evento4():
    boton4.config(text='Botón 4 presionado')

# Definimos 2 botones
# N (norte), E (este/derecha), S (sur), W (oeste/izquierda)
boton1 = ttk.Button(ventana, text='Botón 1', command=evento1)
boton1.grid(row=0,column=0,sticky='NSEW')
# WE (Rellenar de izquierda a derecha), NW (Rellenar de arriba a abajo)
boton2 = ttk.Button(ventana, text='Botón 2', command=evento2)
boton2.grid(row=1,column=0,sticky='NSEW')
boton3 = ttk.Button(ventana, text='Botón 3', command=evento3)
boton3.grid(row=0,column=1,sticky='NSEW')
boton4 = ttk.Button(ventana, text='Botón 4', command=evento4)
boton4.grid(row=1,column=1,sticky='NSEW')

ventana.mainloop()