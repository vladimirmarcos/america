class Afiliados:
     def __init__(self,nombre,dni,domicilio,mail,telefono,condicion):
        self.afiliado_id=None
        self.nombre=nombre
        self.dni=dni
        self.domicilio=domicilio
        self.mail=mail
        self.telefono=telefono
        self.condicion=condicion   
     def __str__(self):
        return f'Creditos[{self.nombre},{self.dni},{self.domicilio},{self.mail},{self.telefono},{self.condicion}]'
     

class OrdenCompra:
     def __init__(self,id_usuario,importe,dinero,porcentaje,cuota,mes,dias,comercio,orden_compra,pagare,estado):
        self.afiliado_id=None
        self.id_usuario=id_usuario
        self.importe=importe
        self.dinero=dinero
        self.porcentaje=porcentaje
        self.cuota=cuota
        self.mes=mes
        self.dias=dias
        self.comercio=comercio
        self.orden_compra=orden_compra
        self.pagare=pagare
        self.estado=estado    
     def __str__(self):
        return f'Creditos[{self.id_usuario},{self.importe},{self.dinero},{self.porcentaje},{self.cuota},{self.mes},{self.dias},{self.comercio},{self.orden_compra},{self.pagare},{self.estado}]'