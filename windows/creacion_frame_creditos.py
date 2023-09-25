
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from  tkcalendar import DateEntry
from Procesamiento import procesar_dato_int,procesar_dato_str,procesar_dato_float
from windows.creacion_frame_busquedas import FrameBusqueda
from models.cuentas_dao import verifica_cuenta,buscar_nombre
from models.models import Creditos,Fechas_Vencimiento
from models.creditos_dao import carga_nueva_credito,max_credito,gravar_fechas
from Procesamiento import procesar_dato_int,procesar_dato_float
import datetime



class FrameCredito(FrameBusqueda):
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
  
        self.label_cuotas=tk.Label(self,text='Cuotas')
        self.label_cuotas.config(font=('Arial',12,'bold'))
        self.label_cuotas.grid(row=2,column=0,padx=10,pady=10)

        self.label_Productos=tk.Label(self,text='Productos')
        self.label_Productos.config(font=('Arial',12,'bold'))
        self.label_Productos.grid(row=3,column=0,padx=10,pady=10)

        self.label_monto_financiado=tk.Label(self,text='Monto financiado')
        self.label_monto_financiado.config(font=('Arial',12,'bold'))
        self.label_monto_financiado.grid(row=4,column=0,padx=10,pady=10)

        self.label_anticipo=tk.Label(self,text='Anticipo')
        self.label_anticipo.config(font=('Arial',12,'bold'))
        self.label_anticipo.grid(row=5,column=0,padx=10,pady=10)

        self.label_primera_cuota=tk.Label(self,text='Primera Cuota')
        self.label_primera_cuota.config(font=('Arial',12,'bold'))
        self.label_primera_cuota.grid(row=6,column=0,padx=10,pady=10)

        self.label_segunda_cuota=tk.Label(self,text='Segunda cuota')
        self.label_segunda_cuota.config(font=('Arial',12,'bold'))
        self.label_segunda_cuota.grid(row=7,column=0,padx=10,pady=10)


        self.label_nombre_garante=tk.Label(self,text='Nombre Garante')
        self.label_nombre_garante.config(font=('Arial',12,'bold'))
        self.label_nombre_garante.grid(row=8,column=0,padx=10,pady=10)

        self.label_telefono_garante=tk.Label(self,text='Telefono Garante')
        self.label_telefono_garante.config(font=('Arial',12,'bold'))
        self.label_telefono_garante.grid(row=9,column=0,padx=10,pady=10)

        self.label_direccion_garante=tk.Label(self,text='Direccion Garante')
        self.label_direccion_garante.config(font=('Arial',12,'bold'))
        self.label_direccion_garante.grid(row=10,column=0,padx=10,pady=10)

        self.label_mensaje_opciones_h=tk.Label(self,text='Presione h o H en  opciones para habilitar campos de credito nuevo',justify=tk.LEFT)
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
        self.entry_nombre_garante.grid(row=8,column=1,padx=10,pady=10,columnspan=2)

        self.mi_telefono_garante=tk.StringVar()
        self.entry_telefono_garante=tk.Entry(self,textvariable=self.mi_telefono_garante)
        self.entry_telefono_garante.config(width=50,font=('Arial',12))
        self.entry_telefono_garante.grid(row=9,column=1,padx=10,pady=10,columnspan=2)

        self.mi_direccion_garante=tk.StringVar()
        self.entry_direccion_garante=tk.Entry(self,textvariable=self.mi_direccion_garante)
        self.entry_direccion_garante.config(width=50,font=('Arial',12))
        self.entry_direccion_garante.grid(row=10,column=1,padx=10,pady=10,columnspan=2)

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
                    hoy= datetime.datetime.now()
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
                    mensaje=f"Generación de nuevo credito a cliente con nombre {nombre}, cuyo dni es {dni} por los productos de {credito_nuevo.producto} por total de monto financiado de {credito_nuevo.monto_financiado}, con un anticipo de {credito_nuevo.anticipo}, quedando a cuenta {acuenta}, en {credito_nuevo.cuotas} cuotas de {monto_cuota} con el primer vencimiento el día  {fecha_1} debe pagar la suma de {monto_cuota-acuenta} con garante {nombre_garante} cuyo telefono es {telefono_garante} y su direccion es {direccion_garante}"
                    respuesta = messagebox.askyesno(titulo, mensaje)
                    if respuesta:
                         carga_nueva_credito(credito_nuevo)
                         numero_credito=max_credito()
                         fechas_pagos=Fechas_Vencimiento(fechas[0],
                                          monto_cuota,
                                          "Por Pagar",
                                          numero_credito,
                                          acuenta,
                                          acuenta)
                         gravar_fechas(fechas_pagos)
                         for i in range(len(fechas)-1):
                                   fechas_pagos=Fechas_Vencimiento(fechas[i+1],
                                          monto_cuota,
                                          "Por Pagar",
                                          numero_credito,
                                          0.0,
                                          0.0)
                                   gravar_fechas(fechas_pagos)
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
    
    

