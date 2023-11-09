from .conexion_db import ConexionDB
def carga_nueva_credito(Cuenta):
        """_carga el credito en la base de datos_

    Args:
        Cuenta (objeto): _debe poseer número de cuenta, cuotas, producto, monto financiado, anticipo, la fecha de cracion, el estado y su calificacion_
    """        """
        """
    
        conexion=ConexionDB()
        sql=f"""INSERT INTO creditos (cuenta,cuotas,producto,monto_financiado,anticipo,fecha,estado,calificacion)
        VALUES ('{Cuenta.cuenta}','{Cuenta.cuotas}','{Cuenta.producto}','{Cuenta.monto_financiado}','{Cuenta.anticipo}','{Cuenta.fecha}','{Cuenta.estado}','{Cuenta.calificacion}')
    """   
        conexion.cursor.execute(sql)
        conexion.cerrar()
    
def buscar_credito(credito):
    """_busca el credito ingresado_

    Args:
        credito (_integrer_): _description_

    Returns:
        _integrer_: en caso de encontrar el credito devuelve su número, caso contrario, devuelve None
    """    """"""
    try:
        conexion=ConexionDB()
        sql=f""" SELECT credito from creditos where credito={credito}"""   
        conexion.cursor.execute(sql)
        id_cuenta=conexion.cursor.fetchone()
        conexion.cerrar() 
        
        id_cuenta=list(id_cuenta[0])
        valor=id_cuenta[0]
        return valor
    except:
         return None

def max_credito():
    """_devuelve el último número de credito_

    Returns:
        _integrer_: valor del último credito
    """    """"""
    
    conexion=ConexionDB()
    sql=f""" SELECT max(credito) from creditos"""   
    conexion.cursor.execute(sql)
    id_cuenta=conexion.cursor.fetchall()
    conexion.cerrar() 
    id_cuenta=list(id_cuenta[0])
    return id_cuenta[0]

def total_credito(cuenta):
            """Busca creditos de cuentas 

    Args:
        cuenta (integrer): _description_

    Returns:
        _type_: devuelve una lista con todos los creditos
            """            """"""
            conexion=ConexionDB()
            sql=f""" SELECT credito,cuotas,monto_financiado/cuotas,producto from creditos WHERE cuenta={cuenta}"""   
            conexion.cursor.execute(sql)
            id_cuenta=conexion.cursor.fetchall()
            conexion.cerrar()
            if id_cuenta: 
                id_cuenta=list(id_cuenta)
                for i in range(len(id_cuenta)):
                   id_cuenta[i]=list(id_cuenta[i])
                          
                return id_cuenta
            else:
                  None

def gravar_fechas(Fechas_Vencimiento):
    """carga en la vase de datos la fecha de vencimiento del pago de credito

    Args:
        Fechas_Vencimiento (objeto): debe poseer fecha, monto, intereses, total,estado, acuenta,credito y cuota
    """    """"""
    conexion=ConexionDB()
    sql=f"""INSERT INTO fechas_pagos (fecha,monto,intereses,total,estado,acuenta,credito,cuota)
        VALUES ('{Fechas_Vencimiento.fecha}','{Fechas_Vencimiento.monto}','{Fechas_Vencimiento.intereses}','{Fechas_Vencimiento.total}','{Fechas_Vencimiento.estado}','{Fechas_Vencimiento.acuenta}','{Fechas_Vencimiento.credito}','{Fechas_Vencimiento.cuota}')
    
        """
    conexion.cursor.execute(sql)
    conexion.cerrar() 

def buscar_credito(credito):
     """busca el credito asociado

    Args:
        credito (integrer): numero entero del credito
    Returns:
        lista: devuelve lista que contiene número de credito,cuotas,producto y cuenta 
     """     """"""
     conexion=ConexionDB()
     sql=f""" SELECT credito,cuotas,producto,cuenta from creditos where credito={credito} and estado=1"""   
     conexion.cursor.execute(sql)
     credito_encontrado=conexion.cursor.fetchone()
     conexion.cerrar()
     try: 
        credito_encontrado=list(credito_encontrado)
        return credito_encontrado
     except:
          return None
     
def buscar_historia_credito(credito):
     """Busca la historia del credito que se quiere pagar

    Args:
        credito (integrer): número de credito

    Returns:
        lista de lista: cada lista contiene fecha,total, acuenta intereses y estado
     """
     conexion=ConexionDB()
     sql=f"SELECT fecha,total,acuenta,intereses,estado from fechas_pagos where credito={credito}"
     conexion.cursor.execute(sql)
     resto_pagar=conexion.cursor.fetchall()
     conexion.cerrar()
    
     j=0
     for i in resto_pagar:
          resto_pagar[j]=list(resto_pagar[j])
          j=j+1
     return resto_pagar
     
def eliminar_credito(credito):
     """elimina el credito solicitado

    Args:
        credito (integrer)
    """     """"""
     conexion=ConexionDB()
     sql=f""" update creditos set estado=0 WHERE credito={credito}
    """
     conexion.cursor.execute(sql)
     conexion.cerrar()
     conexion=ConexionDB()
     sql=f""" update fechas_pagos set estado='Eliminado' WHERE credito={credito}
    """
     conexion.cursor.execute(sql)
     conexion.cerrar()

def finalizar_credito(credito):
     """Hace que un credito deje de estar activo

    Args:
        credito (integrer): _description_
    """     """"""
     conexion=ConexionDB()
     sql=f""" update creditos set estado=0 WHERE credito={credito}
    """
     conexion.cursor.execute(sql)
     conexion.cerrar()

def guardar_garante(Garantes):
        """guarda garante en la base de datos

    Args:
        Garantes (_type_): _description_
    """        """"""
        conexion=ConexionDB()
        sql=f"""INSERT INTO garantes (nombre,direccion,telefono,credito)
        VALUES ('{Garantes.nombre}','{Garantes.direccion}','{Garantes.telefono}','{Garantes.credito}')
    """   
        conexion.cursor.execute(sql)
        conexion.cerrar()

