import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Procesamiento import procesar_dato_int,procesar_dato_fecha,procesar_dato_float,procesar_dato_str,procesar_cuota
from windows.creacion_frame_busquedas import FrameBusqueda 
from models.models import Pagos
from models.cuentas_dao import buscar_nombre
from models.pagos_dao import buscar_moratoria,genera_comprobante_mes,buscar_resto
from models.creditos_dao import total_credito,buscar_credito,buscar_historia_credito,finalizar_credito
from models.pagos_dao import buscar_primera_cuota,buscar_cuota, actualizo_credito,gravar_pago,genera_comprobante_acuenta,genera_recibo_acuenta,actualizar_interes_meses
import datetime


class Framepago(FrameBusqueda):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=tk.YES)
        self.campos_pagos()
        self.desahabilitar_pagos_creditos()
        self.desahabilitar_busqueda_creditos()
        self.desahabilitar_pagos_creditos()
        self.desahabilitar_busqueda_nombre()
        self.desahabilitar_datos_pagos()
      
    def campos_pagos(self):
        #label de campos
        self.moratoria_base=buscar_moratoria()

        self.label_numero_credito=tk.Label(self,text='Numero Credito')
        self.label_numero_credito.config(font=('Arial',12,'bold'))
        self.label_numero_credito.grid(row=1,column=0,padx=10,pady=10)

        self.label_moratoria=tk.Label(self,text='Moratoria actual es de '+str(self.moratoria_base))
        self.label_moratoria.config(font=('Arial',12,'bold'))
        self.label_moratoria.grid(row=2,column=0,padx=10,pady=10)

        self.label_cuotas=tk.Label(self,text='Cuota')
        self.label_cuotas.config(font=('Arial',12,'bold'))
        self.label_cuotas.grid(row=3,column=0,padx=10,pady=10)

        self.label_acuenta=tk.Label(self,text='A cuenta')
        self.label_acuenta.config(font=('Arial',12,'bold'))
        self.label_acuenta.grid(row=5,column=0,padx=10,pady=10)
  
        self.label_busca_credito=tk.Label(self,text="Buscar creditos de cuenta")
        self.label_busca_credito.config(font=('Arial',12,'bold'))
        self.label_busca_credito.grid(row=6,column=1,padx=10,pady=10)

        #Entrys de cada Campo

        self.mi_numero_credito=tk.StringVar()
        self.entry_numero_credito=tk.Entry(self,textvariable=self.mi_numero_credito)
        self.entry_numero_credito.config(width=50,font=('Arial',12))
        self.entry_numero_credito.grid(row=1,column=1,padx=10,pady=10,columnspan=2)

        self.mi_moratoria=tk.StringVar()
        self.entry_moratoria=tk.Entry(self,textvariable=self.mi_moratoria)
        self.entry_moratoria.config(width=50,font=('Arial',12))
        self.entry_moratoria.grid(row=2,column=1,padx=10,pady=10,columnspan=2)

        self.mi_cuotas=tk.StringVar()
        self.entry_cuotas=tk.Entry(self,textvariable=self.mi_cuotas)
        self.entry_cuotas.config(width=50,font=('Arial',12))
        self.entry_cuotas.grid(row=3,column=1,padx=10,pady=10,columnspan=2)

        self.mi_acuenta=tk.StringVar()
        self.entry_acuenta=tk.Entry(self,textvariable=self.mi_acuenta)
        self.entry_acuenta.config(width=50,font=('Arial',12))
        self.entry_acuenta.grid(row=5,column=1,padx=10,pady=10,columnspan=2)

        self.mi_busca_credito=tk.StringVar()
        self.entry_busca_credito=tk.Entry(self,textvariable=self.mi_busca_credito)
        self.entry_busca_credito.config(width=50,font=('Arial',12))
        self.entry_busca_credito.grid(row=6,column=2,padx=10,pady=10,columnspan=2)

        self.label_mensaje_busqueda_c=tk.Label(self,text='Presione c o c en  opciones para habilitar busqueda de creditos',justify=tk.LEFT)
        self.label_mensaje_busqueda_c.config(font=('Arial',12,'bold'))
        self.label_mensaje_busqueda_c.grid(row=51,column=0)

        self.entry_numero_credito.bind ("<Return>",self.genera_pago)
        
        self.entry_moratoria.bind ("<Return>",self.genera_pago)
        self.entry_acuenta.bind ("<Return>",self.genera_pago_acuenta)
        self.entry_cuotas.bind ("<Return>",self.genera_pago_meses)
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
              self.mi_opciones.set('')
              self.entry_numero_credito.config(state='disabled')
              self.entry_opciones.focus()

    def desahabilitar_datos_pagos(self):
         
         self.mi_cuotas.set('')
         self.mi_acuenta.set('')
         self.mi_moratoria.set('')
         self.entry_moratoria.config(state='disabled')
         self.entry_cuotas.config(state='disabled')
         self.entry_acuenta.config(state='disabled')

    def habilitar_datos_pagos(self):
         self.entry_moratoria.config(state='normal')
         self.entry_cuotas.config(state='normal')
         self.entry_acuenta.config(state='normal')    
         self.entry_moratoria.focus()

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
                self.desahabilitar_busqueda_creditos()
        
        else:
            titulo=" Error al buscar historial"
            mensaje="El dato ingresado como número de cuenta no es valido"
            messagebox.showerror(titulo,mensaje) 

    def genera_pago(self,event):     
        self.credito=procesar_dato_int(self.mi_numero_credito.get())
        self.hoy= datetime.datetime.today()
        self.hoy=datetime.datetime.strftime(self.hoy,'%Y%m%d')
        if self.credito:
            credito_encontado=buscar_credito(self.credito)   
            if credito_encontado:
                   datos=buscar_historia_credito(self.credito)
                   datos_persona=buscar_nombre(credito_encontado[3])
                   self.cuenta=credito_encontado[3]
                   self.nombre=datos_persona[0]
                   self.dni=datos_persona[1]
                   j=12
                   t=0
                   
                   for i in datos:
                     if (i[4]=='Pagado'):
                         fecha=procesar_dato_fecha(i[0])
                         mensaje=f"Cuota {t+1} fecha vencimiento {fecha} Monto {i[1]} estado pagado"
                         self.label_fechas=tk.Label(self,text=mensaje)
                         self.label_fechas.config(font=('Arial',12,'bold'))
                         self.label_fechas.grid(row=j,column=0)
                         j=j+1
                         t=t+1
                     else:
                         fecha=procesar_dato_fecha(i[0])
                         mensaje=f"""Cuota {t+1} fecha vencimiento {fecha} monto {i[1]} a cuenta {i[2]}"""
                         self.label_fechas=tk.Label(self,text=mensaje)
                         self.label_fechas.config(font=('Arial',12,'bold'))
                         self.label_fechas.grid(row=j,column=0)
                         j=j+1
                         t=t+1
                   self.habilitar_datos_pagos() 
                   
                 
            else:
                titulo=" Error al generar el pago"
                mensaje="El dato ingresado como número de credito no existe, ya fue dado de baja o finalizado"
                messagebox.showerror(titulo,mensaje)     
        else:
            titulo=" Error al generar el pago"
            mensaje="El dato ingresado como número de credito o el de moratoria no es valido"
            messagebox.showerror(titulo,mensaje) 
    
    def genera_pago_meses(self,event):
         self.moratoria=self.mi_moratoria.get()
         if self.moratoria=="":
             self.moratoria=self.moratoria_base
             self.moratoria=(self.moratoria/100)+1
         else:
              self.moratoria=procesar_dato_float(self.moratoria)
              try:
                self.moratoria=(self.moratoria/100)+1
              except TypeError:
                   self.moratoria=False
         if self.moratoria:
              self.moratoria_base=(self.moratoria_base/100)+1
              cuota=procesar_cuota(self.mi_cuotas.get())
              if cuota:
                if cuota=='p' or cuota =='P':
                             proxima_cuota=buscar_primera_cuota(self.credito)
                             id_fecha=proxima_cuota[0]
                             fecha=proxima_cuota[3]
                             if self.hoy >fecha or self.moratoria!=self.moratoria_base:
                                       total=proxima_cuota[4]*self.moratoria
                                       
                             else:
                                       total=proxima_cuota[4]
                                       self.moratoria=0.0                                       
                            
                             cuota=proxima_cuota[2]
                             
                             monto=proxima_cuota[4]
                             fecha=procesar_dato_fecha(fecha)
                             self.hoystr=procesar_dato_fecha(self.hoy)
                             titulo="Pago de cuota"
                             mensaje= f"""¿Esta seguro de emitir el pago al cliente {self.nombre}, por el monto total de la cuota {total}, cuyo monto base es de {monto} con fecha de vencimiento {fecha} a la fecha {self.hoystr} ?"""
                             respuesta = messagebox.askyesno(titulo, mensaje)
                             if respuesta:
                              if self.moratoria!=self.moratoria_base:
                                   actualizar_interes_meses(id_fecha,(self.moratoria-1)*100,total)
                              genera_comprobante_mes(total,cuota,self.credito,self.hoy,fecha,monto,self.moratoria,self.nombre,self.dni,self.cuenta)
                              actualizo_credito(id_fecha)
                              pagos=Pagos(self.hoy,
                                         total,
                                         self.credito,
                                         self.cuenta,
                                         id_fecha,
                                         0.0)
                              gravar_pago(pagos)
                              self.desahabilitar_datos_pagos()
                              self.desahabilitar_pagos_creditos()
                              restante=buscar_resto(self.credito)
                              if restante==0:
                                   finalizar_credito(self.credito)
                                   finalizar_credito(self.credito)
                                   titulo=" Finalizo el credito"
                                   mensaje="el Credito fue finalizado "
                                   messagebox.showinfo(titulo,mensaje)                           
                elif cuota:
                             cuota_pagar=buscar_cuota(self.credito,cuota)
                             if cuota_pagar:
                                   id_fecha=cuota_pagar[0]
                                   fecha=cuota_pagar[3]
                                   if self.hoy >fecha or self.moratoria!=self.moratoria_base:
                                            total=cuota_pagar[4]*self.moratoria
                                            print(self.moratoria)
                                            
                                   else:
                                            total=cuota_pagar[1]
                                            self.moratoria=0.0                                       
                                
                                   cuota=cuota_pagar[2]                        
                                   monto=cuota_pagar[4]
                                   fecha=procesar_dato_fecha(fecha)
                                   self.hoystr=procesar_dato_fecha(self.hoy)
                                   self.nombre=procesar_dato_str(self.nombre)
                                   titulo="Pago de cuota"
                                   mensaje= f"""¿Esta seguro de emitir el pago al cliente {self.nombre}, por el monto total de la cuota {total}, cuyo monto base es de {monto} con fecha de vencimiento {fecha} a la fecha {self.hoystr}?"""
                                   respuesta = messagebox.askyesno(titulo, mensaje)
                                   if respuesta:
                                        if self.moratoria!=self.moratoria_base:
                                         actualizar_interes_meses(id_fecha,(self.moratoria-1)*100,total)
                                        genera_comprobante_mes(total,cuota,self.credito,self.hoy,fecha,  monto,self.moratoria,self.nombre,self.dni,self.cuenta)
                                        actualizo_credito(id_fecha)
                                        pagos=Pagos(self.hoy,
                                         total,
                                         self.credito,
                                         self.cuenta,
                                         id_fecha,
                                         0.0)
                                        gravar_pago(pagos)
                                        self.desahabilitar_datos_pagos()
                                        self.desahabilitar_pagos_creditos()
                                        restante=buscar_resto(self.credito)
                                        if restante==0:
                                            finalizar_credito(self.credito)
                                            finalizar_credito(self.credito)
                                            titulo=" Finalizo el credito"
                                            mensaje="el Credito fue finalizado "
                                            messagebox.showinfo(titulo,mensaje)   
                             else:
                                  titulo=" Error al generar el pago"
                                  mensaje="El dato cuota no exite en el credito o ya fue pagada "
                                  messagebox.showerror(titulo,mensaje)              
              else:
                titulo=" Error al generar el pago"
                mensaje="El dato ingresado como cuota es invalido"
                messagebox.showerror(titulo,mensaje)
         else:
                titulo=" Error al generar el pago"
                mensaje="El dato ingresado como moratoria es invalido"
                messagebox.showerror(titulo,mensaje)

    def genera_pago_acuenta(self,event):
         self.moratoria=self.mi_moratoria.get()
         if self.moratoria=="":
             self.moratoria=self.moratoria_base
             self.moratoria=(self.moratoria/100)+1
         else:
              try:
                    self.moratoria=procesar_dato_float(self.moratoria)
                    self.moratoria=(self.moratoria/100)+1
                    
              except TypeError:
                   self.moratoria=False
         if self.moratoria:       
            acuenta=procesar_dato_float(self.mi_acuenta.get())
            if acuenta:
              resto_pagar=buscar_resto(self.credito)
              if acuenta<=resto_pagar:
                   titulo="Emitir Pago"
                   mensaje= f"""¿Esta seguro de emitir un pago por {acuenta} al cliente {self.nombre} con dni {self.dni} por el credito número {self.credito}?"""
                   respuesta = messagebox.askyesno(titulo, mensaje)
                   if respuesta:
                    
                    informacion_recibo=genera_comprobante_acuenta(self.credito,acuenta,self.moratoria_base,self.moratoria,self.hoy)
                    genera_recibo_acuenta(informacion_recibo,self.nombre,self.cuenta,self.hoy,acuenta,self.dni,self.credito,self.moratoria)
                    pagos=Pagos(self.hoy,
                                         acuenta,
                                         self.credito,
                                         self.cuenta,
                                         informacion_recibo[0][0],
                                         acuenta)
                    gravar_pago(pagos)
                    self.desahabilitar_datos_pagos()
                    self.desahabilitar_pagos_creditos() 
                    restante=buscar_resto(self.credito)
                    if restante==0:
                        finalizar_credito(self.credito)
                        titulo=" Finalizo el credito"
                        mensaje="el Credito fue finalizado "
                        messagebox.showinfo(titulo,mensaje) 
              else:
                    titulo=" Error al generar el pago"
                    mensaje="El dato ingresado como a cuenta es mayor al total del resto de credito por pagar"
                    messagebox.showerror(titulo,mensaje)       
            else:
              titulo=" Error al generar el pago"
              mensaje="El dato ingresado como a cuenta no es valido"
              messagebox.showerror(titulo,mensaje)

         else:
              titulo=" Error con el dato de Mora"
              mensaje="el dato ingresado como moratoria es incorrecto "
              messagebox.showerror(titulo,mensaje) 
              
        
      
    
