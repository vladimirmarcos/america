class Cuenta:
     def __init__(self,numero_cuenta,nombre,dni,telefono,domicilio):
        self.cuenta_id=None
        self.numero_cuenta=numero_cuenta
        self.nombre=nombre
        self.dni=dni
        self.telefono=telefono
        self.domicilio=domicilio  
     def __str__(self):
        return f'Cuenta[{self.numero_cuenta},{self.nombre},{self.dni},{self.telefono},{self.domicilio}]'
     
class Creditos:
     def __init__(self,cuenta,cuotas,productos,monto_financiado,monto_credito,fecha,estado,calificacion):
        self.credito=None
        self.cuenta=cuenta
        self.cuotas=cuotas
        self.productos=productos
        self.monto_financiado=monto_financiado
        self.monto_credito=monto_credito
        self.fecha=fecha
        self.estado=estado
        self.calificacion=calificacion
        
     def __str__(self):
        return f'Creditos[{self.cuenta},{self.cuotas},{self.productos},{self.monto_financiado},{self.monto_credito},{self.fecha},{self.estado},{self.calificacion}]'