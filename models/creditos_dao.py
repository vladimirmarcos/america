from .conexion_db import ConexionDB
from tkinter import messagebox

def buscar(valor1,valor2):
    conexion=ConexionDB()
    sql=f""" SELECT dni,cuenta,nombre from cuentas WHERE {valor1} like '%{valor2}%'"""
    conexion.cursor.execute(sql)
    datos=conexion.cursor.fetchall()
    conexion.cerrar()
    return datos 
    

    