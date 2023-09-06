import tkinter as tk
from tkinter import ttk
from ttkwidgets import AutocompleteEntry
from Procesamiento import procesar_dato_int,procesar_dato_str,procesar_dato_float


class FrameBusqueda(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=tk.YES)
        self.campos_busquedas()
        self.desahabilitar_busqueda_dni()
        self.desahabilitar_busqueda_nombre()
        
    def campos_busquedas(self):
       #busqueda dni
        self.label_busqueda_dni=tk.Label(self,text='Busqueda Por DNI')
        self.label_busqueda_dni.config(font=('Arial',12,'bold'))
        self.label_busqueda_dni.grid(row=0,column=0,padx=10,pady=10)

        self.mi_busqueda_dni=tk.StringVar()
        self.entry_busqueda_dni=tk.Entry(self,textvariable=self.mi_busqueda_dni)
        self.entry_busqueda_dni.config(width=50,font=('Arial',12))
        self.entry_busqueda_dni.grid(row=0,column=1,padx=10,pady=10,columnspan=2)

        self.boton_habilita_dni=tk.Button(self,text="Habilitar busqueda por DNI",command=self.habilita_busqueda_dni)
        self.boton_habilita_dni.config(width=25,font=('Arial',12,'bold'),fg='#DAD5D6',bg='#158645',cursor='pirate',activebackground='#35BD6F')
        self.boton_habilita_dni.grid(row=1,column=3,padx=10,pady=10)

        self.entry_busqueda_dni.bind ("<Return>",self.busqueda_dni)

        #busqueda nombre

        self.label_busqueda_nombre=tk.Label(self,text='Busqueda por nombre')
        self.label_busqueda_nombre.config(font=('Arial',12,'bold'))
        self.label_busqueda_nombre.grid(row=2,column=0,padx=10,pady=10)

        self.mi_busqueda_nombre=tk.StringVar()
        self.entry_busqueda_nombre=tk.Entry(self,textvariable=self.mi_busqueda_nombre)
        self.entry_busqueda_nombre.config(width=50,font=('Arial',12))
        self.entry_busqueda_nombre.grid(row=2,column=1,padx=10,pady=10,columnspan=2)

        self.boton_habilita_nombre=tk.Button(self,text="Habilitar busqueda por Nombre",command=self.habilita_busqueda_nombre)
        self.boton_habilita_nombre.config(width=25,font=('Arial',12,'bold'),fg='#DAD5D6',bg='#158645',cursor='pirate',activebackground='#35BD6F')
        self.boton_habilita_nombre.grid(row=4,column=3,padx=10,pady=10)

        self.entry_busqueda_nombre.bind ("<Return>",self.busqueda_nombre)
        self._frame = None
    def habilita_busqueda_dni(self):
            self.entry_busqueda_dni.config(state='normal')
    def desahabilitar_busqueda_dni(self):
            self.mi_busqueda_dni.set('')
            self.entry_busqueda_dni.config(state='disabled')
            
    def busqueda_dni(self,event):
         dni=self.mi_busqueda_dni.get()
         print(dni)
         self.desahabilitar_busqueda_dni()
    def habilita_busqueda_nombre(self):
            self.entry_busqueda_nombre.config(state='normal')
    def desahabilitar_busqueda_nombre(self):
            self.mi_busqueda_nombre.set('')
            self.entry_busqueda_nombre.config(state='disabled')
            
    def busqueda_nombre(self,event):
         nombre=self.mi_busqueda_nombre.get()
         
         self.desahabilitar_busqueda_nombre()
    def borrar(self):
        self.pack_forget()
        self.destroy()