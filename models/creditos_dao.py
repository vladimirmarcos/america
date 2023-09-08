from .conexion_db import ConexionDB
import sqlite3


def busca_montos():
    conexion=ConexionDB() 
    sql=f"""SELECT valor FROM montos where valor>0"""
    conexion.cursor.execute(sql)
    id_credito=[]
    id_credito=conexion.cursor.fetchall()
    conexion.cerrar() 
    montos_meses=[]
    for i in range(len(id_credito)):
        montos_meses.append(id_credito[i][0])
    return montos_meses
