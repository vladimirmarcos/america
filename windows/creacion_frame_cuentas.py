import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Procesamiento import procesar_dato_int,procesar_dato_str,procesar_dato_float
from windows.creacion_frame_busquedas import FrameBusqueda

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


    

        self.boton_habilita_nombre=tk.Button(self,text="Habilitar busqueda por Nombre",command="self.habilita_busqueda_nombre")
        self.boton_habilita_nombre.config(width=25,font=('Arial',12,'bold'),fg='#DAD5D6',bg='#158645',cursor='pirate',activebackground='#35BD6F')
        self.boton_habilita_nombre.grid(row=9,column=2,padx=10,pady=10)
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
        
        
        


