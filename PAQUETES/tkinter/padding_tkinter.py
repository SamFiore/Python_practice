import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Padding Tkinter')
ventana.iconbitmap('icono2.ico')

ventana.rowconfigure(0,weight=1)
ventana.rowconfigure(1,weight=10)
ventana.columnconfigure(0,weight=1)
ventana.columnconfigure(1,weight=10)
# i = inner
# ipad = Padding interno
# pad = Padding
# El padding es el espacio que hay entre los elementos

boton1 = ttk.Button(ventana,text='Botón 1')
boton1.grid(row=0,column=0, sticky='NSEW', padx=40, pady=20, ipadx=10, ipady=5, columnspan=2, rowspan= 2)

boton2 = tk.Button(ventana,text='Botón 2')
# boton2.grid(row=1,column=0, sticky='NSEW')
boton2.config(fg='red',bg='black')

boton3 = ttk.Button(ventana,text='Botón 3')
# boton3.grid(row=0,column=1, sticky='NSEW')

boton4 = tk.Button(ventana,text='Botón 4')
# boton4.grid(row=1,column=1, sticky='NSEW')
boton4.config(fg='red',bg='black')

ventana.mainloop()