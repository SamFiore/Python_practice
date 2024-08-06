import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import time


class VentanaComponentes(tk.Tk):
    def __init__(self):
        super().__init__()
        # Geometry(EjeXxEjeY+Horizontal+Vertical)
        self.geometry('650x400+400+190')
        self.title('Tabuladores Tkinter')
        self.iconbitmap('icono2.ico')
        self._crear_tabs()

    def _componentes_tab1(self,tab1):
        # Agregamos una etiquete y un componente de entrada
        etiqueta1 = ttk.Label(tab1, text='Nombre:')
        etiqueta1.grid(row=0,column=0, sticky='E')
        self.entrada1 = ttk.Entry(tab1,width=30)
        self.entrada1.grid(row=0,column=1,padx=5,pady=5)

        def enviar():
            messagebox.showinfo('Mensaje',f'Nombre: {self.entrada1.get()}')

        # Agregamos un botón
        boton1 = ttk.Button(tab1,text='Enviar',command=enviar)
        boton1.grid(row=1,column=0,columnspan=2)

    def _componentes_tab2(self,tab2):
        contenido = 'Este es mi texto con el contenido'
        # Creamos el componente de scroll
        scroll = scrolledtext.ScrolledText(tab2,width=50,height=10,wrap=tk.WORD)
        scroll.insert(tk.INSERT,contenido)
        # Mostramos el componente
        scroll.grid(row=0,column=0)

    def _componentes_tab3(self,tab3):
        # Creamos una lista usando data list comprehension
        datos = [x+1 for x in range(10)]
        combo_box = ttk.Combobox(tab3,width=15, values=datos)
        combo_box.grid(row=0,column=0,padx=10,pady=10)
        # Seleccionamos un elemento a mostrar por default 
        combo_box.current(5)
        # Agregamos un botón para saber que opción selecciona el usuario
        def mostrar_valor():
            messagebox.showinfo('Valor seleccionado',f'Valor seleccionado: {combo_box.get()}')
        boton1 = ttk.Button(tab3,text='Mostrar valor',command=mostrar_valor)
        boton1.grid(row=1,column=0)

    def _componentes_tab4(self,tab4):
        imagen = tk.PhotoImage(file='python-logo.png')
        def mostrar_titulo():
            messagebox.showinfo('Más info de la imagen',f'Nombre imagen: {imagen.cget("file")}')
        boton_imagen = ttk.Button(tab4,image=imagen, command=mostrar_titulo)
        boton_imagen.grid(row=0,column=0)

    def _componentes_tab5(self,tab5):
        # Creamos el componente de barra de progreso
        barra_progreso = ttk.Progressbar(tab5,orient='horizontal',length=550)
        barra_progreso.grid(row=0,column=0,padx=10,pady=10, columnspan=4)
    # Métodos para controlar los eventos de la barra de progreso
        def ejecutar_barra():
            barra_progreso['maximum'] =  100
            for valor in range(101):
                # Mandamos a esperar un poco antes de continuar con la ejecución de la barra
                time.sleep(0.01)
                # Incrementamos nuestra barra de progreso
                barra_progreso['value'] = valor
                # Actualizamos la barra de progreso
                barra_progreso.update()
            barra_progreso['value'] = 0
            

        def ejecutar_ciclo():
            barra_progreso.start()
        def detener():
            barra_progreso.stop()
        def detener_despues():
            esperar_ms = 1000
            self.after(esperar_ms,barra_progreso.stop())

        # Botones para controlar los eventos de una barra de progreso
        boton_inicio = ttk.Button(tab5,text='Ejecutar barra de progreso',command=ejecutar_barra)
        boton_inicio.grid(row=1,column=0)
        boton_ciclo = ttk.Button(tab5,text='Ejecutar ciclo',command=ejecutar_ciclo)
        boton_ciclo.grid(row=1,column=1)
        boton_detener = ttk.Button(tab5,text='Detener ejecución',command=detener)
        boton_detener.grid(row=1,column=2)
        boton_despues = ttk.Button(tab5,text='Detener ejecución después...',command=detener_despues)
        boton_despues.grid(row=1,column=3)

    def _crear_tabs(self):
        # Creamos un tab control, para ello usamos la clase de Notebook
        control_tab = ttk.Notebook(self)

        # Agregamos un frame para agregar dentro del tab y organizar los elementos
        tab1 = ttk.Frame(control_tab)
        # Agregamos el tab al control de tab
        control_tab.add(tab1, text='Tabulador 1')
        # Mostramos el tab
        control_tab.pack(fill='both')
        # Creamos un métodos de los componetes del tab1
        self._componentes_tab1(tab1)

        # Creamos un segundo tab
        tab2 = ttk.LabelFrame(control_tab,text='Contenido')
        control_tab.add(tab2,text='Tabulador 2')
        # Creamos los componentes del segundo tab
        self._componentes_tab2(tab2)

        # Creamos un tercer tab
        tab3 = ttk.LabelFrame(control_tab,text='DataList')
        control_tab.add(tab3,text='Tabulador 3')
        # Creamos los componentes del tab3
        self._componentes_tab3(tab3)

        # Creamos un cuarto tab
        tab4 = ttk.LabelFrame(control_tab,text='Imagen')
        control_tab.add(tab4,text='Tabulador 4')
        self._componentes_tab4(tab4)

        # Creamos un quinto tab
        tab5 = ttk.LabelFrame(control_tab,text='Progress bar')
        control_tab.add(tab5,text='Tabulador 5')
        self._componentes_tab5(tab5)

if __name__ == '__main__':
    # Creamos un objeto de nuestra clase
    ventana_componentes = VentanaComponentes()
    ventana_componentes.mainloop()