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
    
        



def max_credito():
    
    conexion=ConexionDB()
    sql=f""" SELECT max(credito) from creditos"""   
    conexion.cursor.execute(sql)
    id_cuenta=conexion.cursor.fetchall()
    conexion.cerrar() 
    id_cuenta=list(id_cuenta[0])
    return id_cuenta[0]


def gravar_fechas(Fechas_Vencimiento):
    conexion=ConexionDB()
    sql=f"""INSERT INTO fechas_pagos (fecha,monto_base,intereses,total,estado,credito,a_cuenta)
        VALUES ('{Fechas_Vencimiento.fecha}','{Fechas_Vencimiento.monto_base}','{Fechas_Vencimiento.intereses}','{Fechas_Vencimiento.total}','{Fechas_Vencimiento.estado}','{Fechas_Vencimiento.credito}','{Fechas_Vencimiento.a_cuenta}')
    
        """
    conexion.cursor.execute(sql)
    conexion.cerrar() 


