
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from  tkcalendar import DateEntry
from Procesamiento import procesar_dato_int,procesar_dato_str,procesar_dato_float
from windows.creacion_frame_busquedas import FrameBusqueda
from models.cuentas_dao import verifica_cuenta,buscar_nombre
from models.models import Creditos,Fechas_Vencimiento
from models.creditos_dao import carga_nueva_credito,max_credito,gravar_fechas
from Procesamiento import procesar_dato_int,procesar_dato_float,procesar_dato_fecha
import datetime



class FrameCreditoHistoricos(FrameBusqueda):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=tk.YES)
        self.campos_credito()
        self.desahabilitar_campos_nuevo_credito()
        self.desahabilitar_busqueda_nombre()
        self.habilitar_opciones()
        
    def campos_credito(self):
        #label de campos
        self.label_cuenta=tk.Label(self,text='Cuenta')
        self.label_cuenta.config(font=('Arial',12,'bold'))
        self.label_cuenta.grid(row=1,column=0,padx=10,pady=10)
  
        self.label_cuotas=tk.Label(self,text='Cuotas Totales')
        self.label_cuotas.config(font=('Arial',12,'bold'))
        self.label_cuotas.grid(row=2,column=0,padx=10,pady=10)

        self.label_cuotas_pagadas=tk.Label(self,text='Cuotas Pagadas hasta la fecha')
        self.label_cuotas_pagadas.config(font=('Arial',12,'bold'))
        self.label_cuotas_pagadas.grid(row=3,column=0,padx=10,pady=10)

        self.label_Productos=tk.Label(self,text='Productos')
        self.label_Productos.config(font=('Arial',12,'bold'))
        self.label_Productos.grid(row=4,column=0,padx=10,pady=10)

        self.label_monto_financiado=tk.Label(self,text='Monto financiado')
        self.label_monto_financiado.config(font=('Arial',12,'bold'))
        self.label_monto_financiado.grid(row=5,column=0,padx=10,pady=10)

        self.label_acuenta=tk.Label(self,text='A Cuenta a la fecha')
        self.label_acuenta.config(font=('Arial',12,'bold'))
        self.label_acuenta.grid(row=6,column=0,padx=10,pady=10)

        self.label_primera_cuota=tk.Label(self,text='Primera Cuota')
        self.label_primera_cuota.config(font=('Arial',12,'bold'))
        self.label_primera_cuota.grid(row=7,column=0,padx=10,pady=10)

        self.label_segunda_cuota=tk.Label(self,text='Segunda cuota')
        self.label_segunda_cuota.config(font=('Arial',12,'bold'))
        self.label_segunda_cuota.grid(row=8,column=0,padx=10,pady=10)

        self.label_fecha_emision=tk.Label(self,text='Fecha de emision')
        self.label_fecha_emision.config(font=('Arial',12,'bold'))
        self.label_fecha_emision.grid(row=9,column=0,padx=10,pady=10)


        self.label_nombre_garante=tk.Label(self,text='Nombre Garante')
        self.label_nombre_garante.config(font=('Arial',12,'bold'))
        self.label_nombre_garante.grid(row=10,column=0,padx=10,pady=10)

        self.label_telefono_garante=tk.Label(self,text='Telefono Garante')
        self.label_telefono_garante.config(font=('Arial',12,'bold'))
        self.label_telefono_garante.grid(row=11,column=0,padx=10,pady=10)

        self.label_direccion_garante=tk.Label(self,text='Direccion Garante')
        self.label_direccion_garante.config(font=('Arial',12,'bold'))
        self.label_direccion_garante.grid(row=12,column=0,padx=10,pady=10)

        self.label_mensaje_opciones_h=tk.Label(self,text='Presione h o H en  opciones para habilitar campos de credito nuevo',justify=tk.LEFT)
        self.label_mensaje_opciones_h.config(font=('Arial',12,'bold'))
        self.label_mensaje_opciones_h.grid(row=14,column=0)

        



        #Entrys de cada Campo

        self.mi_cuenta=tk.StringVar()
        self.entry_cuenta=tk.Entry(self,textvariable=self.mi_cuenta)
        self.entry_cuenta.config(width=50,font=('Arial',12))
        self.entry_cuenta.grid(row=1,column=1,padx=10,pady=10,columnspan=2)

        self.mi_cuotas=tk.StringVar()
        self.entry_cuotas=tk.Entry(self,textvariable=self.mi_cuotas)
        self.entry_cuotas.config(width=50,font=('Arial',12))
        self.entry_cuotas.grid(row=2,column=1,padx=10,pady=10,columnspan=2)

        self.mi_cuotas_pagadas=tk.StringVar()
        self.entry_cuotas_pagadas=tk.Entry(self,textvariable=self.mi_cuotas_pagadas)
        self.entry_cuotas_pagadas.config(width=50,font=('Arial',12))
        self.entry_cuotas_pagadas.grid(row=3,column=1,padx=10,pady=10,columnspan=2)

        self.mi_productos=tk.StringVar()
        self.entry_productos=tk.Entry(self,textvariable=self.mi_productos)
        self.entry_productos.config(width=50,font=('Arial',12))
        self.entry_productos.grid(row=4,column=1,padx=10,pady=10,columnspan=2)

        self.mi_monto_financiado=tk.StringVar()
        self.entry_monto_financiado=tk.Entry(self,textvariable=self.mi_monto_financiado)
        self.entry_monto_financiado.config(width=50,font=('Arial',12))
        self.entry_monto_financiado.grid(row=5,column=1,padx=10,pady=10,columnspan=2)

        self.mi_acuenta=tk.StringVar()
        self.entry_acuenta=tk.Entry(self,textvariable=self.mi_acuenta)
        self.entry_acuenta.config(width=50,font=('Arial',12))
        self.entry_acuenta.grid(row=6,column=1,padx=10,pady=10,columnspan=2)

        self.cal_1=DateEntry(self,
                           width=70,
                           locale='es_ES',
                           date_pattern='y-mm-dd')
        self.cal_1.grid(row=7,column=1,padx=10,pady=10,columnspan=2)

        self.cal_2=DateEntry(self,
                           width=70,
                           locale='es_ES',
                           date_pattern='y-mm-dd')
        self.cal_2.grid(row=8,column=1,padx=10,pady=10,columnspan=2)

        self.cal_3=DateEntry(self,
                           width=70,
                           locale='es_ES',
                           date_pattern='y-mm-dd')
        self.cal_3.grid(row=9,column=1,padx=10,pady=10,columnspan=2)

        self.mi_nombre_garante=tk.StringVar()
        self.entry_nombre_garante=tk.Entry(self,textvariable=self.mi_nombre_garante)
        self.entry_nombre_garante.config(width=50,font=('Arial',12))
        self.entry_nombre_garante.grid(row=10,column=1,padx=10,pady=10,columnspan=2)

        self.mi_telefono_garante=tk.StringVar()
        self.entry_telefono_garante=tk.Entry(self,textvariable=self.mi_telefono_garante)
        self.entry_telefono_garante.config(width=50,font=('Arial',12))
        self.entry_telefono_garante.grid(row=11,column=1,padx=10,pady=10,columnspan=2)

        self.mi_direccion_garante=tk.StringVar()
        self.entry_direccion_garante=tk.Entry(self,textvariable=self.mi_direccion_garante)
        self.entry_direccion_garante.config(width=50,font=('Arial',12))
        self.entry_direccion_garante.grid(row=12,column=1,padx=10,pady=10,columnspan=2)

        self.entry_cuenta.bind ("<Return>",self.genera_nuevo_credito)
        self.entry_cuotas.bind ("<Return>",self.genera_nuevo_credito)
        self.entry_cuotas_pagadas.bind ("<Return>",self.genera_nuevo_credito)
        self.entry_productos.bind ("<Return>",self.genera_nuevo_credito)
        self.entry_monto_financiado.bind ("<Return>",self.genera_nuevo_credito)
        self.entry_acuenta.bind ("<Return>",self.genera_nuevo_credito)
        self.entry_nombre_garante.bind ("<Return>",self.genera_nuevo_credito)
        self.entry_telefono_garante.bind ("<Return>",self.genera_nuevo_credito)
        self.entry_direccion_garante.bind ("<Return>",self.genera_nuevo_credito)
        

        self._frame = None
    

    def campos_busquedas(self):
       #busqueda nombre 
        self.label_opciones=tk.Label(self,text='Opciones')
        self.label_opciones.config(font=('Arial',12,'bold'))
        self.label_opciones.grid(row=0,column=1,pady=10)

        self.label_busqueda_nombre=tk.Label(self,text='Busqueda por nombre')
        self.label_busqueda_nombre.config(font=('Arial',12,'bold'))
        self.label_busqueda_nombre.grid(row=13,column=1,pady=10)

        self.mi_opciones=tk.StringVar()
        self.entry_opciones=tk.Entry(self,textvariable=self.mi_opciones)
        self.entry_opciones.config(width=40,font=('Arial',12))
        self.entry_opciones.grid(row=0,column=2,pady=10,columnspan=2)
        self.entry_opciones.bind ("<Key>",self.verifica_tecla)

        self.mi_busqueda_nombre=tk.StringVar()
        self.entry_busqueda_nombre=tk.Entry(self,textvariable=self.mi_busqueda_nombre)
        self.entry_busqueda_nombre.config(width=50,font=('Arial',12))
        self.entry_busqueda_nombre.grid(row=13,column=2,pady=10,columnspan=2)
        self.entry_busqueda_nombre.bind ("<Return>",self.busqueda_nombre)

        self.label_mensaje_busqueda_b=tk.Label(self,text='Presione b o B en  opciones para habilitar busqueda por nombre',justify=tk.LEFT)
        self.label_mensaje_busqueda_b.config(font=('Arial',12,'bold'))
        self.label_mensaje_busqueda_b.grid(row=15,column=0)
        
        self._frame = None


    def desahabilitar_campos_nuevo_credito(self):
              self.mi_cuenta.set('')
              self.mi_cuotas.set('')
              self.mi_cuotas_pagadas.set('')
              self.mi_productos.set('')
              self.mi_monto_financiado.set('')
              self.mi_acuenta.set('')
              self.mi_nombre_garante.set('')
              self.mi_telefono_garante.set('')
              self.mi_direccion_garante.set('')
              self.mi_opciones.set('')
        
              self.entry_cuenta.config(state='disabled')
              self.entry_cuotas.config(state='disabled')
              self.entry_cuotas_pagadas.config(state='disabled')
              self.entry_productos.config(state='disabled')
              self.entry_monto_financiado.config(state='disabled')
              self.entry_acuenta.config(state='disabled')
              self.entry_nombre_garante.config(state='disabled')
              self.entry_telefono_garante.config(state='disabled')
              self.entry_direccion_garante.config(state='disabled')
              self.entry_opciones.focus()

    def habilitar_campos_nuevos_credito(self):
              self.entry_cuenta.config(state='normal')
              self.entry_cuotas.config(state='normal')
              self.entry_cuotas_pagadas.config(state='normal')
              self.entry_productos.config(state='normal')
              self.entry_monto_financiado.config(state='normal')
              self.entry_acuenta.config(state='normal')
              self.entry_nombre_garante.config(state='normal')
              self.entry_telefono_garante.config(state='normal')
              self.entry_direccion_garante.config(state='normal')
              self.entry_cuenta.focus()

    def genera_nuevo_credito(self,event):
       
       cuenta=procesar_dato_int(self.mi_cuenta.get())
       cuotas_totales=procesar_dato_int(self.mi_cuotas.get())
       cuotas_pagadas=procesar_dato_int(self.mi_cuotas_pagadas.get())
       producto=procesar_dato_str(self.mi_productos.get())
       monto_financiado=procesar_dato_float(self.mi_monto_financiado.get())
       acuenta=procesar_dato_float(self.mi_acuenta.get())
       nombre_garante=procesar_dato_str(self.mi_nombre_garante.get())
       telefono_garante=self.mi_telefono_garante.get()
       direccion_garante=procesar_dato_str(self.mi_direccion_garante.get())
       
       if (cuenta and cuotas_totales and monto_financiado and acuenta!=None and cuotas_pagadas!=None):
         if (cuotas_totales>= cuotas_pagadas):
             monto_cuota=monto_financiado/cuotas_totales
             if (acuenta<monto_cuota):
                if ((producto!="") and (nombre_garante!="")):
                     cuenta=verifica_cuenta(cuenta)
                     if (cuenta=="no se pudo abrir la base de datos intente más tarde"):
                        titulo="No se ingresar a la base de datos"
                        mensaje= cuenta 
                        messagebox.showerror(titulo,mensaje)
                        self.desahabilitar_campos_nuevo_credito()
                     if cuenta and cuenta!="no se pudo abrir la base de datos intente más tarde":
                         fecha_1=self.cal_1.get_date()
                         fecha_2=self.cal_2.get_date()
                         fecha_3=self.cal_3.get_date()
                        
                         hoy=datetime.date.today()
                         fechas=self.generar_fechas(fecha_1,fecha_2,cuotas_totales)
                         if (fecha_1!=hoy and fecha_2!=hoy and fecha_3!=hoy):
                             if telefono_garante=="":
                                   telefono_garante="No tiene teléfono"
                             if direccion_garante=="":
                                   direccion_garante="No tiene dirección"
                             fecha_emision=datetime.datetime.strftime(fecha_3,'%Y%m%d')
                             credito_nuevo=Creditos(cuenta,cuotas_totales,producto,monto_financiado,0,fecha_emision,1,"muy bueno")
                             datos=buscar_nombre(cuenta)
                             nombre=datos[0]
                             dni=datos[1]
                             restante=cuotas_totales-cuotas_pagadas
                             proximo_vencimiento=procesar_dato_fecha(fechas[restante])
                             fecha_emision=procesar_dato_fecha(fecha_emision)
                             titulo=f"Generación de nuevo credito"
                             mensaje=f"Generación de nuevo credito a cliente con nombre {nombre}, cuyo dni es {dni}, con fecha de emisión {fecha_emision} por los productos {credito_nuevo.producto} por un monto financiado de {credito_nuevo.monto_financiado},en {credito_nuevo.cuotas} cuotas de {monto_cuota} con un total de {cuotas_pagadas} cuotas pagadas, quedando a cuenta {acuenta}, , con garante {nombre_garante} cuyo telefono es {telefono_garante} y su direccion es {direccion_garante}, con proximo vencimiento a pagar {proximo_vencimiento} con un faltante a pagar de {monto_cuota-acuenta}"
                             respuesta = messagebox.askyesno(titulo, mensaje)
                             if respuesta:
                                   carga_nueva_credito(credito_nuevo)
                                   numero_credito=max_credito()
                                   cuotas_pagadas_aux=cuotas_pagadas
                                   pagado=0.0
                                   acuenta_auxiliar=0.0
                                   if cuotas_pagadas_aux>0:
                                        estado="Pagado"
                                        pagado=monto_cuota
                                   else:
                                        estado="Por Pagar"
                                        pagado=0.0
                                        acuenta_auxiliar=0.0
                                   if cuotas_pagadas_aux==0:
                                        acuenta_auxiliar=acuenta
                                        pagado=acuenta

                                   fechas_pagos=Fechas_Vencimiento(fechas[0],
                                          monto_cuota,
                                          estado,
                                          numero_credito,
                                          acuenta_auxiliar,
                                          pagado)
                                   gravar_fechas(fechas_pagos)
                                   cuotas_pagadas_aux=cuotas_pagadas_aux-1
                                   for i in range(len(fechas)-1):
                                        if cuotas_pagadas_aux>0:
                                             estado="Pagado"
                                             pagado=monto_cuota
                                        else:
                                             estado="Por Pagar"
                                             pagado=0.0
                                             acuenta_auxiliar=0.0
                                        if cuotas_pagadas_aux==0:
                                             acuenta_auxiliar=acuenta
                                             pagado=acuenta
                                        fechas_pagos=Fechas_Vencimiento(fechas[i+1],
                                          monto_cuota,
                                             estado,
                                          numero_credito,
                                          acuenta_auxiliar,
                                          pagado)
                                        gravar_fechas(fechas_pagos)
                                        cuotas_pagadas_aux=cuotas_pagadas_aux-1
                                   titulo=f"Generación de nuevo credito"
                                   mensaje=f"Generación exito de credito, el número es {numero_credito}"
                                   messagebox.showinfo(titulo,mensaje)
                                   self.desahabilitar_campos_nuevo_credito()
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
               mensaje= f"El valor ingresado como a cuenta {acuenta} es mayor que el monto de una cuota {monto_cuota}!!!" 
               messagebox.showerror(titulo,mensaje)
         
         else:
              titulo="Error al generar el credito"
              mensaje= f"El número ingresado como cuotas totales {cuotas_totales} es menor a cuotas pagadas {cuotas_pagadas}!!!" 
              messagebox.showerror(titulo,mensaje)
              
       else:
          titulo="Error al generar el credito"
          mensaje= f"Los datos de cuenta {cuenta}, el numero de cuotas totales {cuotas_totales}, pagadas {cuotas_pagadas}, el valor a cuenta {acuenta} o el monto financiado {monto_financiado} no son validos o estan vacios!!!" 
          messagebox.showerror(titulo,mensaje)
            
              
    def generar_fechas(self,fecha_1,fecha_2,cuotas):
         lista=[]
         dia_delta=datetime.timedelta(days=31)
         if(fecha_1>=fecha_2):
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
    
    