from .conexion_db import ConexionDB
import sqlite3
import datetime
def carga_nueva_credito(Cuenta):
    
        conexion=ConexionDB()
        sql=f"""INSERT INTO creditos (cuenta,cuotas,producto,monto_financiado,anticipo,fecha,estado,calificacion)
        VALUES ('{Cuenta.cuenta}','{Cuenta.cuotas}','{Cuenta.producto}','{Cuenta.monto_financiado}','{Cuenta.anticipo}','{Cuenta.fecha}','{Cuenta.estado}','{Cuenta.calificacion}')
    """   
        conexion.cursor.execute(sql)
        conexion.cerrar()
    
        

def buscar_credito(credito):
    try:
        conexion=ConexionDB()
        sql=f""" SELECT credito from creditos where credito={credito}"""   
        conexion.cursor.execute(sql)
        id_cuenta=conexion.cursor.fetchall()
        conexion.cerrar() 
        
        id_cuenta=list(id_cuenta[0])
        valor=id_cuenta[0]
        return valor
    except:
         return None

def max_credito():
    
    conexion=ConexionDB()
    sql=f""" SELECT max(credito) from creditos"""   
    conexion.cursor.execute(sql)
    id_cuenta=conexion.cursor.fetchall()
    conexion.cerrar() 
    id_cuenta=list(id_cuenta[0])
    return id_cuenta[0]

def total_credito(cuenta):
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
    conexion=ConexionDB()
    sql=f"""INSERT INTO fechas_pagos (fecha,monto,estado,credito,a_cuenta,pagado)
        VALUES ('{Fechas_Vencimiento.fecha}','{Fechas_Vencimiento.monto}','{Fechas_Vencimiento.estado}','{Fechas_Vencimiento.credito}','{Fechas_Vencimiento.a_cuenta}',{Fechas_Vencimiento.pagado})
    
        """
    conexion.cursor.execute(sql)
    conexion.cerrar() 


def buscar_credito(credito):
     conexion=ConexionDB()
     sql=f""" SELECT credito,cuotas,producto from creditos where credito={credito}"""   
     conexion.cursor.execute(sql)
     credito_encontrado=conexion.cursor.fetchone()
     conexion.cerrar()
     try: 
        credito_encontrado=list(credito_encontrado)
        return credito_encontrado
     except:
          return None
     
def buscar_faltante_pagar(credito):
     conexion=ConexionDB()
     sql=f"SELECT fecha,monto,pagado from fechas_pagos where credito={credito} and estado='Por Pagar'"
     conexion.cursor.execute(sql)
     resto_pagar=conexion.cursor.fetchall()
     conexion.cerrar()
     j=0
     for i in resto_pagar:
          resto_pagar[j]=list(resto_pagar[j])
          j=j+1
     return resto_pagar

def eliminar_credito(credito):
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