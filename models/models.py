class Cuenta:
     def __init__(self,numero_cuenta,nombre,dni,telefono,domicilio,domiciliotrabajo,funcion):
        self.cuenta_id=None
        self.numero_cuenta=numero_cuenta
        self.nombre=nombre
        self.dni=dni
        self.telefono=telefono
        self.domicilio=domicilio
        self.domiciliotrabajo=domiciliotrabajo
        self.funcion=funcion 
     def __str__(self):
        return f'Cuenta[{self.numero_cuenta},{self.nombre},{self.dni},{self.telefono},{self.domicilio},{self.domiciliotrabajo},{self.funcion}]'
     
class Creditos:
     def __init__(self,cuenta,cuotas,productos,monto_financiado,anticipo,fecha,estado,calificacion):
        self.credito=None
        self.cuenta=cuenta
        self.cuotas=cuotas
        self.producto=productos
        self.monto_financiado=monto_financiado
        self.anticipo=anticipo
        self.fecha=fecha
        self.estado=estado
        self.calificacion=calificacion
        
     def __str__(self):
        return f'Creditos[{self.cuenta},{self.cuotas},{self.producto},{self.monto_financiado},{self.anticipo},{self.fecha},{self.estado},{self.calificacion}]'
     
class Fechas_Vencimiento:
    def __init__(self,fecha,monto,intereses,estado,credito,acuenta,cuota):
        self.id_fecha=None
        self.fecha=fecha
        self.monto=monto 
        self.intereses=intereses 
        self.total=monto+intereses*monto
        self.acuenta=acuenta      
        self.estado=estado
        self.credito=credito
        self.cuota=cuota
        
    def __str__(self):
        return f'Fechas_vencimiento[{self.fecha},{self.monto},{self.intereses},{self.total},{self.acuenta},{self.estado},{self.credito},{self.cuota}]'

class Pagos:
    def __init__(self,fecha,monto,credito,cuenta,cuotaanterior,acuentaanterior):
        self.id_pagos=None
        self.fecha=fecha
        self.monto=monto 
        self.credito=credito
        self.cuenta=cuenta
        self.cuotaanterior=cuotaanterior
        self.acuentaanterior=acuentaanterior
        self.estado=1
        
    def __str__(self):
        return f'Pagos[{self.fecha},{self.monto},{self.credito},{self.cuenta},{self.cuotaanterior},{self.acuentaanterior}]'
    



class Garantes:
    def __init__(self,nombre,direccion,telefono,credito):
        self.id_pagos=None
        self.nombre=nombre
        self.direccion=direccion
        self.telefono=telefono
        self.credito=credito
        
        
    def __str__(self):
        return f'Garante[{self.nombre},{self.direccion},{self.telefono},{self.credito}]'
    

