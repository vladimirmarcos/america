
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from  tkcalendar import DateEntry
from Procesamiento import procesar_dato_int,procesar_dato_str,procesar_dato_float,procesar_dato_fecha
from windows.creacion_frame_busquedas import FrameBusqueda
from models.cuentas_dao import verifica_cuenta,buscar_nombre
from models.models import Creditos,Fechas_Vencimiento,Garantes
from models.creditos_dao import carga_nueva_credito,max_credito,gravar_fechas,guardar_garante
from Procesamiento import procesar_dato_int,procesar_dato_float
import datetime

class FrameCredito(FrameBusqueda):
    def __init__(self, parent):
        super().__init__(parent)
        #self.pack(fill=tk.BOTH, expand=tk.YES)
        self.campos_credito()
        self.desahabilitar_campos_nuevo_credito()
        self.desahabilitar_busqueda_nombre()
        self.habilitar_opciones()
        
    def campos_credito(self):
        #label de campos
        self.label_cuenta=tk.Label(self,text='Cuenta (obligatorio)')
        self.label_cuenta.config(font=('Arial',12,'bold'))
        self.label_cuenta.grid(row=1,column=0,padx=10,pady=10)
  
        self.label_cuotas=tk.Label(self,text='Cuotas (obligatorio)')
        self.label_cuotas.config(font=('Arial',12,'bold'))
        self.label_cuotas.grid(row=2,column=0,padx=10,pady=10)

        self.label_Productos=tk.Label(self,text='Productos (obligatorio)')
        self.label_Productos.config(font=('Arial',12,'bold'))
        self.label_Productos.grid(row=3,column=0,padx=10,pady=10)

        self.label_monto_financiado=tk.Label(self,text='Monto financiado (obligatorio)')
        self.label_monto_financiado.config(font=('Arial',12,'bold'))
        self.label_monto_financiado.grid(row=4,column=0,padx=10,pady=10)

        self.label_anticipo=tk.Label(self,text='Anticipo (obligatorio)')
        self.label_anticipo.config(font=('Arial',12,'bold'))
        self.label_anticipo.grid(row=5,column=0,padx=10,pady=10)

        self.label_primera_cuota=tk.Label(self,text='Primera Cuota')
        self.label_primera_cuota.config(font=('Arial',12,'bold'))
        self.label_primera_cuota.grid(row=6,column=0,padx=10,pady=10)

        self.label_segunda_cuota=tk.Label(self,text='Segunda cuota')
        self.label_segunda_cuota.config(font=('Arial',12,'bold'))
        self.label_segunda_cuota.grid(row=7,column=0,padx=10,pady=10)

        self.label_nombre_garante=tk.Label(self,text='Nombre Garante (obligatorio)')
        self.label_nombre_garante.config(font=('Arial',12,'bold'))
        self.label_nombre_garante.grid(row=9,column=0,padx=10,pady=10)

        self.label_telefono_garante=tk.Label(self,text='Telefono Garante')
        self.label_telefono_garante.config(font=('Arial',12,'bold'))
        self.label_telefono_garante.grid(row=10,column=0,padx=10,pady=10)

        self.label_direccion_garante=tk.Label(self,text='Direccion Garante')
        self.label_direccion_garante.config(font=('Arial',12,'bold'))
        self.label_direccion_garante.grid(row=11,column=0,padx=10,pady=10)

        self.label_mensaje_opciones_h=tk.Label(self,text='Presione h o H en  opciones para habilitar campos de credito',justify=tk.LEFT)
        self.label_mensaje_opciones_h.config(font=('Arial',12,'bold'))
        self.label_mensaje_opciones_h.grid(row=12,column=0)

        #Entrys de cada Campo

        self.mi_cuenta=tk.StringVar()
        self.entry_cuenta=tk.Entry(self,textvariable=self.mi_cuenta)
        self.entry_cuenta.config(width=50,font=('Arial',12))
        self.entry_cuenta.grid(row=1,column=1,padx=10,pady=10,columnspan=2)

        self.mi_cuotas=tk.StringVar()
        self.entry_cuotas=tk.Entry(self,textvariable=self.mi_cuotas)
        self.entry_cuotas.config(width=50,font=('Arial',12))
        self.entry_cuotas.grid(row=2,column=1,padx=10,pady=10,columnspan=2)

        self.mi_productos=tk.StringVar()
        self.entry_productos=tk.Entry(self,textvariable=self.mi_productos)
        self.entry_productos.config(width=50,font=('Arial',12))
        self.entry_productos.grid(row=3,column=1,padx=10,pady=10,columnspan=2)

        self.mi_monto_financiado=tk.StringVar()
        self.entry_monto_financiado=tk.Entry(self,textvariable=self.mi_monto_financiado)
        self.entry_monto_financiado.config(width=50,font=('Arial',12))
        self.entry_monto_financiado.grid(row=4,column=1,padx=10,pady=10,columnspan=2)

        self.mi_anticipo=tk.StringVar()
        self.entry_anticipo=tk.Entry(self,textvariable=self.mi_anticipo)
        self.entry_anticipo.config(width=50,font=('Arial',12))
        self.entry_anticipo.grid(row=5,column=1,padx=10,pady=10,columnspan=2)

        self.cal_1=DateEntry(self,
                           width=70,
                           locale='es_ES',
                           date_pattern='y-mm-dd')
        self.cal_1.grid(row=6,column=1,padx=10,pady=10,columnspan=2)

        self.cal_2=DateEntry(self,
                           width=70,
                           locale='es_ES',
                           date_pattern='y-mm-dd')
        self.cal_2.grid(row=7,column=1,padx=10,pady=10,columnspan=2)

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

        self.entry_cuenta.bind ("<Return>",self.genera_nuevo_credito)
        self.entry_cuotas.bind ("<Return>",self.genera_nuevo_credito)
        self.entry_productos.bind ("<Return>",self.genera_nuevo_credito)
        self.entry_monto_financiado.bind ("<Return>",self.genera_nuevo_credito)
        self.entry_anticipo.bind ("<Return>",self.genera_nuevo_credito)
        self.entry_nombre_garante.bind ("<Return>",self.genera_nuevo_credito)
        self.entry_telefono_garante.bind ("<Return>",self.genera_nuevo_credito)
        self.entry_direccion_garante.bind ("<Return>",self.genera_nuevo_credito)
     
        self._frame = None
    
    def desahabilitar_campos_nuevo_credito(self):
              self.mi_cuenta.set('')
              self.mi_cuotas.set('')
              self.mi_productos.set('')
              self.mi_monto_financiado.set('')
              self.mi_anticipo.set('')
              self.mi_nombre_garante.set('')
              self.mi_telefono_garante.set('')
              self.mi_direccion_garante.set('')
              self.mi_opciones.set('')
        
              self.entry_cuenta.config(state='disabled')
              self.entry_cuotas.config(state='disabled')
              self.entry_productos.config(state='disabled')
              self.entry_monto_financiado.config(state='disabled')
              self.entry_anticipo.config(state='disabled')
              self.entry_nombre_garante.config(state='disabled')
              self.entry_telefono_garante.config(state='disabled')
              self.entry_direccion_garante.config(state='disabled')
              self.entry_opciones.focus()

    def habilitar_campos_nuevos_credito(self):
              self.entry_cuenta.config(state='normal')
              self.entry_cuotas.config(state='normal')
              self.entry_productos.config(state='normal')
              self.entry_monto_financiado.config(state='normal')
              self.entry_anticipo.config(state='normal')
              self.entry_nombre_garante.config(state='normal')
              self.entry_telefono_garante.config(state='normal')
              self.entry_direccion_garante.config(state='normal')
              self.entry_cuenta.focus()

    def genera_nuevo_credito(self,event):
             
       cuenta=procesar_dato_int(self.mi_cuenta.get())
       cuotas=procesar_dato_int(self.mi_cuotas.get())
       producto=procesar_dato_str(self.mi_productos.get())
       monto_financiado=procesar_dato_float(self.mi_monto_financiado.get())
       anticipo=procesar_dato_float(self.mi_anticipo.get())
       nombre_garante=procesar_dato_str(self.mi_nombre_garante.get())
       telefono_garante=self.mi_telefono_garante.get()
       direccion_garante=procesar_dato_str(self.mi_direccion_garante.get())
       if (cuenta and cuotas and monto_financiado and anticipo!=None ):
          
          if ((producto!="") and (nombre_garante!="")):
                  cuenta=verifica_cuenta(cuenta)
                  if (cuenta=="no se pudo abrir la base de datos intente más tarde"):
                   titulo="No se ingresar a la base de datos"
                   mensaje= cuenta 
                   messagebox.showerror(titulo,mensaje)
                   self.desahabilitar_campos_nuevo_credito()
                  
                  if cuenta and cuenta!="no se pudo abrir la base de datos intente más tarde":
                    monto_cuota=monto_financiado/cuotas
                    acuenta=anticipo
                    while acuenta>monto_cuota:
                         cuotas=cuotas-1
                         acuenta=abs(acuenta-monto_cuota)
                         
                    fecha_1=self.cal_1.get_date()
                    fecha_2=self.cal_2.get_date()
                    fechas=self.generar_fechas(fecha_1,fecha_2,cuotas)
                    hoy= datetime.datetime.today()
                    hoy=datetime.datetime.strftime(hoy,'%Y%m%d')
                    if telefono_garante=="":
                         telefono_garante="No tiene teléfono"
                    if direccion_garante=="":
                         direccion_garante="No tiene dirección"
                    credito_nuevo=Creditos(cuenta,cuotas,producto,monto_financiado,anticipo,hoy,1,"muy bueno")
                    datos=buscar_nombre(cuenta)
                    nombre=datos[0]
                    dni=datos[1]
                    primer_vencimiento=fechas[0]
                    titulo=f"Generación de nuevo credito"
                    mensaje=f"Generación de nuevo credito a cliente con nombre {nombre}, cuyo dni es {dni} por los productos de {credito_nuevo.producto} por total de monto financiado de {credito_nuevo.monto_financiado}, con un anticipo de {credito_nuevo.anticipo}, quedando a cuenta {acuenta}, en {credito_nuevo.cuotas} cuotas de {monto_cuota} con el primer vencimiento el día  {procesar_dato_fecha(primer_vencimiento)} debe pagar la suma de {monto_cuota-acuenta} con garante {nombre_garante} cuyo telefono es {telefono_garante} y su direccion es {direccion_garante}"
                    respuesta = messagebox.askyesno(titulo, mensaje)
                    if respuesta:
                         carga_nueva_credito(credito_nuevo)
                         numero_credito=max_credito()
                         fechas_pagos=Fechas_Vencimiento(fechas[0],
                                          monto_cuota,
                                          0.0,
                                          "Por Pagar",
                                          numero_credito,
                                          acuenta,
                                          1)
                         t=2
                         gravar_fechas(fechas_pagos)
                         for i in range(len(fechas)-1):
                                   fechas_pagos=Fechas_Vencimiento(fechas[i+1],
                                          monto_cuota,
                                          0.0,
                                          "Por Pagar",
                                          numero_credito,
                                          0.0,
                                          t)
                                   gravar_fechas(fechas_pagos)
                                   t=t+1
                         garante=Garantes(nombre_garante,direccion_garante,telefono_garante,numero_credito)
                         guardar_garante(garante)
                         titulo=f"Generación de nuevo credito"
                         mensaje=f"Generación exito de credito, el número es {numero_credito}"
                         messagebox.showinfo(titulo,mensaje)
                         self.desahabilitar_campos_nuevo_credito()

                  else: 
                       titulo="Error al generar el credito"
                       mensaje= "No existe el número de cuenta ingresado" 
                       messagebox.showerror(titulo,mensaje)
                       
                  
          else:
               titulo="Error al generar el credito"
               mensaje= "Los datos del producto y el nombre de garante son obligatorios!!!" 
               messagebox.showerror(titulo,mensaje)
       else:
          titulo="Error al generar el credito"
          mensaje= "Los datos de cuenta, de monto financiado,anticipos o numero de cuotas no son validos o estan vacios!!!" 
          messagebox.showerror(titulo,mensaje)
                        
    def generar_fechas(self,fecha_1,fecha_2,cuotas):
         lista=[]
         dia_delta=datetime.timedelta(days=31)
         if(fecha_1==fecha_2):
              fecha=fecha_1+dia_delta
              fecha_texto=datetime.datetime.strftime(fecha,"%Y%m%d")
              lista.append(fecha_texto)
              for i in range(cuotas-1): 
                   fecha=fecha+dia_delta
                   fecha_texto=datetime.datetime.strftime(fecha,"%Y%m%d")
                   lista.append(fecha_texto)
              
              return lista
         if(fecha_1>fecha_2):
              fecha=fecha_1
              fecha_texto=datetime.datetime.strftime(fecha,"%Y%m%d")
              lista.append(fecha_texto)
              for i in range(cuotas-1): 
                   fecha=fecha+dia_delta
                   fecha_texto=datetime.datetime.strftime(fecha,"%Y%m%d")
                   lista.append(fecha_texto)
              
              return lista
         if (fecha_1<fecha_2):
              fecha_texto=datetime.datetime.strftime(fecha_1,"%Y%m%d")
              lista.append(fecha_texto)
              fecha_texto=datetime.datetime.strftime(fecha_2,"%Y%m%d")
              lista.append(fecha_texto)
              fecha=fecha_2
              for i in range(cuotas-2): 
                   fecha=fecha+dia_delta
                   fecha_texto=datetime.datetime.strftime(fecha,"%Y%m%d")
                   lista.append(fecha_texto)
              return lista
         
    def verifica_tecla(self,event):
         super().verifica_tecla(event)
         if self.variable=='H' or self.variable=='h':
              self.habilitar_campos_nuevos_credito()
       
class FrameCreditoNuevo(FrameCredito):
     def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=tk.YES)
