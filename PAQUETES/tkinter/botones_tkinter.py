import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()

ventana.geometry('600x400')
ventana.title('Botones tk')
ventana.iconbitmap('icono2.ico')

def evento1():
    boton1.config(text='Botón 1 presionado')

def evento2():
    # Estas configuraciones se puede hacer solo en botones del paquete directo
    # Fr = Foreground (primer plano)
    # relie (relieve)
    # bg = Background (fondo)
    boton2.config(text='Botón 2 presionado',fg='red',relief='groove', bg='Black')

boton1 = ttk.Button(ventana,text='Botón 1',command=evento1)
boton1.grid(row=0,column=0,sticky='E')

boton2 = tk.Button(ventana,text='Botón 2', command=evento2)
boton2.grid(row=1,column=0, sticky='E')

ventana.mainloop()