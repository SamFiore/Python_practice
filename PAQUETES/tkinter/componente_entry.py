import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Padding Tkinter')
ventana.iconbitmap('icono2.ico')


# width es la cantidad de cáracteres que ocupa la caja
# entrada1 = ttk.Entry(ventana, width=30, justify='center', show='*')
# state=tk.DISABLE deshabilita la caja
entrada1 = ttk.Entry(ventana, width=30, justify='center', state='normal')
entrada1.grid(row=0,column=0)
entrada1.insert(0,'Introduce un str')
entrada1.insert('end','.')
# entrada1.config(state='readonly')

def enviar():
    print(entrada1.get())
    boton1.config(text=entrada1.get())
    # Eliminar el contenido 
    # entrada1.delete(0,'end')
    # Seleccionar el texto de la caja
    entrada1.select_range(0,'end')
    # Para hacerlo efectivo
    entrada1.focus()


# Creamos un botón
boton1 = ttk.Button(ventana,text='Enviar',command=enviar)
boton1.grid(row=1,column=0, sticky='E')

ventana.mainloop()