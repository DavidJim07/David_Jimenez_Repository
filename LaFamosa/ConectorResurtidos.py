import mysql.connector
from datetime import *
import bd

class TablaResurtidos(object):
    def __init__(self,baseDatos,usuario,clave):
        self.host="localhost"
        self.database=baseDatos
        self.user=usuario
        self.password=clave
        self.port="3306"
        self.con=self.hacerConexion()
        self.myCursor=self.con.cursor()

    def hacerConexion(self): 
        try:
            return mysql.connector.connect(host="localhost", user="root", password="lobito200", port="3306", database="lafamosa")
        except :
            print("Fallo al conectar a mysql")

    def ejecutar(self, sentenciaSQL, opCrud):
        self.myCursor.execute(sentenciaSQL)
        if opCrud=="buscar":
            return self.myCursor.fetchone()
        if opCrud=="listar":
           return self.myCursor.fetchall()
        if opCrud=="eliminar":
           pass
        if opCrud=="llamar":
            return self.myCursor.callproc()
        #self.con.commit()

    def cerrarConeccion(self):
        if self.con:self.con.close()

    def cantidadSubResurtidosProcedure(self):
        self.myCursor.callproc('sp_mostrarCantidadResurtidos')
        for result in self.myCursor.stored_results():
            return result.fetchall()

    def listarResurtidosProcedure(self):
        self.myCursor.callproc('sp_mostrarResurtidos')
        resurtidos=[]
        for result in self.myCursor.stored_results():
            for dato in result.fetchall():
                resurtir=bd.Resurtir()
                b=0
                for at in dato:
                    if b==0:
                        resurtir.setClaveRes(at)
                    elif b==1:
                        resurtir.setFechaRes(at)
                    elif b==2:
                        resurtir.setTotalRes(at)
                    elif b==3:
                        resurtir.setClaveProv(at)
                    elif b==4:
                        resurtir.setClaveTie(at)
                    b+=1
                resurtidos.append(resurtir)
        return resurtidos