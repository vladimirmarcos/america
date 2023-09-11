class Cuenta:
     def __init__(self,numero_cuenta,nombre,dni,telefono,domicilio,domicilio_trabajo,funcion):
        self.cuenta_id=None
        self.numero_cuenta=numero_cuenta
        self.nombre=nombre
        self.dni=dni
        self.telefono=telefono
        self.domicilio=domicilio
        self.domicilio_trabajo=domicilio_trabajo
        self.funcion=funcion 
     def __str__(self):
        return f'Cuenta[{self.numero_cuenta},{self.nombre},{self.dni},{self.telefono},{self.domicilio},,{self.domicilio_trabajo},{self.funcion}]'
     
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
    def __init__(self,fecha,monto_base,total,estado,credito,acuenta,pagado):
        self.id_fecha=None
        self.fecha=fecha
        self.monto_base=monto_base
        self.intereses=0.0
        self.total=total        
        self.estado=estado
        self.credito=credito
        self.a_cuenta=acuenta
        self.pagado=pagado
        
    def __str__(self):
        return f'Creditos[{self.fecha},{self.monto_base},{self.intereses},{self.total},{self.estado},{self.credito},{self.a_cuenta},{self.pagado}]'
