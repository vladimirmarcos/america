from .conexion_db import ConexionDB
from docxtpl import DocxTemplate
import os
import math
import Procesamiento
from Procesamiento import convertir_mes,procesar_dato_int

def buscar_moratoria():
    """Busca el porcentaje de moratoria de ese momento

    Returns:
        float: porcentaje de moratoria
    """    """"""
    
    conexion=ConexionDB()
    sql=f""" SELECT moratoria from mora"""   
    conexion.cursor.execute(sql)
    moratoria=conexion.cursor.fetchall()
    conexion.cerrar() 
    moratoria=list(moratoria)
    moratoria=list(moratoria[0])
    moratoria=moratoria[0]
    return moratoria

def buscar_informacion_cuota(credito):
    """busca información de cuenta 

    Args:
        credito (integrer): número de credito

    Returns:
        devuelve información de cuotas  
    """    """"""
    conexion=ConexionDB()
    sql=f"""SELECT  fecha_id,monto,fecha from fechas_pagos where credito={credito} and pagado=0 and estado='Por Pagar' """
    conexion.cursor.execute(sql)
    informacion=conexion.cursor.fetchone()
    conexion.cerrar() 
    informacion=list(informacion)
    return informacion

def buscar_primera_cuota (credito):
    """busca la primera cuota que se debe pagar el total del credito (sin nada a cuenta)

    Args:
        credito (integrer): número de credito

    Returns:
        _type_: número de cuota
    """    """"""
    conexion=ConexionDB()
    sql=f"""SELECT  fecha_id,total,cuota,fecha,monto,intereses from fechas_pagos where credito={credito} and acuenta=0 and estado='Por Pagar'"""
    conexion.cursor.execute(sql)
    informacion=conexion.cursor.fetchone()
    conexion.cerrar() 
    informacion=list(informacion)
    return informacion

def buscar_cuota (credito,cuota):
    """busca la primera cuota a pagar sin nada a cuenta  y la cuota

    Args:
        credito (integrer): número de credito
        cuota (integrer): número de cuota

    Returns:
        lista con fecha_id,total,cuota,fecha,monto,intereses 
    """    """"""
    try:
        conexion=ConexionDB()
        sql=f"""SELECT  fecha_id,total,cuota,fecha,monto,intereses from fechas_pagos where credito={credito} and acuenta=0 and cuota={cuota} and estado='Por Pagar'"""
        conexion.cursor.execute(sql)
        informacion=conexion.cursor.fetchone()
        conexion.cerrar() 
        informacion=list(informacion)
        return informacion
    except:
        return None
    
def genera_comprobante_mes(total,cuota,credito,hoy,fecha,monto,moratoria,nombre,dni,cuenta,bandera=1):
     """genera comprobante para pago de mes

    Args:
        total (_type_): _description_
        cuota (_type_): _description_
        credito (_type_): _description_
        hoy (_type_): _description_
        fecha (_type_): _description_
        monto (_type_): _description_
        moratoria (_type_): _description_
        nombre (_type_): _description_
        dni (_type_): _description_
        cuenta (_type_): _description_
    """
    
     modelo_blanco = DocxTemplate("PagoMes.docx")
     hoy=procesar_dato_fecha(hoy)
     partes_fecha = hoy.split("-")
     if moratoria>0:
          intereses=(moratoria-1)*monto
     else:
          intereses=0.0
     mes=convertir_mes(procesar_dato_int(partes_fecha[1]))
     context={
         'dia':partes_fecha[2],
          'mes':mes,
          'ano':partes_fecha[0],
         'nombre':nombre,
          'dni': dni,
          'cuenta':cuenta,
         'monto_cuotas':monto,
         'cuota':cuota,
         'credito':credito,
         'intereses':math.ceil(intereses),
         'fecha':fecha,
         'total':math.ceil(total)
     }
     modelo_blanco.render(context)
     archivo="pagosmes/"+"Recibo-"+nombre+str(credito)+"-"+str(hoy)+"-"+str(cuota)+".doc"
     modelo_blanco.render(context)
     modelo_blanco.save(archivo)
     nombre="Recibo-"+nombre+str(credito)+"-"+str(hoy)+"-"+str(cuota)+".doc"
     nombre=os.path.join( 'pagosmes', nombre)
     if bandera == 1:
        os.startfile(nombre,"print")
     
