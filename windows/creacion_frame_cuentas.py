import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Procesamiento import procesar_dato_int,procesar_dato_str,procesar_dato_float
from windows.creacion_frame_busquedas import FrameBusqueda
from models.cuentas_dao import verifica_dni,max_cuenta,carga_nueva_cuenta
from models.models import Cuenta
import sqlite3

class FrameCuentaNueva(FrameBusqueda):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=tk.YES)
        self.campos_busquedas()
        self.campos_cuenta_nueva()
        self.desahabilitar_busqueda_dni()
        self.desahabilitar_busqueda_nombre()
        self.desahabilitar_campos_cuenta_nueva()


    def campos_cuenta_nueva(self):
        #label de campos
        self.label_nombre=tk.Label(self,text='Nombre')
        self.label_nombre.config(font=('Arial',12,'bold'))
        self.label_nombre.grid(row=5,column=0,padx=10,pady=10)

        self.label_dni=tk.Label(self,text='DNI')
        self.label_dni.config(font=('Arial',12,'bold'))
        self.label_dni.grid(row=6,column=0,padx=10,pady=10)

        self.label_telefono=tk.Label(self,text='Teléfono')
        self.label_telefono.config(font=('Arial',12,'bold'))
        self.label_telefono.grid(row=7,column=0,padx=10,pady=10)

        self.label_domicilio=tk.Label(self,text='Domicilio')
        self.label_domicilio.config(font=('Arial',12,'bold'))
        self.label_domicilio.grid(row=8,column=0,padx=10,pady=10)



        #Entrys de cada Campo

        self.mi_nombre=tk.StringVar()
        self.entry_nombre=tk.Entry(self,textvariable=self.mi_nombre)
        self.entry_nombre.config(width=50,font=('Arial',12))
        self.entry_nombre.grid(row=5,column=1,padx=10,pady=10,columnspan=2)

        self.mi_dni=tk.StringVar()
        self.entry_dni=tk.Entry(self,textvariable=self.mi_dni)
        self.entry_dni.config(width=50,font=('Arial',12))
        self.entry_dni.grid(row=6,column=1,padx=10,pady=10,columnspan=2)

        self.mi_telefono=tk.StringVar()
        self.entry_telefono=tk.Entry(self,textvariable=self.mi_telefono)
        self.entry_telefono.config(width=50,font=('Arial',12))
        self.entry_telefono.grid(row=7,column=1,padx=10,pady=10,columnspan=2)

        self.mi_domicilio=tk.StringVar()
        self.entry_domicilio=tk.Entry(self,textvariable=self.mi_domicilio)
        self.entry_domicilio.config(width=50,font=('Arial',12))
        self.entry_domicilio.grid(row=8,column=1,padx=10,pady=10,columnspan=2)


        self.boton_habilita_nombre=tk.Button(self,text="Habilitar Carga de datos",command=self.habilitar_campos_cuenta_nueva)
        self.boton_habilita_nombre.config(width=25,font=('Arial',12,'bold'),fg='#DAD5D6',bg='#158645',cursor='pirate',activebackground='#35BD6F')
        self.boton_habilita_nombre.grid(row=9,column=2,padx=10,pady=10)

        self.entry_nombre.bind ("<Return>",self.guradar_datos_cuenta_nueva)
        self.entry_dni.bind ("<Return>",self.guradar_datos_cuenta_nueva)
        self.entry_telefono.bind ("<Return>",self.guradar_datos_cuenta_nueva)
        self.entry_domicilio.bind ("<Return>",self.guradar_datos_cuenta_nueva)
        self._frame = None

    def desahabilitar_campos_cuenta_nueva(self):
        self.mi_nombre.set('')
        self.mi_dni.set('')
        self.mi_telefono.set('')
        self.mi_domicilio.set('')
        
        self.entry_nombre.config(state='disabled')
        self.entry_dni.config(state='disabled')
        self.entry_telefono.config(state='disabled')
        self.entry_domicilio.config(state='disabled')
        
    def habilitar_campos_cuenta_nueva(self):
        self.entry_nombre.config(state='normal')
        self.entry_dni.config(state='normal')
        self.entry_telefono.config(state='normal')
        self.entry_domicilio.config(state='normal')
        
    def  guradar_datos_cuenta_nueva(self,event):
        self.desahabilitar_busqueda_dni()
        self.desahabilitar_busqueda_nombre()
        nombre=self.mi_nombre.get()
        dni=self.mi_dni.get()
        telefono=self.mi_telefono.get()
        domicilio=self.mi_domicilio.get()
        if nombre!="" and dni!="":
            dni=procesar_dato_int(dni)
            if dni:
                try:
                    dni_vericado=verifica_dni(dni)
                    
                    if dni_vericado==None:
                        
                            cuenta_numero=max_cuenta()
                            if telefono=="":
                                 telefono="no lo tenemos"
                            if domicilio=="":
                                 domicilio="no lo tenemos"
                            Cuenta_Nueva=Cuenta(cuenta_numero,
                                                nombre,
                                                dni,
                                                domicilio,
                                                telefono)
                            
                            carga_nueva_cuenta(Cuenta_Nueva)
                            titulo="Carga exitosa"
                            mensaje= f"el dni {dni} se cargo de manera exitosa" 
                            messagebox.showinfo(titulo,mensaje)
                            self.desahabilitar_campos_cuenta_nueva()
                          
                    
                    else:
                            cuenta=list (dni_vericado)
                            titulo="Error por dato ya existent"
                            mensaje= f"el dni {dni} ya esta registrado con la cuenta {cuenta[0]}" 
                            messagebox.showerror(titulo,mensaje)
                            #self.desahabilitar_campos_cuenta_nueva()
                except sqlite3.OperationalError:
                                titulo="No se ingresar a la base de datos"
                                mensaje= "La base de datos esta siendo ocupada o esta dañada, intente más tarde" 
                                messagebox.showerror(titulo,mensaje)
                                #self.desahabilitar_campos_cuenta_nueva()
      

            else:
                dni=self.mi_dni.get()
                titulo="Error por dato no valido"
                mensaje= f"el dato {dni} no es valido como dni" 
                messagebox.showerror(titulo,mensaje)
                #self.desahabilitar_campos_cuenta_nueva()
        else:
            titulo="Error por falta de datos importantes"
            mensaje= "Los campos de nombre, dni o ambos estan vacíos, no se puede cargar usuario sin ellos" 
            messagebox.showerror(titulo,mensaje)
            #self.desahabilitar_campos_cuenta_nueva()




