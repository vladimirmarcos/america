
from .conexion_db import ConexionDB
import sqlite3
import datetime

def buscar_moratoria():
    
    conexion=ConexionDB()
    sql=f""" SELECT moratoria from mora"""   
    conexion.cursor.execute(sql)
    id_cuenta=conexion.cursor.fetchall()
    conexion.cerrar() 
    id_cuenta=list(id_cuenta[0])
    return id_cuenta[0]

def buscar_informacion_cuota(credito):
    conexion=ConexionDB()
    sql=f"""SELECT  fecha_id,monto,fecha from fechas_pagos where credito={credito} and pagado=0 and estado='Por Pagar' """
    conexion.cursor.execute(sql)
    informacion=conexion.cursor.fetchone()
    conexion.cerrar() 
    informacion=list(informacion)
    return informacion