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