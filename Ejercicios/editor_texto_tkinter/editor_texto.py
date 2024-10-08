import tkinter as tk
from tkinter.filedialog import askopenfile, asksaveasfilename

# FileDialog = Ventana de busqueda

class Editor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Editor de texto')
        self.iconbitmap('editor_texto.ico')
        # Configuración del tamaño mínimo de la pantalla 
        # Weight = Ancho
        self.rowconfigure(0,minsize=600,weight=1)
        # Configuración mínima de la primer columna
        self.columnconfigure(1,minsize=600,weight=1)
        # Atributo de campo de texto
        self.campo_texto = tk.Text(self,wrap=tk.WORD)
        # Atributo de archivo
        self.archivo = None
        # Atributo de comprobación si ya se abrió un archivo anteriormente
        self.abierto = False
        # Creación de componentes
        self._crear_componentes()
        self._crear_menu()

    def _abrir_archivo(self):
        # Abrimos el archivo para edición, lectura y escritura
        self.abierto = askopenfile(mode='r+')
        # Eliminamos el texto anterior
        self.campo_texto.delete(1.0,tk.END)
        # Revisamos si hay un archivo
        if not self.abierto:
            return
        # Abrimos el archivo en modo lectura y escritura, pero en modo recurso
        with open(self.abierto.name, 'r+') as self.archivo:
            # Leemos el contenido
            texto = self.archivo.read()
            # Insertamos el contenido en el campo de texto
            self.campo_texto.insert(1.0,texto)
            # Modificamos el título de la app
            self.title(f'*Editor de Texto - {self.archivo.name}')

    def _guardar_archivo(self):
        # Si ya se abrió previamente el archivo, lo sobreescribimos
        if self.abierto:
            # Salvamos el archivo (lo abrimos en modo escritura)
            with open(self.abierto.name, 'w') as self.archivo:
                # Leemos el contenido de la caja de texto
                texto = self.campo_texto.get(1.0,tk.END)
                # Escribimos el contenido al mismo archivo
                self.archivo.write(texto)
                # Cambiamos el nombre del título de la app
                self.title(f'Editor de texto - {self.archivo.name}')
        else: 
            self._guardar_como()

    def _guardar_como(self):
        # Salvamos el archivo actual como un nuevo archivo
        self.archivo = asksaveasfilename(defaultextension='txt',filetypes=[('Archivos de texto','*.txt'), ('Todos los archivos','*.*')])

        if not self.archivo:
            return
        
        # Abrimos el archivo en modo escritura
        with open(self.archivo,'w') as self.archivo:
            # Leemos el contenido de la caja de texto
            texto = self.campo_texto.get(1.0,tk.END)
            # Escribimos el contenido al nuevo archivo
            self.archivo.write(texto)
            # Cambiamos el nombre del archivo
            self.title(f'Editor de texto - {self.archivo.name}')
            # Indicamos que hemos abierto un archivo 
            self.abierto = self.archivo

    def _crear_menu(self):
        # Creamos el menú de la app
        menu_app = tk.Menu(self)
        self.config(menu=menu_app)
        # Agregamos las opciones a nuestro menú
        # Agregamos menú archivo
        menu_archivo = tk.Menu(menu_app,tearoff=False)
        menu_app.add_cascade(label='Archivo', menu=menu_archivo)
        # Agregamos las opciones del menú archivo 
        menu_archivo.add_command(label='Abrir', command=self._abrir_archivo)
        menu_archivo.add_command(label='Guardar',command=self._guardar_archivo)
        menu_archivo.add_command(label='Guardar como...',command=self._guardar_como)
        menu_archivo.add_separator()
        menu_archivo.add_command(label='Salir',command=self.quit)

    def _crear_componentes(self):
        frame_botones =  tk.Frame(self,relief='raised',bd=2)
        boton_abrir = tk.Button(frame_botones,text='Abrir', command=self._abrir_archivo)
        boton_guardar = tk.Button(frame_botones,text='Guardar',command=self._guardar_archivo)
        boton_guardar_como = tk.Button(frame_botones,text='Guardar como...',command=self._guardar_como)
        # Los botones los expandimos de manera horizontal (sticky='ew')
        boton_abrir.grid(row=0,column=0,sticky='ew',padx=5,pady=5)
        boton_guardar.grid(row=1,column=0,sticky='ew',padx=5,pady=5)
        boton_guardar_como.grid(row=2,column=0,sticky='ew',padx=5,pady=5)
        # Se coloca el frame de manera vertical(sticky='ns')
        frame_botones.grid(row=0,column=0,sticky='ns')
        # Agregamos el campo de texto se expandirá por completo en el espacio disponible
        self.campo_texto.grid(row=0,column=1,sticky='nsew')
        self.campo_texto.config(font=('Fira Code',12))



    

if __name__ == '__main__':
    editor = Editor()
    editor.mainloop()