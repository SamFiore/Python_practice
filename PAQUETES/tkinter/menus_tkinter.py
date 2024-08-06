import tkinter as tk
from tkinter import ttk, messagebox,Menu
import sys

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Etiquetas Tkinter')
ventana.iconbitmap('icono2.ico')

entrada1 = tk.Entry(ventana, width=30)
entrada1.grid(row=0,column=0)

etiqueta_var1 = tk.StringVar(value='Aquí se mostrara el contenido de la caja de texto')
etiqueta1 = tk.Label(ventana,textvariable=etiqueta_var1)
etiqueta1.grid(row=0,column=1,columnspan=2,rowspan=2,padx=40,pady=20)
etiqueta1.config(bg='black',fg='white')

def enviar():
    etiqueta_var1.set(entrada1.get())
    mensaje1 = entrada1.get()
    if mensaje1:
        messagebox.showinfo('Mensaje informativo',mensaje1)

def salir():
    ventana.quit()
    ventana.destroy()
    print('Salimos...')
    sys.exit()

def crear_menu():
    # Configurar el menú principal
    menu_principal = Menu(ventana)
    # tearoff = False (Para que no se separe el menú de nuestra interfaz gráfica)
    # o también puede ser tearoff = 0
    submenu_archivo = Menu(menu_principal, tearoff=0)
    # Agregamos una nueva opción al menú archivo
    submenu_archivo.add_command(label='Nuevo')
    # Agregamos separador
    submenu_archivo.add_separator()
    # Agregamos la opción de salir
    submenu_archivo.add_command(label='Salir', command=salir)

    # Agregamos submenu de ayuda (con la opción 'Acerca de...')
    submenu_ayuda = Menu(menu_principal,tearoff=0)
    submenu_ayuda.add_command(label='Acerca de...')

    # Agregamos el submenú al menú principal
    menu_principal.add_cascade(menu=submenu_archivo, label='Archivo')
    menu_principal.add_cascade(menu=submenu_ayuda, label='Ayuda')
    # Mostramos el menú en la ventana principal
    ventana.config(menu=menu_principal)

boton1 = ttk.Button(ventana,text='Enviar',command=enviar)
boton1.grid(row=1,column=0,sticky='E')

crear_menu()

ventana.mainloop()