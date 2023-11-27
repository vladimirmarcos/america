import tkinter as tk
from tkinter import ttk
from windows.creacion_frame_cuentas import FrameCuentaNueva,FrameModificarCuenta
from windows.creacion_frame_creditos import FrameCreditoNuevo
from windows.creacion_frame_pagos import Framepago
from windows.creacion_frame_creditos_historicos import FrameCreditoHistoricos
from windows.creacion_frame_elimar_creditos import FrameEliminaCuenta
from windows.creacion_freme_pagos_historicos import FramepagoHistorico
from windows.creacion_frame_judiciales import FrameEnviarJudiciales
from windows.creacion_frame_actualizar_mora import FrameActualizarMora
#from windows.creacion_frame_ordenes_compras import FrameOrdenAmepp
class App(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.menu = tk.Menu(parent)
        
        
        self.menu_cuentas= tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Cuentas", menu=self.menu_cuentas)
        self.menu_cuentas.add_command(label="Crear Nueva Cuenta",command=self.cuenta_nueva_para_creditos)
        #self.menu_cuentas.add_command(label="Modificar Datos en cuentas",command=self.modificar_datos)
        parent.config(menu=self.menu)

        self.menu_creditos= tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Creditos", menu=self.menu_creditos)
        self.menu_creditos.add_command(label="Crear Nuevo Credito",command=self.crear_nuevo_credito)
        self.menu_creditos.add_command(label="Cargar Credito historico",command=self.crear_credito_historico)
        self.menu_creditos.add_command(label="Eliminar Credito",command=self.elimar_credito)
        
        #self.menu_creditos.add_command(label="Enviar a Judciales",command=self.enviar_judiciales)

        self.menu_pagos= tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Pagos", menu=self.menu_pagos)
        self.menu_pagos.add_command(label="Pago",command=self.generar_pago)
        self.menu_pagos.add_command(label="Pago Historico",command=self.generar_pago_historico)
        #self.menu_cuentas.add_command(label="Modificar Datos en cuentas",command=self.modificar_datos)

        self.configuracion= tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Configuracion", menu=self.configuracion)
        self.configuracion.add_command(label="Actualizar Mora",command=self.actualizar_mora)
        parent.config(menu=self.menu)


        self._frame = None
    def cuenta_nueva_para_creditos(self):
            if self._frame is not None:
               self._frame.borrar()
               self._frame = None
            if self._frame is None:
               self._frame = FrameCuentaNueva(self)

    def modificar_datos(self):
            if self._frame is not None:
               self._frame.borrar()
               self._frame = None
            if self._frame is None:
               self._frame = FrameModificarCuenta(self)

    def crear_nuevo_credito(self):
            if self._frame is not None:
               self._frame.borrar()
               self._frame = None
            if self._frame is None:
               self._frame = FrameCreditoNuevo(self)

    def crear_credito_historico(self):
            if self._frame is not None:
               self._frame.borrar()
               self._frame = None
            if self._frame is None:
               self._frame = FrameCreditoHistoricos(self)

    def generar_pago(self):
            if self._frame is not None:
               self._frame.borrar()
               self._frame = None
            if self._frame is None:
               self._frame = Framepago(self)
    
    def generar_pago_historico(self):
            if self._frame is not None:
               self._frame.borrar()
               self._frame = None
            if self._frame is None:
               self._frame = FramepagoHistorico(self)

    def elimar_credito(self):
            if self._frame is not None:
               self._frame.borrar()
               self._frame = None
            if self._frame is None:
               self._frame = FrameEliminaCuenta(self)

    def enviar_judiciales(self):
            if self._frame is not None:
               self._frame.borrar()
               self._frame = None
            if self._frame is None:
               self._frame = FrameEnviarJudiciales(self)

    def actualizar_mora(self):
            if self._frame is not None:
               self._frame.borrar()
               self._frame = None
            if self._frame is None:
               self._frame = FrameActualizarMora(self)
    
'''
        self.menu_ordenes_compra = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Ordenes de compra",menu=self.menu_ordenes_compra)
        self.menu_ordenes_compra.add_command(label="Crear orden de compra ADEPP",command="self.crear_orden_compra_amepp")
        self.menu_ordenes_compra.add_command(label="Crear orden de compra AMEPP",command=self.crear_orden_compra_amepp)
        parent.config(menu=self.menu)


        

'''
    


   