# Tamaño ventana 300x130 (largo,alto) / (x,y)
# Dos etiquetas: Usuario (0,0) | Contraseña (1,0)
# Dos caja de texto (entry): (0,1) | (1,1)
# Un botón: Acceder (0,2) (columnspan 2)

# Columnas c1 = 1 | c2 = 3
# Filas f1 = 1 | f2 = 1 | f3 = 3
# Agregar padding
# Evento por presionar login, mostrar una caja de mensaje informativa con Usuario: {usuario} | Contraseña: {}

import tkinter as tk
from tkinter import ttk,messagebox,Menu

class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        # ventana = tk.Tk()
        self.geometry('300x130')
        self.title('Login')
        self.iconbitmap('login.ico')
        self.resizable(0,0)

        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=3)
        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=1)
        self.rowconfigure(2,weight=3)

        self._crear_widgets()

        # definimos el método crear componente
    def _crear_widgets(self):


        etiqueta_usuario = tk.Label(self, text='Usuario:')
        etiqueta_usuario.grid(row=0,column=0,sticky='E')

        etiqueta_contraseña = tk.Label(self, text='Contraseña:')
        etiqueta_contraseña.grid(row=1,column=0,sticky='E')

        self.entrada_usuario = ttk.Entry(self)
        self.entrada_usuario.insert(0,'Ingrese su usuario')
        self.entrada_usuario.config(foreground='gray',justify='center')
        self.entrada_usuario.bind('<Button-1>',lambda e:[self.entrada_usuario.delete(0,tk.END), self.entrada_usuario.config(foreground='black')])
        self.entrada_usuario.grid(row=0,column=1,sticky='NSWE',padx=10,pady=8)

        self.entrada_contraseña = ttk.Entry(self)
        self.entrada_contraseña.insert(0,'Ingrese su contraseña')
        self.entrada_contraseña.config(foreground='gray',justify='center')
        self.entrada_contraseña.bind('<Button-1>',lambda e:[self.entrada_contraseña.delete(0,tk.END),self.entrada_contraseña.config(show='*'),self.entrada_contraseña.config(foreground='black')])
        self.entrada_contraseña.grid(row=1,column=1,sticky='NSWE', padx=10,pady=8)

        boton_acceder = ttk.Button(self,text='Acceder',command=self._acceder)
        boton_acceder.grid(row=2,column=0, columnspan=2, pady=5, sticky='n')

    def _acceder(self):
        messagebox.showinfo('Accediendo', f'Usuario: {self.entrada_usuario.get()} | Contraseña {self.entrada_contraseña.get()}')


if __name__ == '__main__':
    login_ventana = Login()
    login_ventana.mainloop()