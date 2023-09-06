def convertir_mes(mes):
        if mes==1:
            return "Enero"
        if mes==2:
            return "Febrero"
        if mes==3:
            return "Marzo"
        if mes==4:
            return "Abril"
        if mes==5:
            return "Mayo"
        if mes==6:
            return "Junio"
        if mes==7:
            return "Julio"
        if mes==8:
            return "Agosto"
        if mes==9:
            return "Septiembre"
        if mes==10:
            return "Octubre"
        if mes==11:
            return "Noviembre"
        if mes==12:
            return "Diciembre" 
        
def procesar_dato_str(dato):
        
            dato=dato.lower()
            dato=dato.strip()    
            dato=dato.title() 
            return dato 
      
def procesar_dato_int(dato):
     try:
        dato=int(dato)
        return dato
     except ValueError:
          return None
     
def procesar_dato_float(dato):
     try:
        dato=float(dato)
        return dato
     except ValueError:
          return None
