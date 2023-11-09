import sqlite3

class ConexionDB:

    def __init__(self):
        """Se conecta a la base de datos 
        """
        self.base_datos='creditos.db'
        self.conexion=sqlite3.connect(self.base_datos)
        self.cursor =self.conexion.cursor()
        

    def cerrar(self):
        """Cierra la conexión de base de datos
        """
        self.conexion.commit()
        self.conexion.close()