def gravar_pago(Pagos):
        """escribe el pago del cliente en la tabla pagos

    Args:
        Pagos (Objeto): contiene fecha del pago, monto pagado, el número de credito y el número de cuenta asociado
        """        
        conexion=ConexionDB()
        sql=f"""INSERT INTO pagos (fecha_pago,monto_pagado,credito,cuenta,cuota_anterior,a_cuenta,estado)
        VALUES ('{Pagos.fecha}','{Pagos.monto}','{Pagos.credito}','{Pagos.cuenta}','{Pagos.cuotaanterior}','{Pagos.acuentaanterior}','{Pagos.estado}')
    """   
        conexion.cursor.execute(sql)
        conexion.cerrar()
        
def  actualizo_credito(id_fecha):
          """actualizada fecha de pago

    Args:
        id_fecha (id): _description_
    """          """"""
          conexion=ConexionDB()
          sql=f"""  update fechas_pagos set estado='Pagado' WHERE fecha_id={id_fecha}
    """
          conexion.cursor.execute(sql)
          conexion.cerrar()

def buscar_resto(credito):
        """_busca la cantidad de dinero que le falta para terminar el credito_

    Args:
        credito (integrer):número de credito
        hoy (_type_): fecha de hoy
        

    Returns:
        _type_: total para culminar la dueda
        """        
        conexion=ConexionDB()
        sql=f"""SELECT  total,acuenta,fecha from fechas_pagos where credito={credito} and estado='Por Pagar'"""
        conexion.cursor.execute(sql)
        informacion=conexion.cursor.fetchall()
        conexion.cerrar() 
        t=0
        informacion=list(informacion)
        
        for i in informacion:
             informacion[t]=list(i)
             t=t+1
        total=0.0
        for i in informacion:
             
                total=total+(i[0]-i[1])
             
        
        return total

def actualizo_intereses_pagos(moratoria_base,moratoria,credito,hoy):
     """_actualizo los intereses en caso de que coloque otro monto de mora _

    Args:
        moratoria_base (_type_): _description_
        moratoria (_type_): _description_
        credito (_type_): _description_
        hoy (_type_): _description_
    """     """"""
     if moratoria_base!=moratoria:
          conexion=ConexionDB()
          sql=f"""SELECT  fecha_id,monto from fechas_pagos where credito={credito} and estado='Por Pagar' """
          conexion.cursor.execute(sql)
          informacion=conexion.cursor.fetchall()
          conexion.cerrar()
          informacion=list(informacion)
          t=0
          for i in informacion:
            informacion[t]=list(i)
            t=t+1
          t=0
          conexion=ConexionDB()
          for i in informacion:
               sql=f"""  update fechas_pagos set intereses={(moratoria-1)*100},total={informacion[t][1]*moratoria} WHERE fecha_id={informacion[t][0]}
    """        
               conexion.cursor.execute(sql)
               t=t+1
          conexion.cerrar() 
               

