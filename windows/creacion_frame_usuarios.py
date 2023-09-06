import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Procesamiento import procesar_dato_str,procesar_dato_int
from models.afiliados_dao import buscar_dni,cargar_afiliado
from models.models import Afiliados
  
class FrameUser(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
                
    def campos_datos_usuario(self):
        #label de campos
        self.label_nombre=tk.Label(self,text='Nombre')
        self.label_nombre.config(font=('Arial',12,'bold'))
        self.label_nombre.grid(row=0,column=0,padx=10,pady=10)

        self.label_dni=tk.Label(self,text='DNI')
        self.label_dni.config(font=('Arial',12,'bold'))
        self.label_dni.grid(row=1,column=0,padx=10,pady=10)

        self.label_domicilio=tk.Label(self,text='Domicilio')
        self.label_domicilio.config(font=('Arial',12,'bold'))
        self.label_domicilio.grid(row=2,column=0,padx=10,pady=10)

        self.label_telefono=tk.Label(self,text='Teléfono')
        self.label_telefono.config(font=('Arial',12,'bold'))
        self.label_telefono.grid(row=3,column=0,padx=10,pady=10)  

        
        self.label_mail=tk.Label(self,text='Mail')
        self.label_mail.config(font=('Arial',12,'bold'))
        self.label_mail.grid(row=4,column=0,padx=10,pady=10)


        self.label_condicion=tk.Label(self,text='Condicion')
        self.label_condicion.config(font=('Arial',12,'bold'))
        self.label_condicion.grid(row=5,column=0,padx=10,pady=10)


        #Entrys de cada Campo

        self.mi_nombre=tk.StringVar()
        self.entry_nombre=tk.Entry(self,textvariable=self.mi_nombre)
        self.entry_nombre.config(width=50,font=('Arial',12))
        self.entry_nombre.grid(row=0,column=1,padx=10,pady=10,columnspan=2)

        self.mi_dni=tk.StringVar()
        self.entry_dni=tk.Entry(self,textvariable=self.mi_dni)
        self.entry_dni.config(width=50,font=('Arial',12))
        self.entry_dni.grid(row=1,column=1,padx=10,pady=10,columnspan=2)

        self.mi_domicilio=tk.StringVar()
        self.entry_domicilio=tk.Entry(self,textvariable=self.mi_domicilio)
        self.entry_domicilio.config(width=50,font=('Arial',12))
        self.entry_domicilio.grid(row=2,column=1,padx=10,pady=10,columnspan=2)


        self.mi_telefono=tk.StringVar()
        self.entry_telefono=tk.Entry(self,textvariable=self.mi_telefono)
        self.entry_telefono.config(width=50,font=('Arial',12))
        self.entry_telefono.grid(row=3,column=1,padx=10,pady=10,columnspan=2)


        self.mi_mail=tk.StringVar()
        self.entry_mail=tk.Entry(self,textvariable=self.mi_mail)
        self.entry_mail.config(width=50,font=('Arial',12))
        self.entry_mail.grid(row=4,column=1,padx=10,pady=10,columnspan=2)

        
        self.mi_condicion=ttk.Combobox(self,
                                      state="readonly",
                                      values=["Directo", "Adherente"])
        self.mi_condicion.config(width=50, height=200,font=('Arial',12))
        self.mi_condicion.grid(row=5,column=1,padx=10,pady=10,columnspan=2) 

   
        self._frame = None
        
    def borrar(self):
        self.pack_forget()
        self.destroy()

class FrameUserAmepp(FrameUser):
      def __init__(self,parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=tk.YES)
        self.campos_datos_usuario()
        self.botones()
        self.desahabilitar_campos()

      
      def botones(self):
            self.boton_nuevo=tk.Button(self,text="Nuevo afiliado AMEPP",command=self.habilitar_campos)
            self.boton_nuevo.config(width=20,font=('Arial',12,'bold'),fg='#DAD5D6',bg='#158645',cursor='pirate',activebackground='#35BD6F')
            self.boton_nuevo.grid(row=6,column=0,padx=10,pady=10)

            self.boton_generar=tk.Button(self,text="Generar",command=self.verificar_dato)
            self.boton_generar.config(width=20,font=('Arial',12,'bold'),fg='#DAD5D6',bg='#BD152E',cursor='pirate',activebackground='#E15370')
            self.boton_generar.grid(row=6,column=1,padx=10,pady=10)
          
          
            self._frame = None

      def habilitar_campos(self):
        self.entry_nombre.config(state='normal')
        self.entry_dni.config(state='normal')
        self.entry_domicilio.config(state='normal')
        self.entry_telefono.config(state='normal')
        self.entry_mail.config(state='normal')
        self.mi_condicion.config(state='normal')
        self.boton_generar.config(state='normal')

      def desahabilitar_campos(self):
        self.mi_nombre.set('')
        self.mi_dni.set('')
        self.mi_domicilio.set('')
        self.mi_telefono.set('')
        self.mi_mail.set('')
        
       
        self.entry_nombre.config(state='disabled')
        self.entry_dni.config(state='disabled')
        self.entry_domicilio.config(state='disabled')
        self.entry_telefono.config(state='disabled')
        self.entry_mail.config(state='disabled')
        self.mi_condicion.config(state='disabled')
      
      def verificar_dato(self):
         
          dni=procesar_dato_int(self.mi_dni.get())
          if dni:
              verificado=buscar_dni("afiliado_amep",dni)
              if verificado:
                  titulo=" error al registrar el usuario"
                  mensaje= "el dni ya esta registrado" 
                  messagebox.showerror(titulo,mensaje)
              else: 
                   nombre=procesar_dato_str(self.mi_nombre.get())
                   domicilio=procesar_dato_str(self.mi_domicilio.get())
                   condicion=procesar_dato_str(self.mi_condicion.get())
                   mail=self.mi_telefono.get()
                   telefono=self.mi_telefono.get()
                   if nombre=="" or condicion=="":
                       titulo=" error al registrar el usuario"
                       mensaje= "EL nombre y la condición deben ser completados" 
                       messagebox.showerror(titulo,mensaje)
                   else: 
                         afiliado_amepp=Afiliados(
                             nombre,
                             dni,
                             domicilio,
                             mail,
                             telefono,
                             condicion

                         )
                         cargar_afiliado("afiliado_amep",afiliado_amepp)
                         titulo="Se cargo exitosamente "
                         mensaje= "el Afiliado en Amep se cargo exitosamente" 
                         messagebox.showinfo(titulo,mensaje)

                       
          else:
              titulo=" error al registrar el usuario"
              mensaje= "El dato ingresado como dni no es válido" 
              messagebox.showerror(titulo,mensaje)
          self.desahabilitar_campos()
          
class FrameUserAdepp(FrameUser):
     def __init__(self,parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=tk.YES)
        self.campos_datos_usuario()
        self.botones()
        self.desahabilitar_campos()
    
     def botones(self):
            self.boton_nuevo=tk.Button(self,text="Nuevo afiliado ADEP",command=self.habilitar_campos)
            self.boton_nuevo.config(width=20,font=('Arial',12,'bold'),fg='#DAD5D6',bg='#158645',cursor='pirate',activebackground='#35BD6F')
            self.boton_nuevo.grid(row=6,column=0,padx=10,pady=10)

            self.boton_generar=tk.Button(self,text="Generar",command=self.verificar_dato)
            self.boton_generar.config(width=20,font=('Arial',12,'bold'),fg='#DAD5D6',bg='#BD152E',cursor='pirate',activebackground='#E15370')
            self.boton_generar.grid(row=6,column=1,padx=10,pady=10)
          
          
            self._frame = None

     def habilitar_campos(self):
        self.entry_nombre.config(state='normal')
        self.entry_dni.config(state='normal')
        self.entry_domicilio.config(state='normal')
        self.entry_telefono.config(state='normal')
        self.entry_mail.config(state='normal')
        self.mi_condicion.config(state='normal')
        self.boton_generar.config(state='normal')

     def desahabilitar_campos(self):
        self.mi_nombre.set('')
        self.mi_dni.set('')
        self.mi_domicilio.set('')
        self.mi_telefono.set('')
        self.mi_mail.set('')
        
       
        self.entry_nombre.config(state='disabled')
        self.entry_dni.config(state='disabled')
        self.entry_domicilio.config(state='disabled')
        self.entry_telefono.config(state='disabled')
        self.entry_mail.config(state='disabled')
        self.mi_condicion.config(state='disabled')


     def verificar_dato(self):
         
          dni=procesar_dato_int(self.mi_dni.get())
          if dni:
              verificado=buscar_dni("afiliado_adep",dni)
              if verificado:
                  titulo=" error al registrar el usuario"
                  mensaje= "el dni ya esta registrado" 
                  messagebox.showerror(titulo,mensaje)
              else: 
                   nombre=procesar_dato_str(self.mi_nombre.get())
                   domicilio=procesar_dato_str(self.mi_domicilio.get())
                   condicion=procesar_dato_str(self.mi_condicion.get())
                   mail=self.mi_telefono.get()
                   telefono=self.mi_telefono.get()
                   if nombre=="" or condicion=="":
                       titulo=" error al registrar el usuario"
                       mensaje= "EL nombre y la condición deben ser completados" 
                       messagebox.showerror(titulo,mensaje)
                   else: 
                         afiliado_adepp=Afiliados(
                             nombre,
                             dni,
                             domicilio,
                             mail,
                             telefono,
                             condicion

                         )
                         cargar_afiliado("afiliado_adep",afiliado_adepp)
                         titulo="Se cargo exitosamente "
                         mensaje= "el Afiliado en Adepp se cargo exitosamente" 
                         messagebox.showinfo(titulo,mensaje)

                       
          else:
              titulo=" error al registrar el usuario"
              mensaje= "El dato ingresado como dni no es válido" 
              messagebox.showerror(titulo,mensaje)
          self.desahabilitar_campos()   