class FrameModificarCuenta(FrameBusqueda):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=tk.YES)
        self.campos_busquedas()
        self.campos_nuevos_cuenta()
        self.desahabilitar_busqueda_dni()
        self.desahabilitar_busqueda_nombre()
        self.desahabilitar_campos_nuevos_cuenta()


    def campos_nuevos_cuenta(self):
        #label de campos
        self.label_nombre=tk.Label(self,text='Nombre')
        self.label_nombre.config(font=('Arial',12,'bold'))
        self.label_nombre.grid(row=5,column=0,padx=10,pady=10)

        self.label_dni=tk.Label(self,text='DNI')
        self.label_dni.config(font=('Arial',12,'bold'))
        self.label_dni.grid(row=6,column=0,padx=10,pady=10)

        self.label_telefono=tk.Label(self,text='Teléfono')
        self.label_telefono.config(font=('Arial',12,'bold'))
        self.label_telefono.grid(row=7,column=0,padx=10,pady=10)

        self.label_domicilio=tk.Label(self,text='Domicilio')
        self.label_domicilio.config(font=('Arial',12,'bold'))
        self.label_domicilio.grid(row=8,column=0,padx=10,pady=10)



        #Entrys de cada Campo

        self.mi_nombre=tk.StringVar()
        self.entry_nombre=tk.Entry(self,textvariable=self.mi_nombre)
        self.entry_nombre.config(width=50,font=('Arial',12))
        self.entry_nombre.grid(row=5,column=1,padx=10,pady=10,columnspan=2)

        self.mi_dni=tk.StringVar()
        self.entry_dni=tk.Entry(self,textvariable=self.mi_dni)
        self.entry_dni.config(width=50,font=('Arial',12))
        self.entry_dni.grid(row=6,column=1,padx=10,pady=10,columnspan=2)

        self.mi_telefono=tk.StringVar()
        self.entry_telefono=tk.Entry(self,textvariable=self.mi_telefono)
        self.entry_telefono.config(width=50,font=('Arial',12))
        self.entry_telefono.grid(row=7,column=1,padx=10,pady=10,columnspan=2)

        self.mi_domicilio=tk.StringVar()
        self.entry_domicilio=tk.Entry(self,textvariable=self.mi_domicilio)
        self.entry_domicilio.config(width=50,font=('Arial',12))
        self.entry_domicilio.grid(row=8,column=1,padx=10,pady=10,columnspan=2)


        self.boton_habilita_nombre=tk.Button(self,text="Habilitar Carga de datos",command=self.habilitar_campos_nuevos_cuenta)
        self.boton_habilita_nombre.config(width=25,font=('Arial',12,'bold'),fg='#DAD5D6',bg='#158645',cursor='pirate',activebackground='#35BD6F')
        self.boton_habilita_nombre.grid(row=9,column=2,padx=10,pady=10)

        self.entry_nombre.bind ("<Return>",self.datos_modificados)
        self.entry_dni.bind ("<Return>",self.datos_modificados)
        self.entry_telefono.bind ("<Return>",self.datos_modificados)
        self.entry_domicilio.bind ("<Return>",self.datos_modificados)
        self._frame = None

    def desahabilitar_campos_nuevos_cuenta(self):
        self.mi_nombre.set('')
        self.mi_dni.set('')
        self.mi_telefono.set('')
        self.mi_domicilio.set('')
        
        self.entry_nombre.config(state='disabled')
        self.entry_dni.config(state='disabled')
        self.entry_telefono.config(state='disabled')
        self.entry_domicilio.config(state='disabled')
        
    def habilitar_campos_nuevos_cuenta(self):
        self.entry_nombre.config(state='normal')
        self.entry_dni.config(state='normal')
        self.entry_telefono.config(state='normal')
        self.entry_domicilio.config(state='normal')

    def datos_modificados(self,event):
         nombre=self.mi_nombre.get()
         dni=self.mi_dni.get()
         telefono=self.mi_telefono.get()
         domicilio=self.mi_domicilio.get()
         if ((nombre=="") and (dni=="") and (telefono=="")and (domicilio=="")):
                titulo="Error"
                mensaje= "No se detecto que ingreso datos en ningun campo" 
                messagebox.showerror(titulo,mensaje)
                self.desahabilitar_campos_nuevos_cuenta()  
                return
         
         if (nombre!=""):
              self.dato_a_modificar(nombre,0)
         self.desahabilitar_campos_nuevos_cuenta()  
                
    def dato_a_modificar(self,dato,flag):
         if flag==0:
              pass