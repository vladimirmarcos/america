import tkinter as tk
from models.cuentas_dao import buscar
from tkinter import messagebox
import sqlite3
from models.pagos_dao import buscar_moratoria
import Procesamiento
from Procesamiento import procesar_dato_float
from models.general_dao import actualizo_moratoria
class FrameActualizarMora(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=tk.YES)
        self.campos_actualizar_mora()
        self.desahabilitar_actualiza_mora()
        self.habilitar_opciones()
        
    def campos_actualizar_mora(self):
       #busqueda nombre 
        self.moratoria_base=buscar_moratoria()
        self.label_opciones=tk.Label(self,text='Opciones')
        self.label_opciones.config(font=('Arial',12,'bold'))
        self.label_opciones.grid(row=0,column=1,pady=10)

        self.label_nuevo_valor_mora=tk.Label(self,text='Nuevo valor de Mora')
        self.label_nuevo_valor_mora.config(font=('Arial',12,'bold'))
        self.label_nuevo_valor_mora.grid(row=1,column=0,pady=10)

        self.label_nuevo_valor_mora=tk.Label(self,text=f'El Valor actual de mora es {self.moratoria_base}')
        self.label_nuevo_valor_mora.config(font=('Arial',12,'bold'))
        self.label_nuevo_valor_mora.grid(row=2,column=0,pady=10)

        self.mi_opciones=tk.StringVar()
        self.entry_opciones=tk.Entry(self,textvariable=self.mi_opciones)
        self.entry_opciones.config(width=40,font=('Arial',12))
        self.entry_opciones.grid(row=0,column=2,pady=10,columnspan=2)
        self.entry_opciones.bind ("<Key>",self.verifica_tecla)

        self.mi_actualizar_mora=tk.StringVar()
        self.entry_actualizar_mora=tk.Entry(self,textvariable=self.mi_actualizar_mora)
        self.entry_actualizar_mora.config(width=50,font=('Arial',12))
        self.entry_actualizar_mora.grid(row=2,column=1,pady=10,columnspan=2)
        self.entry_actualizar_mora.bind ("<Return>",self.verificar_mora)

        self.label_mensaje_manejo_mora=tk.Label(self,text='Presione h o H en  opciones para habilitar Cambio de valor de mora',justify=tk.LEFT)
        self.label_mensaje_manejo_mora.config(font=('Arial',12,'bold'))
        self.label_mensaje_manejo_mora.grid(row=50,column=0)
        
        self._frame = None
        
    def habilitar_opciones(self):
         self.mi_opciones.set('')
         self.entry_opciones.config(state='disabled')
         self.entry_opciones.config(state='normal')
         self.entry_opciones.focus()

    def verifica_tecla(self,event):
         self.variable=event.char
         if self.variable=='H' or self.variable=='h':
              self.habilitar_actualizar_mora()

    def desahabilitar_actualiza_mora(self):
            self.mi_actualizar_mora.set('')
            self.entry_actualizar_mora.config(state='disabled')
            self.habilitar_opciones()

    

    def habilitar_actualizar_mora(self):
          self.entry_actualizar_mora.config(state='normal')
          self.entry_actualizar_mora.focus()       

    def verificar_mora(self,event):
         self.moratoria=procesar_dato_float(self.mi_actualizar_mora.get())
         if self.moratoria:
              titulo="Cambio de valor de Mora"
              mensaje= f"""¿Esta seguro de cambiar el valor de mora a {self.moratoria}?"""
              respuesta = messagebox.askyesno(titulo, mensaje)
              if respuesta:
                   actualizo_moratoria(self.moratoria)
                   self.desahabilitar_actualiza_mora()
         else:
              titulo=" Error al generar el pago"
              mensaje="El dato ingresado como cuota es invalido"
              messagebox.showerror(titulo,mensaje)    


   
              
    def borrar(self):
          self.pack_forget()
          self.destroy()