import tkinter as tk
from models.cuentas_dao import buscar
from tkinter import messagebox
import sqlite3
from models.pagos_dao import buscar_moratoria

class FrameActualizarMora(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=tk.YES)
        
        self.habilitar_opciones()
        
    def campos_busquedas(self):
       #busqueda nombre 
        self.moratoria_base=buscar_moratoria()
        self.label_opciones=tk.Label(self,text='Opciones')
        self.label_opciones.config(font=('Arial',12,'bold'))
        self.label_opciones.grid(row=0,column=1,pady=10)

        self.label_nuevo_valor_mora=tk.Label(self,text='Nuevo valor de Mora')
        self.label_nuevo_valor_mora.config(font=('Arial',12,'bold'))
        self.label_nuevo_valor_mora.grid(row=1,column=0,pady=10)

        self.mi_opciones=tk.StringVar()
        self.entry_opciones=tk.Entry(self,textvariable=self.mi_opciones)
        self.entry_opciones.config(width=40,font=('Arial',12))
        self.entry_opciones.grid(row=0,column=2,pady=10,columnspan=2)
        self.entry_opciones.bind ("<Key>",self.verifica_tecla)

        self.mi_busqueda_nombre=tk.StringVar()
        self.entry_busqueda_nombre=tk.Entry(self,textvariable=self.mi_busqueda_nombre)
        self.entry_busqueda_nombre.config(width=50,font=('Arial',12))
        self.entry_busqueda_nombre.grid(row=15,column=2,pady=10,columnspan=2)
        self.entry_busqueda_nombre.bind ("<Return>",self.busqueda_nombre)

        self.label_mensaje_busqueda_b=tk.Label(self,text='Presione b o B en  opciones para habilitar busqueda por nombre',justify=tk.LEFT)
        self.label_mensaje_busqueda_b.config(font=('Arial',12,'bold'))
        self.label_mensaje_busqueda_b.grid(row=50,column=0)
        
        self._frame = None
        
    def desahabilitar_busqueda_nombre(self):
            self.mi_busqueda_nombre.set('')
            self.entry_busqueda_nombre.config(state='disabled')
            self.habilitar_opciones()

    def verifica_tecla(self,event):
         self.variable=event.char
         if self.variable=='b' or self.variable=='B':
              self.habilitar_busqueda_nombre()

    def habilitar_busqueda_nombre(self):
          self.entry_busqueda_nombre.config(state='normal')
          self.entry_busqueda_nombre.focus()       

    def habilitar_opciones(self):
         self.mi_opciones.set('')
         self.entry_opciones.config(state='disabled')
         self.entry_opciones.config(state='normal')
         self.entry_opciones.focus()

    def busqueda_nombre(self,event):
         nombre=self.mi_busqueda_nombre.get()
         if nombre !="":
                try:
                        auxiliar=buscar ("nombre",nombre)
                        if auxiliar:
                                lista=[list(x) for x in auxiliar]
                                titulo=f" Usuarios con nombre {nombre}"
                                mensaje= "\n"
                                for i in lista:
                                         mensaje=mensaje+ str(i[2])+ " dni "+ str(i[0])+" domicilio "+ str(i[3])+ " N cuenta "+str(i[1])+" \n"
                                messagebox.showinfo(titulo,mensaje)
                                self.desahabilitar_busqueda_nombre()
                                
                        else: 
                                titulo="No se encontro nombre"
                                mensaje= f"el nombre {nombre} no tiene asociada ninguna cuenta" 
                                messagebox.showerror(titulo,mensaje)
                                                           
                except sqlite3.OperationalError:
                       titulo="No se ingresar a la base de datos"
                       mensaje= "La base de datos esta siendo ocupada o esta dañada, intente más tarde" 
                       messagebox.showerror(titulo,mensaje)
                                       
         else:
              titulo="No ingreso nombre"
              mensaje= "Se envio el campo vacío" 
              messagebox.showerror(titulo,mensaje)
              
    def borrar(self):
          self.pack_forget()
          self.destroy()