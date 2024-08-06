import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Padding Tkinter')
ventana.iconbitmap('icono2.ico')

# Definimos una variable que podremos modificar posteriormente (set), leer(get)
entrada_var1 = tk.StringVar(value='Valor por default')
entrada1 = ttk.Entry(ventana, width=30, textvariable=entrada_var1)
entrada1.grid(row=0,column=0)

def enviar():
    # Recuperamos la info a partir de la variable asociado con la caja de texto
    boton1.config(text=entrada_var1.get())
    # Modificaciones utilizamos la variable de texto y el método set
    entrada_var1.set('Cambio...')
    # Recuperamos la información
    print(entrada_var1.get())

boton1 = ttk.Button(ventana,text='Enviar',command=enviar)
boton1.grid(row=1,column=0, sticky='E')

ventana.mainloop()