def genera_comprobante_acuenta(credito,acuenta,moratoria_base,moratoria,fecha_hoy):
     """genera información para generar comprobante a cuenta

    Args:
        credito (_type_): _description_
        acuenta (_type_): _description_
    """     """"""
     actualizo_intereses_pagos(moratoria_base,moratoria,credito,fecha_hoy)
     conexion=ConexionDB()
     sql=f"""SELECT  fecha_id,total,acuenta,cuota,fecha,credito,intereses from fechas_pagos where credito={credito} and estado='Por Pagar'"""
     conexion.cursor.execute(sql)
     informacion=conexion.cursor.fetchall()
     conexion.cerrar() 
     informacion=list(informacion)
     informacion_recibo=[]
     auxiliar=[]
     resta=1
     t=0
     for i in informacion:
          informacion[t]=list(i)
          t=t+1
     t=0
     while resta>0 and t<=len(informacion) :
     
        id_fecha=informacion[t][0]
        total=informacion[t][1]
        acuenta_cuota=informacion[t][2]
        cuota=informacion[t][3]
        resta=acuenta-(total-acuenta_cuota)
        fecha=procesar_dato_fecha(informacion[t][4])
        credito=informacion[t][5]
        intereses=informacion[t][6]
      
        conexion=ConexionDB()
        if resta>0:
          
          auxiliar.append(cuota)
          auxiliar.append("P")
          auxiliar.append(total-acuenta_cuota)
          auxiliar.append(fecha)
          auxiliar.append(credito)
          auxiliar.append(total)
          auxiliar.append(acuenta_cuota)
          informacion_recibo.append(auxiliar)
         
          sql=f"""  update fechas_pagos set estado='Pagado',acuenta={total} WHERE fecha_id={id_fecha}
    """
          conexion.cursor.execute(sql)
          auxiliar=[]
          acuenta=resta
        
        elif resta==0:
    
          auxiliar.append(cuota)
          auxiliar.append("P")
          auxiliar.append(total-acuenta_cuota)
          auxiliar.append(fecha)
          auxiliar.append(credito)
          auxiliar.append(total)
          auxiliar.append(acuenta_cuota)
          informacion_recibo.append(auxiliar)
          
         
          sql=f"""  update fechas_pagos set estado='Pagado',acuenta={total} WHERE fecha_id={id_fecha}
    """
          conexion.cursor.execute(sql)
          auxiliar=[]
          acuenta=resta
        else:
          
          auxiliar.append(cuota)
          auxiliar.append("A")
          auxiliar.append(acuenta)
          auxiliar.append(fecha)
          auxiliar.append(credito)
          auxiliar.append(abs(resta))
          informacion_recibo.append(auxiliar)
          acuenta=acuenta+acuenta_cuota
          sql=f"""  update fechas_pagos set acuenta={acuenta} WHERE fecha_id={id_fecha}
    """
          conexion.cursor.execute(sql)
         
          auxiliar=[]
          acuenta=resta
        t=t+1
        conexion.cerrar() 
     return informacion_recibo

def procesar_dato_fecha(dato):
     proximo_vencimiento=list(dato)
     proximo_vencimiento.insert(4,"-")
     proximo_vencimiento.insert(7,"-")
     proximo_vencimiento = ''.join(map(str, proximo_vencimiento))
     return proximo_vencimiento

def genera_recibo_acuenta(informacion,nombre,cuenta,hoy,acuenta,dni,credito,moratoria):
     """genera e imprime comprobante de pagos a cuenta

    Args:
        informacion (_type_): _description_
        nombre (_type_): _description_
        cuenta (_type_): _description_
        hoy (_type_): _description_
        acuenta (_type_): _description_
        dni (_type_): _description_
        credito (_type_): _description_
        moratoria (_type_): _description_
    """
     modelo_blanco = DocxTemplate("PagoAcuenta.docx")
     hoy=procesar_dato_fecha(hoy)
     partes_fecha = hoy.split("-")
     mes=convertir_mes(procesar_dato_int(partes_fecha[1]))
     context={
          'información':informacion,
          'hoy':partes_fecha[2],
           'mes':mes,
           'ano':partes_fecha[0],
         'nombre':nombre,
          'dni': dni,
          'cuenta':cuenta,
         'total':acuenta,
         'intereses':moratoria
     }
     modelo_blanco.render(context)
     archivo="pagosmes/"+"Recibo-"+nombre+str(credito)+"-"+str(hoy)+"-Por-monto-"+str(acuenta)+".doc"
     modelo_blanco.render(context)
     modelo_blanco.save(archivo)
     nombre="Recibo-"+nombre+str(credito)+"-"+str(hoy)+"-Por-monto-"+str(acuenta)+".doc"
     nombre=os.path.join( 'pagosmes', nombre)
     os.startfile(nombre,"print")


def actualizar_interes_meses(fecha_id,intereses,total):
      conexion=ConexionDB()
      sql=f"""  update fechas_pagos set intereses={intereses},total={total} WHERE fecha_id={fecha_id}"""
      conexion.cursor.execute(sql)
      conexion.cerrar()