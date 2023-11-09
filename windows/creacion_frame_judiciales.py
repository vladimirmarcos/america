import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Procesamiento import procesar_dato_int,procesar_dato_fecha
from windows.creacion_frame_busquedas import FrameBusqueda
from models.creditos_dao import total_credito,buscar_credito,eliminar_credito
from models.pagos_dao import buscar_moratoria,buscar_resto
from models.cuentas_dao import buscar_nombre
import datetime

class FrameEnviarJudiciales(FrameBusqueda):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=tk.YES)
        self.campos_busquedas()
        self.campos_enviar_judiciales()
        self.desahabilitar_campos_elimar_credito()
        self.desahabilitar_busqueda_nombre()
        self.desahabilitar_busqueda_creditos()
        


    def campos_enviar_judiciales(self):
        #label de campos
        self.label_numero_credito=tk.Label(self,text='Numero Credito')
        self.label_numero_credito.config(font=('Arial',12,'bold'))
        self.label_numero_credito.grid(row=1,column=0,padx=10,pady=10)

        self.label_busca_credito=tk.Label(self,text="Buscar creditos de cuenta")
        self.label_busca_credito.config(font=('Arial',12,'bold'))
        self.label_busca_credito.grid(row=4,column=1,padx=10,pady=10)
        #Entrys de cada Campo

        self.mi_numero_credito=tk.StringVar()
        self.entry_numero_credito=tk.Entry(self,textvariable=self.mi_numero_credito)
        self.entry_numero_credito.config(width=50,font=('Arial',12))
        self.entry_numero_credito.grid(row=1,column=1,padx=10,pady=10,columnspan=2)

        self.mi_busca_credito=tk.StringVar()
        self.entry_busca_credito=tk.Entry(self,textvariable=self.mi_busca_credito)
        self.entry_busca_credito.config(width=50,font=('Arial',12))
        self.entry_busca_credito.grid(row=4,column=2,padx=10,pady=10,columnspan=2)

        self.entry_numero_credito.bind ("<Return>",self.elimar_credito)
        self.entry_busca_credito.bind ("<Return>",self.busca_informacion_creditos)

        self.label_mensaje_busqueda_b=tk.Label(self,text='Presione c o C en  opciones para habilitar busqueda Creditos',justify=tk.LEFT)
        self.label_mensaje_busqueda_b.config(font=('Arial',12,'bold'))
        self.label_mensaje_busqueda_b.grid(row=16,column=0)

        self.label_mensaje_busqueda_b=tk.Label(self,text='Presione h o H en  opciones para habilitar eliminación de credito',justify=tk.LEFT)
        self.label_mensaje_busqueda_b.config(font=('Arial',12,'bold'))
        self.label_mensaje_busqueda_b.grid(row=17,column=0)
        self._frame = None
 
    def verifica_tecla(self,event):
         
         super().verifica_tecla(event)
         if self.variable=='H' or self.variable=='h':
              self.habilitar_campos_elimar_credito()
         elif (self.variable=='C' or self.variable=='c'):
             self.habilitar_busqueda_creditos()
             
    def desahabilitar_busqueda_creditos(self):
        self.mi_busca_credito.set('')
        self.mi_opciones.set('')
        self.entry_busca_credito.config(state='disabled')    
        self.entry_opciones.focus()
    
    def habilitar_busqueda_creditos(self):
        self.entry_busca_credito.config(state='normal')
        self.entry_busca_credito.focus()

    def desahabilitar_campos_elimar_credito(self):
        self.mi_numero_credito.set('')
        self.mi_opciones.set('')
        self.entry_numero_credito.config(state='disabled')
        self.entry_opciones.focus()
                
    def habilitar_campos_elimar_credito(self):
        
        self.entry_numero_credito.config(state='normal')        
        self.entry_numero_credito.focus()   


    def elimar_credito(self,event):
        numero_credito=procesar_dato_int(self.mi_numero_credito.get())
        if numero_credito:
            credito_verificado=buscar_credito(numero_credito)
            if credito_verificado:
                moratoria_base=(buscar_moratoria()/100)+1
                hoy= datetime.datetime.today()
                hoy=datetime.datetime.strftime(hoy,'%Y%m%d')
                resto_pagar=buscar_resto(numero_credito)
                datos=buscar_nombre(credito_verificado[3])
                hoy_str=procesar_dato_fecha(hoy)
                titulo=f"Eliminacion de credito "
                mensaje=f"¿ Esta seguro de eliminar el credito {numero_credito}, con productos {credito_verificado[2]}, perteneciente al cliente {datos[0]} cuyo dni es {datos[1]}, teniendo un faltante a pagar en el día de hoy {hoy_str} de {resto_pagar} "
                respuesta = messagebox.askyesno(titulo, mensaje)   
                if respuesta:
                    eliminar_credito(numero_credito)
                    titulo=" Eliminacion de Creditos"
                    mensaje="El credito fue eliminado exitosamente"
                    messagebox.showinfo(titulo,mensaje)
                    self.desahabilitar_campos_elimar_credito()

                
            else:
                titulo=" Error al buscar el credito"
                mensaje="El credito ingresado no existe"
                messagebox.showerror(titulo,mensaje)

        else:
            titulo=" Error al buscar el credito"
            mensaje="El dato ingresado como número de credito no es valido"
            messagebox.showerror(titulo,mensaje)

    def busca_informacion_creditos(self,event):
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