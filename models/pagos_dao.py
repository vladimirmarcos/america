
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
    print (id_cuenta)
    return id_cuenta[0]