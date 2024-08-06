import tkinter as tk
from tkinter import ttk,messagebox

class VentanaCalculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('280x149')
        self.title('Calculadora')
        self.iconbitmap('calculadora.ico')
        self.resizable(0,0)

        self.expresion = ''
        self.entrada = None
        self.var_entrada = tk.StringVar()

        self._caja_numeros()
        self._numeral()

    def _insertar_numero(self,num):
        self.expresion = f'{self.expresion}{num}'
        self.var_entrada.set(self.expresion)

    def _eliminar_todo(self):
        self.entrada.delete(0,tk.END)
        self.expresion = ''

    def _solucion(self):
        try:
            resultado = int(eval(self.expresion))
            self.var_entrada.set(resultado)
            self.expresion = ''
        except:
            messagebox.showerror('Error',f'Error: expresión invalida')
        

    def _componentes_numeral(self,frame,funcion_insertar):
        
        # 1er Reglón
        boton_c = ttk.Button(frame,text='C',command=self._eliminar_todo)
        boton_c.grid(row=0,column=0,columnspan=3,sticky='EW')
        boton_division = ttk.Button(frame,text='/',command=lambda:funcion_insertar('/'))
        boton_division.grid(row=0,column=3)
        # 2do Reglón
        boton_7 = ttk.Button(frame,text='7',command=lambda:funcion_insertar(7))
        boton_7.grid(row=1,column=0)
        boton_8 = ttk.Button(frame,text='8',command=lambda:funcion_insertar(8))
        boton_8.grid(row=1,column=1)
        boton_9 = ttk.Button(frame,text='9',command=lambda:funcion_insertar(9))
        boton_9.grid(row=1,column=2)
        boton_multiplicacion = ttk.Button(frame,text='*',command=lambda:funcion_insertar('*'))
        boton_multiplicacion.grid(row=1,column=3)
        # 3er Reglón
        boton_4 = ttk.Button(frame,text='4',command=lambda:funcion_insertar(4))
        boton_4.grid(row=2,column=0)
        boton_5 = ttk.Button(frame,text='5',command=lambda:funcion_insertar(5))
        boton_5.grid(row=2,column=1)
        boton_6 = ttk.Button(frame,text='6',command=lambda:funcion_insertar(6))
        boton_6.grid(row=2,column=2)
        boton_resta = ttk.Button(frame,text='-',command=lambda:funcion_insertar('-'))
        boton_resta.grid(row=2,column=3)
        # 4to Reglón
        boton_1 = ttk.Button(frame,text='1',command=lambda:funcion_insertar(1))
        boton_1.grid(row=3,column=0)
        boton_2 = ttk.Button(frame,text='2',command=lambda:funcion_insertar(2))
        boton_2.grid(row=3,column=1)
        boton_3 = ttk.Button(frame,text='3',command=lambda:funcion_insertar(3))
        boton_3.grid(row=3,column=2)
        boton_suma = ttk.Button(frame,text='+',command=lambda:funcion_insertar('+'))
        boton_suma.grid(row=3,column=3)
        # 5to Reglón
        boton_0 = ttk.Button(frame,text='0',command=lambda:funcion_insertar(0))
        boton_0.grid(row=4,column=0,columnspan=2,sticky='EW')
        boton_punto = ttk.Button(frame,text='.',command=lambda:funcion_insertar('.'))
        boton_punto.grid(row=4,column=2)
        boton_igual = ttk.Button(frame,text='=',command=self._solucion)
        boton_igual.grid(row=4,column=3)

    def _numeral(self):
        frame_numeral = ttk.Frame(self,relief='solid',width=100,height=326)
        frame_numeral.pack(fill='both',side='bottom')
        for e in range(3):
            frame_numeral.rowconfigure(e,weight=10)
        self._componentes_numeral(frame_numeral,self._insertar_numero)

    def _componentes_caja(self,frame):
        self.entrada = ttk.Entry(frame,justify='right',font=('Segoe',12),textvariable=self.var_entrada)
        self.entrada.pack(fill='x',side='top')

    def _caja_numeros(self):
        frame_caja = ttk.Frame(self,relief='solid',width=100,height=50)
        frame_caja.pack(fill='x')
        self._componentes_caja(frame_caja)


        
    


if __name__ == '__main__':
    ventana_calculadora = VentanaCalculadora()
    ventana_calculadora.mainloop()