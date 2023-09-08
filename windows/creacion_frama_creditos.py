import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Procesamiento import procesar_dato_int,procesar_dato_str,procesar_dato_float
from windows.creacion_frame_busquedas import FrameBusqueda
from models.cuentas_dao import verifica_cuenta
from models.models import Creditos
from models.creditos_dao import busca_montos
from Procesamiento import procesar_dato_int,procesar_dato_float
import sqlite3
import datetime
import math

class FrameCredito(FrameBusqueda):
    def __init__(self, parent):
        super().__init__(parent)
        self.campos_credito()
      


    def campos_credito(self):
        #label de campos
        self.label_cuenta=tk.Label(self,text='Cuenta')
        self.label_cuenta.config(font=('Arial',12,'bold'))
        self.label_cuenta.grid(row=5,column=0,padx=10,pady=10)

        
        self.label_cuotas=tk.Label(self,text='Cuotas')
        self.label_cuotas.config(font=('Arial',12,'bold'))
        self.label_cuotas.grid(row=6,column=0,padx=10,pady=10)

        self.label_Productos=tk.Label(self,text='Productos')
        self.label_Productos.config(font=('Arial',12,'bold'))
        self.label_Productos.grid(row=7,column=0,padx=10,pady=10)

        self.label_monto_financiado=tk.Label(self,text='Monto financiado')
        self.label_monto_financiado.config(font=('Arial',12,'bold'))
        self.label_monto_financiado.grid(row=8,column=0,padx=10,pady=10)

        



        #Entrys de cada Campo

        self.mi_cuenta=tk.StringVar()
        self.entry_cuenta=tk.Entry(self,textvariable=self.mi_cuenta)
        self.entry_cuenta.config(width=50,font=('Arial',12))
        self.entry_cuenta.grid(row=5,column=1,padx=10,pady=10,columnspan=2)

        self.mi_cuotas=ttk.Combobox(self,
                                      state="readonly",
                                      values=["1", "2","3","4",
                                              "5", "6","7","8",
                                              "9", "10","11","12",])
        self.mi_cuotas.config(width=50, height=200,font=('Arial',12))
        self.mi_cuotas.grid(row=6,column=1,padx=10,pady=10,columnspan=2)
        

        self.mi_productos=tk.StringVar()
        self.entry_productos=tk.Entry(self,textvariable=self.mi_productos)
        self.entry_productos.config(width=50,font=('Arial',12))
        self.entry_productos.grid(row=7,column=1,padx=10,pady=10,columnspan=2)

        self.mi_monto_financiado=tk.StringVar()
        self.entry_monto_financiado=tk.Entry(self,textvariable=self.mi_monto_financiado)
        self.entry_monto_financiado.config(width=50,font=('Arial',12))
        self.entry_monto_financiado.grid(row=8,column=1,padx=10,pady=10,columnspan=2)
        self._frame = None

    def borrar(self):
        self.pack_forget()
        self.destroy()



