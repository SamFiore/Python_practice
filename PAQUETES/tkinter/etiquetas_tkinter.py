import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Etiquetas Tkinter')
ventana.iconbitmap('icono2.ico')


entrada_var1 = tk.StringVar(value='Aquí va el texto')
entrada1 = tk.Entry(ventana, width=30, textvariable=entrada_var1)
entrada1.grid(row=0,column=0)

# Etiqueta (Label) 
etiqueta_var1 = tk.StringVar(value='Aquí se mostrara el contenido de la caja de texto')
etiqueta1 = tk.Label(ventana,textvariable=etiqueta_var1)
etiqueta1.grid(row=0,column=1,columnspan=2,rowspan=2,padx=40,pady=20)
etiqueta1.config(bg='black',fg='white')

def enviar():
    etiqueta_var1.set(entrada_var1.get())
    entrada_var1.set('Cambio...')

boton1 = ttk.Button(ventana,text='Enviar',command=enviar)
boton1.grid(row=1,column=0,sticky='E')

ventana.mainloop()