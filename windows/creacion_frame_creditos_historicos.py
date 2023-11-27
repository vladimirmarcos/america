import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from  tkcalendar import DateEntry
from Procesamiento import procesar_dato_int,procesar_dato_str,procesar_dato_float
from windows.creacion_frame_creditos import FrameCredito
from models.cuentas_dao import verifica_cuenta,buscar_nombre
from models.models import Creditos,Fechas_Vencimiento,Garantes
from models.creditos_dao import carga_nueva_credito,max_credito,gravar_fechas,guardar_garante
from Procesamiento import procesar_dato_int,procesar_dato_float,procesar_dato_fecha
from models.general_dao import actualizar_intereses
import datetime

class FrameCreditoHistoricos(FrameCredito):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=tk.YES)
        self.campos_credito()
        self.desahabilitar_campos_nuevo_credito()
        self.desahabilitar_busqueda_nombre()
        self.habilitar_opciones()

    def campos_credito(self):
        super().campos_credito()
        self.cal_1=DateEntry(self,
                             year=2022, 
                            month=1, day=1,
                           width=70,
                           locale='es_ES',
                           date_pattern='y-mm-dd')
        self.cal_1.grid(row=6,column=1,padx=10,pady=10,columnspan=2)

        self.cal_2=DateEntry(self,
                             year=2022, 
                            month=1, day=1,
                           width=70,
                           locale='es_ES',
                           date_pattern='y-mm-dd')
        self.cal_2.grid(row=7,column=1,padx=10,pady=10,columnspan=2)
        self.label_fecha_emision=tk.Label(self,text='Fecha emisión')
        self.label_fecha_emision.config(font=('Arial',12,'bold'))
        self.label_fecha_emision.grid(row=8,column=0,padx=10,pady=10)

        self.cal_3=DateEntry(self,
                             year=2022, 
                            month=1, day=1,
                           width=70,
                           locale='es_ES',
                           date_pattern='y-mm-dd')
        self.cal_3.grid(row=8,column=1,padx=10,pady=10,columnspan=2)

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
                    fecha_3=self.cal_3.get_date()
                    hoy=datetime.date.today()
                    if (fecha_1!=hoy and fecha_2!=hoy and fecha_3!=hoy):
                         fechas=self.generar_fechas(fecha_1,fecha_2,cuotas)
                         fecha_emision=datetime.datetime.strftime(fecha_3,'%Y%m%d')
                         credito_nuevo=Creditos(cuenta,cuotas,producto,monto_financiado,anticipo,fecha_emision,1,"muy bueno")
                         if telefono_garante=="":
                              telefono_garante="No tiene teléfono"
                         if direccion_garante=="":
                              direccion_garante="No tiene dirección"
                         credito_nuevo=Creditos(cuenta,cuotas,producto,monto_financiado,anticipo,fecha_emision,1,"muy bueno")
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
                              actualizar_intereses()          
                    else:
                        titulo="Error al generar el credito"
                        mensaje= f"La fecha vencimiento 1 {fecha_1}, la fecha de vencimiento 2 {fecha_2} o la fecha de emisión {fecha_3} coiciden con la fecha de hoy {hoy}" 
                        messagebox.showerror(titulo,mensaje)
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
              fecha=fecha_1
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