'''

class FrameCreditoNuevo(FrameCredito):
        def __init__(self, parent):
            super().__init__(parent)
            

        def campos_garante(self):
        #label de campos
            

            #Entrys de cada Campo

            

            self._frame = None

        
                self.ventan_nueva=tk.Toplevel()
                mensaje_nombre="el cliente de nombre "+nombre
                
                mensaje_producto=" solicita un credito por el/los productos "+producto
                mensaje_monto_financiado=" con un monto financiado de  " + str(monto_financiado)
                mensaje_anticipo=" con anticipo de  "+str(anticipo)
                mensaje_cuotas=" en cuotas "+str(cuotas)
                
                


                label_1=tk.Label(self.ventan_nueva,text=mensaje_nombre)
                label_1.config(font=('Arial',12,'bold'))
                label_1.grid(row=0,column=0,padx=10,pady=10)

                label_2=tk.Label(self.ventan_nueva,text=mensaje_producto)
                label_2.config(font=('Arial',12,'bold'))
                label_2.grid(row=1,column=0,padx=10,pady=10)

                label_3=tk.Label(self.ventan_nueva,text=mensaje_monto_financiado)
                label_3.config(font=('Arial',12,'bold'))
                label_3.grid(row=2,column=0,padx=10,pady=10)

                label_4=tk.Label(self.ventan_nueva,text=mensaje_anticipo)
                label_4.config(font=('Arial',12,'bold'))
                label_4.grid(row=3,column=0,padx=10,pady=10)

                label_5=tk.Label(self.ventan_nueva,text=mensaje_cuotas)
                label_5.config(font=('Arial',12,'bold'))
                label_5.grid(row=4,column=0,padx=10,pady=10)

                
            
                label_10=label_id_nombre=tk.Label(self.ventan_nueva,text="¿Esta seguro que quiere generarlo?")
                label_10.config(font=('Arial',12,'bold'))
                label_10.grid(row=9,column=0,padx=10,pady=10)


                boton_crear=tk.Button(self.ventan_nueva,text="Crear credito",command=self.crear_credito)
                boton_crear.config(width=20,font=('Arial',12,'bold'),fg='#DAD5D6',bg='red',cursor='pirate',activebackground='#35BD6F')
                boton_crear.grid(row=10,column=0,padx=10,pady=10)

                boton_cancelar=tk.Button(self.ventan_nueva,text="cancelar",command=self.cancelar_generacion_credito)
                boton_cancelar.config(width=20,font=('Arial',12,'bold'),fg='#DAD5D6',bg='#158645',cursor='pirate',activebackground='#35BD6F')
                boton_cancelar.grid(row=10,column=1,padx=10,pady=10)
                
                self.desahabilitar_campos_nuevo_credito()
                self.habilitar_campos_nuevos_credito()
                  
             else:
                  titulo="Error al generar el credito"
                  mensaje= "No se encontro la cuenta" 
                  messagebox.showerror(titulo,mensaje)
                  #self.desahabilitar_campos_nuevo_credito()
        def crear_credito(self):
                carga_nueva_credito(self.Nuevo_credito)
                numero_credito=max_credito()
                dia_delta=datetime.timedelta(days=30)
                auxiliar= self.fecha_actual+dia_delta
                fecha_vencimiento=datetime.datetime.strftime(auxiliar,"%Y/%m/%d")
                fecha_primer_vencimiento=fecha_vencimiento
                fechas=Fechas_Vencimiento(self.Nuevo_credito.fecha,
                                          self.Nuevo_credito.monto_financiado/self.Nuevo_credito.cuotas,
                                          self.Nuevo_credito.monto_financiado/self.Nuevo_credito.cuotas,
                                          "Por Pagar",
                                          numero_credito,
                                          self.Nuevo_credito.anticipo,
                                          self.Nuevo_credito.anticipo)

                gravar_fechas(fechas)
                for i in range (self.Nuevo_credito.cuotas-1):
                    auxiliar= auxiliar+dia_delta
                    fecha_vencimiento=datetime.datetime.strftime(auxiliar,"%Y/%m/%d")
                    
                    fechas.fecha=fecha_vencimiento
                    gravar_fechas(fechas)
                    
                
                self.ventan_nueva.destroy()
                titulo="el credito se creo exitosamente"
                mensaje= "el número de credito es "+ str(numero_credito)+ " con vencimiento "+fecha_primer_vencimiento
                messagebox.showinfo(titulo,mensaje)

        def cancelar_generacion_credito(self):
             self.ventan_nueva.destroy()        '''