class FrameCreditoNuevo(FrameCredito):
        def __init__(self, parent):
            super().__init__(parent)
            self.pack(fill=tk.BOTH, expand=tk.YES)
            self.campos_credito()
            self.campos_garante()
            self.desahabilitar_campos_nuevo_credito()

        def campos_garante(self):
        #label de campos
            self.label_nombre_garante=tk.Label(self,text='Nombre Garante')
            self.label_nombre_garante.config(font=('Arial',12,'bold'))
            self.label_nombre_garante.grid(row=9,column=0,padx=10,pady=10)

            self.label_telefono_garante=tk.Label(self,text='Telefono Garante')
            self.label_telefono_garante.config(font=('Arial',12,'bold'))
            self.label_telefono_garante.grid(row=10,column=0,padx=10,pady=10)

            self.label_direccion_garante=tk.Label(self,text='Direccion Garante')
            self.label_direccion_garante.config(font=('Arial',12,'bold'))
            self.label_direccion_garante.grid(row=11,column=0,padx=10,pady=10)

            #Entrys de cada Campo

            self.mi_nombre_garante=tk.StringVar()
            self.entry_nombre_garante=tk.Entry(self,textvariable=self.mi_nombre_garante)
            self.entry_nombre_garante.config(width=50,font=('Arial',12))
            self.entry_nombre_garante.grid(row=9,column=1,padx=10,pady=10,columnspan=2)

            self.mi_telefono_garante=tk.StringVar()
            self.entry_telefono_garante=tk.Entry(self,textvariable=self.mi_telefono_garante)
            self.entry_telefono_garante.config(width=50,font=('Arial',12))
            self.entry_telefono_garante.grid(row=10,column=1,padx=10,pady=10,columnspan=2)

            self.mi_direccion_garante=tk.StringVar()
            self.entry_direccion_garante=tk.Entry(self,textvariable=self.mi_direccion_garante)
            self.entry_direccion_garante.config(width=50,font=('Arial',12))
            self.entry_direccion_garante.grid(row=11,column=1,padx=10,pady=10,columnspan=2)

            self.boton_habilita_nuevo_credito=tk.Button(self,text="Habilitar Carga de credito nuevo",command=self.habilitar_campos_nuevos_credito)
            self.boton_habilita_nuevo_credito.config(width=25,font=('Arial',12,'bold'),fg='#DAD5D6',bg='#158645',cursor='pirate',activebackground='#35BD6F')
            self.boton_habilita_nuevo_credito.grid(row=12,column=2,padx=10,pady=10)

            self.entry_cuenta.bind ("<Return>",self.genera_nuevo_credito)
            self.entry_productos.bind ("<Return>",self.genera_nuevo_credito)
            self.entry_monto_financiado.bind ("<Return>",self.genera_nuevo_credito)
            self.entry_nombre_garante.bind ("<Return>",self.genera_nuevo_credito)
            self.entry_telefono_garante.bind ("<Return>",self.genera_nuevo_credito)
            self.entry_direccion_garante.bind ("<Return>",self.genera_nuevo_credito)

            self._frame = None

        def desahabilitar_campos_nuevo_credito(self):
              self.mi_cuenta.set('')
              self.mi_cuotas.set('1')
              self.mi_productos.set('')
              self.mi_monto_financiado.set('')
              self.mi_nombre_garante.set('')
              self.mi_telefono_garante.set('')
              self.mi_direccion_garante.set('')
        
              self.entry_cuenta.config(state='disabled')
              self.mi_cuotas.config(state='disabled')
              self.entry_productos.config(state='disabled')
              self.entry_monto_financiado.config(state='disabled')
              self.entry_nombre_garante.config(state='disabled')
              self.entry_telefono_garante.config(state='disabled')
              self.entry_direccion_garante.config(state='disabled')

        def habilitar_campos_nuevos_credito(self):
              self.entry_cuenta.config(state='normal')
              self.mi_cuotas.config(state='normal')
              self.entry_productos.config(state='normal')
              self.entry_monto_financiado.config(state='normal')
              self.entry_nombre_garante.config(state='normal')
              self.entry_telefono_garante.config(state='normal')
              self.entry_direccion_garante.config(state='normal')

        def genera_nuevo_credito(self,event):
             self.desahabilitar_busqueda_dni()
             self.desahabilitar_busqueda_nombre()
             montos=busca_montos()
             
             cuenta=procesar_dato_int(self.mi_cuenta.get())
             cuotas=procesar_dato_int(self.mi_cuotas.get())
             producto=self.mi_productos.get()
             monto_financiado=procesar_dato_float(self.mi_monto_financiado.get())
             nombre_garante=self.mi_nombre_garante.get()
             telefono_garante=self.mi_telefono_garante.get()
             direccion_garante=self.mi_direccion_garante.get()
             if ((producto=="") or (nombre_garante=="")):
                  titulo="Error al generar el credito"
                  mensaje= "Los datos del producto y el nombre son obligatorios!!!" 
                  messagebox.showerror(titulo,mensaje)
                  #self.desahabilitar_campos_nuevo_credito()
                  return
             if ((cuenta==None)or (monto_financiado==None)):
                  titulo="Error al generar el credito"
                  mensaje= "Los datos de cuenta, de monto financiado o ambos  no son validos!!!" 
                  messagebox.showerror(titulo,mensaje)
                  #self.desahabilitar_campos_nuevo_credito()
                  return
             cuenta=verifica_cuenta(cuenta)
             if (cuenta=="no se pudo abrir la base de datos intente más tarde"):
                   titulo="No se ingresar a la base de datos"
                   mensaje= cuenta 
                   messagebox.showerror(titulo,mensaje)
                   #self.desahabilitar_campos_nuevo_credito()
                   return

             if cuenta != None:
                fecha_actual=datetime.datetime.now()
                fecha_creacion_credito=datetime.datetime.strftime(fecha_actual,"%Y/%m/%d")
                estado=1
                calificacion="Muy bueno"
                monto_credito=monto_financiado*montos[cuotas-1]
                
                Nuevo_credito=Creditos(cuenta,cuotas,producto,monto_financiado,monto_credito,fecha_creacion_credito,estado,calificacion)
                montos_cuotas=math.ceil(monto_credito/cuotas)
                print(montos_cuotas)
                self.desahabilitar_campos_nuevo_credito()
                  
             else:
                  titulo="Error al generar el credito"
                  mensaje= "No se encontro la cuenta" 
                  messagebox.showerror(titulo,mensaje)
                  #self.desahabilitar_campos_nuevo_credito()