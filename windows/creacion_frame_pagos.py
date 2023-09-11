import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Procesamiento import procesar_dato_int,procesar_dato_str,procesar_dato_float
from windows.creacion_frame_busquedas import FrameBusqueda
from models.cuentas_dao import verifica_cuenta,buscar_nombre
from models.models import Creditos,Fechas_Vencimiento
from models.pagos_dao import buscar_moratoria
from models.creditos_dao import total_credito,buscar_credito
from Procesamiento import procesar_dato_int,procesar_dato_float
import sqlite3
import datetime
import math

class Framepago(FrameBusqueda):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=tk.YES)
       
        self.campos_pagos()
      


    def campos_pagos(self):
        #label de campos
        self.moratoria_base=buscar_moratoria()

        self.label_numero_credito=tk.Label(self,text='Numero Credito')
        self.label_numero_credito.config(font=('Arial',12,'bold'))
        self.label_numero_credito.grid(row=0,column=0,padx=10,pady=10)

        
        self.label_cuotas=tk.Label(self,text='Cuota')
        self.label_cuotas.config(font=('Arial',12,'bold'))
        self.label_cuotas.grid(row=1,column=0,padx=10,pady=10)

        self.label_acuenta=tk.Label(self,text='A cuenta')
        self.label_acuenta.config(font=('Arial',12,'bold'))
        self.label_acuenta.grid(row=2,column=0,padx=10,pady=10)

        self.label_moratoria=tk.Label(self,text='Moratoria actual es de '+str(self.moratoria_base))
        self.label_moratoria.config(font=('Arial',12,'bold'))
        self.label_moratoria.grid(row=3,column=0,padx=10,pady=10)


        self.label_busca_credito=tk.Label(self,text="Buscar creditos de cuenta")
        self.label_busca_credito.config(font=('Arial',12,'bold'))
        self.label_busca_credito.grid(row=4,column=2,padx=10,pady=10)

        

        



        #Entrys de cada Campo

        self.mi_numero_credito=tk.StringVar()
        self.entry_numero_credito=tk.Entry(self,textvariable=self.mi_numero_credito)
        self.entry_numero_credito.config(width=50,font=('Arial',12))
        self.entry_numero_credito.grid(row=0,column=1,padx=10,pady=10,columnspan=2)


        self.mi_cuotas=tk.StringVar()
        self.entry_cuotas=tk.Entry(self,textvariable=self.mi_cuotas)
        self.entry_cuotas.config(width=50,font=('Arial',12))
        self.entry_cuotas.grid(row=1,column=1,padx=10,pady=10,columnspan=2)

        self.mi_acuenta=tk.StringVar()
        self.entry_acuenta=tk.Entry(self,textvariable=self.mi_acuenta)
        self.entry_acuenta.config(width=50,font=('Arial',12))
        self.entry_acuenta.grid(row=2,column=1,padx=10,pady=10,columnspan=2)

        self.mi_moratoria=tk.StringVar()
        self.entry_moratoria=tk.Entry(self,textvariable=self.mi_moratoria)
        self.entry_moratoria.config(width=50,font=('Arial',12))
        self.entry_moratoria.grid(row=3,column=1,padx=10,pady=10,columnspan=2)

        self.mi_busca_credito=tk.StringVar()
        self.entry_busca_credito=tk.Entry(self,textvariable=self.mi_busca_credito)
        self.entry_busca_credito.config(width=50,font=('Arial',12))
        self.entry_busca_credito.grid(row=4,column=3,padx=10,pady=10,columnspan=2)

        self.entry_numero_credito.bind ("<Return>",self.genera_pago)
        self.entry_cuotas.bind ("<Return>",self.genera_pago)
        self.entry_acuenta.bind ("<Return>",self.genera_pago)
        self.entry_moratoria.bind ("<Return>",self.genera_pago)
        self.entry_busca_credito.bind ("<Return>",self.busca_creditos)
        self._frame = None

    def borrar(self):
        self.pack_forget()
        self.destroy()
    

    def busca_creditos(self,event):
        cuenta=procesar_dato_int(self.mi_busca_credito.get())
        if cuenta:
            historial_credito_cuenta=total_credito(cuenta)
            if historial_credito_cuenta:
                mensaje="La cuenta tiene asociado los siguientes creditos"+ "\n"
                for i in historial_credito_cuenta:
                    mensaje=mensaje+"Credito número "+ str(i[0])+ " cuotas de "+ str(i[2])+" por el  producto de  "+ str(i[3])+" \n"
                titulo=" Historial de creditos de cuenta"
                messagebox.showinfo(titulo,mensaje) 
            else: 
                titulo=" Historial de creditos de cuenta"
                mensaje=" la cuenta no tiene asociado ningun credito"
                messagebox.showinfo(titulo,mensaje) 
        
        else:
            titulo=" Error al buscar historial"
            mensaje="El dato ingresado como número de cuenta no es valido"
            messagebox.showerror(titulo,mensaje) 

    def genera_pago(self,event):
        
        credito=procesar_dato_int(self.mi_numero_credito.get())
        print(credito)
        credito=buscar_credito(credito)
        print(credito)
        if credito:
             cuota=self.mi_cuotas.get()
             a_cuenta=self.mi_acuenta.get()
             moratoria=self.mi_moratoria.get()
             if cuota!= "":
                 cuota=procesar_dato_int(cuota)
             if a_cuenta!= "":
                 a_cuenta=procesar_dato_float(a_cuenta)
             if moratoria!= "":
                 self.moratoria_base=procesar_dato_int(moratoria)
             if ((cuota==None) or (a_cuenta==None) or (self.moratoria_base==None)):
                 titulo=" Error al generar el pago"
                 mensaje="Alguno de los datos ingresados no es válido"
                 messagebox.showerror(titulo,mensaje)
             else:
                  if ((cuota=="")and (a_cuenta=="")):
                       titulo=" Error al generar el pago"
                       mensaje="Campos de cuota y a cuenta vacios simultaneamente"
                       messagebox.showerror(titulo,mensaje)
                  else:
                      
                          
                         titulo="se pudo generar el pago"
                         mensaje="El pago se genero de manera exitosa"
                         messagebox.showinfo(titulo,mensaje)
                 
                 
        else:
            titulo=" Error al generar el pago"
            mensaje="El dato ingresado como número de credito no es valido o no existe"
            messagebox.showerror(titulo,mensaje) 