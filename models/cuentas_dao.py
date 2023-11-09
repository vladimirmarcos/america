from .conexion_db import ConexionDB
import sqlite3

def buscar(valor1,valor2):
    """funcion, busca cuenta con nombres parecesido al string ingresado en la base de datos

    Args:
        valor1 (_type_): _description_
        valor2 (_type_): _description_

    Returns:
        _type_: Lista de nombre encontrados en la base de datos
    """    
    conexion=ConexionDB()
    sql=f""" SELECT dni,cuenta,nombre,contacto_direccion from cuentas WHERE {valor1} like '%{valor2}%'"""
    conexion.cursor.execute(sql)
    datos=conexion.cursor.fetchall()
    conexion.cerrar()
    return datos 
   
def verifica_dni(dni):
    """Busca dni en base de datos

    Args:
        dni (integrer): dni 

    Returns:
        _type_: retorna dni en caso de existir o none en caso de no
    """    
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
    """ Carga nueva cuenta en la base de datos

    Args:
        Cuenta (objeto):  debe poseer número cuenta,nombre,dni,contacto telefono y direccion
    """    """"""
    try:
        conexion=ConexionDB()
        sql=f"""INSERT INTO cuentas (cuenta,nombre,dni,contacto_telefono,contacto_direccion,direccion_trabajo,funcion)
        VALUES ('{Cuenta.numero_cuenta}','{Cuenta.nombre}','{Cuenta.dni}','{Cuenta.domicilio}','{Cuenta.telefono}','{Cuenta.domicilio_trabajo}','{Cuenta.funcion}')
    """   
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
           pass

def verifica_cuenta(cuenta):
    """verifica que la cuenta exista en la cuenta en la base de datos

    Args:
        cuenta (integrer): número de cuenta

    Returns:
        _type_: devuelve el número de cuenta, en caso de que no exista devuelve none
    """    """"""
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
        """Busca informacion asociada a la cuenta ingresada

        Args:
        cuenta (integer): número de cuenta

    Returns:
        _type_: regresa una lista con el nombre y dni asociados a la cuenta ingresado
        """        """"""
        conexion=ConexionDB()
        sql=f""" SELECT nombre,dni from cuentas WHERE cuenta={cuenta}"""   
        conexion.cursor.execute(sql)
        datos=conexion.cursor.fetchone()
        conexion.cerrar()
        datos=list(datos)
        return datos