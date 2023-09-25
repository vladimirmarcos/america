from .conexion_db import ConexionDB
import sqlite3

def buscar(valor1,valor2):
    conexion=ConexionDB()
    sql=f""" SELECT dni,cuenta,nombre,contacto_direccion from cuentas WHERE {valor1} like '%{valor2}%'"""
    conexion.cursor.execute(sql)
    datos=conexion.cursor.fetchall()
    conexion.cerrar()
    return datos 
    

def verifica_dni(dni):
    conexion=ConexionDB()
    sql=f""" SELECT cuenta from cuentas WHERE dni={dni}"""   
    conexion.cursor.execute(sql)
    datos=conexion.cursor.fetchone()
    conexion.cerrar()
    return datos 

def max_cuenta():
    
    conexion=ConexionDB()
    sql=f""" SELECT max(cuenta+1) from cuentas"""   
    conexion.cursor.execute(sql)
    id_cuenta=conexion.cursor.fetchall()
    conexion.cerrar() 
    id_cuenta=list(id_cuenta[0])
    return id_cuenta[0]

def carga_nueva_cuenta(Cuenta):
    try:
        conexion=ConexionDB()
        sql=f"""INSERT INTO cuentas (cuenta,nombre,dni,contacto_telefono,contacto_direccion,direccion_trabajo,funcion)
        VALUES ('{Cuenta.numero_cuenta}','{Cuenta.nombre}','{Cuenta.dni}','{Cuenta.domicilio}','{Cuenta.telefono}','{Cuenta.domicilio_trabajo}','{Cuenta.funcion}')
    """   
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        print ("no se guardo")

def verifica_cuenta(cuenta):
    try:
        conexion=ConexionDB()
        sql=f""" SELECT cuenta from cuentas WHERE cuenta={cuenta}"""   
        conexion.cursor.execute(sql)
        datos=conexion.cursor.fetchone()
        conexion.cerrar()
        datos=list(datos)
        datos=datos[0]
        return datos
    except sqlite3.OperationalError:
        return "no se pudo abrir la base de datos intente más tarde"
    except TypeError:
        return None
    

def buscar_nombre(cuenta):
        conexion=ConexionDB()
        sql=f""" SELECT nombre,dni from cuentas WHERE cuenta={cuenta}"""   
        conexion.cursor.execute(sql)
        datos=conexion.cursor.fetchone()
        conexion.cerrar()
        datos=list(datos)
        return datos