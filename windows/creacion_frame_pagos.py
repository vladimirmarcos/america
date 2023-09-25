import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Procesamiento import procesar_dato_int,procesar_dato_fecha,procesar_dato_float
from windows.creacion_frame_busquedas import FrameBusqueda
from models.cuentas_dao import verifica_cuenta,buscar_nombre
from models.models import Creditos,Fechas_Vencimiento
from models.pagos_dao import buscar_moratoria
from models.creditos_dao import total_credito,buscar_credito
from models.pagos_dao import buscar_informacion_cuota
import sqlite3
import datetime
import math

class Framepago(FrameBusqueda):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=tk.YES)
        self.campos_pagos()
        self.desahabilitar_pagos_creditos()
        self.desahabilitar_busqueda_creditos()
        self.desahabilitar_pagos_creditos()
        self.desahabilitar_busqueda_nombre()
      


    def campos_pagos(self):
        #label de campos
        self.moratoria_base=buscar_moratoria()

        self.label_numero_credito=tk.Label(self,text='Numero Credito')
        self.label_numero_credito.config(font=('Arial',12,'bold'))
        self.label_numero_credito.grid(row=1,column=0,padx=10,pady=10)

        
        self.label_cuotas=tk.Label(self,text='Cuota')
        self.label_cuotas.config(font=('Arial',12,'bold'))
        self.label_cuotas.grid(row=2,column=0,padx=10,pady=10)

        self.label_acuenta=tk.Label(self,text='A cuenta')
        self.label_acuenta.config(font=('Arial',12,'bold'))
        self.label_acuenta.grid(row=3,column=0,padx=10,pady=10)

        self.label_moratoria=tk.Label(self,text='Moratoria actual es de '+str(self.moratoria_base))
        self.label_moratoria.config(font=('Arial',12,'bold'))
        self.label_moratoria.grid(row=4,column=0,padx=10,pady=10)


        self.label_busca_credito=tk.Label(self,text="Buscar creditos de cuenta")
        self.label_busca_credito.config(font=('Arial',12,'bold'))
        self.label_busca_credito.grid(row=5,column=1,padx=10,pady=10)

        #Entrys de cada Campo

        self.mi_numero_credito=tk.StringVar()
        self.entry_numero_credito=tk.Entry(self,textvariable=self.mi_numero_credito)
        self.entry_numero_credito.config(width=50,font=('Arial',12))
        self.entry_numero_credito.grid(row=1,column=1,padx=10,pady=10,columnspan=2)


        self.mi_cuotas=tk.StringVar()
        self.entry_cuotas=tk.Entry(self,textvariable=self.mi_cuotas)
        self.entry_cuotas.config(width=50,font=('Arial',12))
        self.entry_cuotas.grid(row=2,column=1,padx=10,pady=10,columnspan=2)

        self.mi_acuenta=tk.StringVar()
        self.entry_acuenta=tk.Entry(self,textvariable=self.mi_acuenta)
        self.entry_acuenta.config(width=50,font=('Arial',12))
        self.entry_acuenta.grid(row=3,column=1,padx=10,pady=10,columnspan=2)

        self.mi_moratoria=tk.StringVar()
        self.entry_moratoria=tk.Entry(self,textvariable=self.mi_moratoria)
        self.entry_moratoria.config(width=50,font=('Arial',12))
        self.entry_moratoria.grid(row=4,column=1,padx=10,pady=10,columnspan=2)

        self.mi_busca_credito=tk.StringVar()
        self.entry_busca_credito=tk.Entry(self,textvariable=self.mi_busca_credito)
        self.entry_busca_credito.config(width=50,font=('Arial',12))
        self.entry_busca_credito.grid(row=5,column=2,padx=10,pady=10,columnspan=2)

        self.entry_numero_credito.bind ("<Return>",self.genera_pago)
        self.entry_cuotas.bind ("<Return>",self.genera_pago)
        self.entry_acuenta.bind ("<Return>",self.genera_pago)
        self.entry_moratoria.bind ("<Return>",self.genera_pago)
        self.entry_busca_credito.bind ("<Return>",self.busca_creditos)
        self._frame = None

    def verifica_tecla(self,event):
         
         super().verifica_tecla(event)
         if self.variable=='H' or self.variable=='h':
              self.habilitar_campos_nuevo_pago()
         elif (self.variable=='C' or self.variable=='c'):
             self.habilitar_busqueda_creditos()
    
    def desahabilitar_pagos_creditos(self):
              self.mi_numero_credito.set('')
              self.mi_cuotas.set('')
              self.mi_acuenta.set('')
              self.mi_moratoria.set('')
              self.mi_opciones.set('')
        
              self.entry_numero_credito.config(state='disabled')
              self.entry_cuotas.config(state='disabled')
              self.entry_acuenta.config(state='disabled')
              self.entry_moratoria.config(state='disabled')
              self.entry_opciones.focus()

    def desahabilitar_busqueda_creditos(self):
        self.mi_busca_credito.set('')
        self.mi_opciones.set('')
        self.entry_busca_credito.config(state='disabled')    
        self.entry_opciones.focus()
    
    def habilitar_busqueda_creditos(self):
        self.entry_busca_credito.config(state='normal')
        self.entry_busca_credito.focus()

    def habilitar_campos_nuevo_pago(self):
              self.entry_numero_credito.config(state='normal')
              self.entry_cuotas.config(state='normal')
              self.entry_acuenta.config(state='normal')
              self.entry_moratoria.config(state='normal')
              self.entry_numero_credito.focus()
    
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
                self.desahabilitar_busqueda_creditos()
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
        if credito:
            credito_encontado=buscar_credito(credito)
        
            if credito_encontado:
               cuota=self.mi_cuotas.get()
               acuenta=self.mi_acuenta.get()
               moratoria=self.mi_moratoria.get()
               if cuota!= "":
                 cuota=procesar_dato_int(cuota)
               if acuenta!= "":
                 acuenta=procesar_dato_float(acuenta)
               
               if moratoria!= "":
                 moratoria=procesar_dato_int(moratoria)
               if ((cuota==None) or (acuenta==None) or (moratoria==None)):
                 titulo=" Error al generar el pago"
                 mensaje="Alguno de los datos ingresados no es válido"
                 messagebox.showerror(titulo,mensaje)
               else: 
                      if ((cuota=="")and (acuenta=="")):
                        titulo=" Error al generar el pago"
                        mensaje="Campos de cuota y a cuenta vacios simultaneamente"
                        messagebox.showerror(titulo,mensaje)
                      else:
                            if (cuota=='P' or cuota=='p'):
                                 informacion_cuota=buscar_informacion_cuota(credito)
                                 monto=informacion_cuota[1]
                                 moratoria_mensaje=buscar_moratoria()
                                 moratoria=moratoria_mensaje/100
                                 hoy=datetime.date.today()
                                 hoy=datetime.datetime.strftime(hoy,'%Y%m%d')
                                 hoystr=procesar_dato_fecha(hoy)
                                 if (informacion_cuota[2]<hoy):
                                     if moratoria:
                                         monto=monto*(1+moratoria/100)
                                     else:
                                         
                                         monto=monto*(1+moratoria)
                                 titulo=f"Pagar cuota "
                                 mensaje=f"¿ Esta seguro de emitir el pago de cuota por el monto {monto} con una mora de {moratoria_mensaje} en la fecha de {hoystr}"
                                 respuesta = messagebox.askyesno(titulo, mensaje)
                            #elif (cuota!='P' and cuota!='p' and cuota):


                                 
                   
                 
            else:
                titulo=" Error al generar el pago"
                mensaje="El dato ingresado como número de credito no existe"
                messagebox.showerror(titulo,mensaje)     
        else:
            titulo=" Error al generar el pago"
            mensaje="El dato ingresado como número de credito no es valido"
            messagebox.showerror(titulo,mensaje) 