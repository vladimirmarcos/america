from .conexion_db import ConexionDB
from models.pagos_dao import buscar_moratoria
import sqlite3
import datetime

def actualizar_intereses():
    """actualiza los intereses  en caso de fecha vencida
    """    """"""
    hoy= datetime.datetime.now()
    hoy=datetime.datetime.strftime(hoy,'%Y%m%d')
    conexion=ConexionDB()
    sql=f""" SELECT fecha_id,intereses,total from fechas_pagos where fecha<{hoy} and intereses=0"""   
    conexion.cursor.execute(sql)
    datos=conexion.cursor.fetchall()
    conexion.cerrar()
    moratoria=buscar_moratoria()
    
    t=0
    conexion=ConexionDB()
    for i in datos:
        info=list(i)
        monto=info[2]
        total=monto+monto*(moratoria/100)
        
        sql=f""" update fechas_pagos set intereses={moratoria},total={total} WHERE fecha_id={info[0]}
    """
        conexion.cursor.execute(sql)
        t=t+1
    conexion.cerrar()

       
        
   

