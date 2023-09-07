from .conexion_db import ConexionDB


def consulta_ordenes_Compra(organizacion):
    conexion=ConexionDB()
    sql=f""" SELECT pagare,{organizacion} FROM orden_compra """
    conexion.cursor.execute(sql)
    datos=conexion.cursor.fetchone()
    conexion.cerrar()
    return datos

