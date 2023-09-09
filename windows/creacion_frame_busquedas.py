import tkinter as tk
from tkinter import ttk,END
import re 
from Procesamiento import procesar_dato_int,procesar_dato_str,procesar_dato_float
from models.cuentas_dao import buscar
from tkinter import messagebox
import sqlite3

class FrameBusqueda(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.campos_busquedas()
        self.desahabilitar_busqueda_nombre()
        self.habilitar_busqueda_nombre()
        

    def campos_busquedas(self):
       #busqueda nombre 

        self.label_busqueda_nombre=tk.Label(self,text='Busqueda por nombre')
        self.label_busqueda_nombre.config(font=('Arial',12,'bold'))
        self.label_busqueda_nombre.grid(row=10,column=2,padx=10,pady=10)

        self.mi_busqueda_nombre=tk.StringVar()
        self.entry_busqueda_nombre=tk.Entry(self,textvariable=self.mi_busqueda_nombre)
        self.entry_busqueda_nombre.config(width=50,font=('Arial',12))
        self.entry_busqueda_nombre.grid(row=10,column=3,padx=10,pady=10,columnspan=2)
        self.entry_busqueda_nombre.bind ("<Return>",self.busqueda_nombre)
        
        self._frame = None


        
    
    
            
    def desahabilitar_busqueda_nombre(self):
            self.mi_busqueda_nombre.set('')
            self.entry_busqueda_nombre.config(state='disabled')

    def habilitar_busqueda_nombre(self):
          self.entry_busqueda_nombre.config(state='normal')       
            
    def busqueda_nombre(self,event):
         nombre=self.mi_busqueda_nombre.get()
         if nombre !="":
                try:
                        auxiliar=buscar ("nombre",nombre)
                        if auxiliar:
                                lista=[list(x) for x in auxiliar]
                                titulo=f" Usuarios con nombre {nombre}"
                                mensaje= f"algunos usarios asociados al nombre {nombre} ingresado son \n"
                                for i in lista:
                                         mensaje=mensaje+"usuario con nombre "+ str(i[2])+ " dni "+ str(i[0])+" vivi en "+ str(i[3])+ "   tiene asociado la cuenta "+str(i[1])+" \n"
                                messagebox.showinfo(titulo,mensaje)
                                self.desahabilitar_busqueda_nombre()
                                self.habilitar_busqueda_nombre()
                        else: 
                                titulo="No se encontro nombre"
                                mensaje= f"el nombre {nombre} no tiene asociada ninguna cuenta" 
                                messagebox.showerror(titulo,mensaje)
                                self.desahabilitar_busqueda_nombre()
                                self.habilitar_busqueda_nombre()
                except sqlite3.OperationalError:
                       titulo="No se ingresar a la base de datos"
                       mensaje= "La base de datos esta siendo ocupada o esta dañada, intente más tarde" 
                       messagebox.showerror(titulo,mensaje)
                       self.desahabilitar_busqueda_nombre()
                       self.habilitar_busqueda_nombre()
                       
         else:
              titulo="No ingreso nombre"
              mensaje= "Se envio el campo vacío" 
              messagebox.showerror(titulo,mensaje)
              self.desahabilitar_busqueda_nombre() 
    def borrar(self):
        self.pack_forget()
        self.destroy()