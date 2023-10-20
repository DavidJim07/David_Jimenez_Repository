import mysql.connector
from datetime import *
import ConectorDirecciones 
import bd

tablaDirecciones=ConectorDirecciones.TablaDirecciones("lafamosa","root","lobito200")

class TablaTienda(object):
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
        self.con.commit()

    def cerrarConeccion(self):
        if self.con:self.con.close()

    def listarTiendasProcedure(self):
        self.myCursor.callproc('sp_mostrarTiendas')
        tiendas=[]
        for result in self.myCursor.stored_results():
            for dato in result.fetchall():
                tienda=bd.Tienda()
                b=0
                for at in dato:
                    if b==0:
                        tienda.setClaveTie(at)
                    elif b==1:
                        tienda.setFaperturaTie(at)
                    elif b==2:
                        tienda.setCalleTie(at)
                    elif b==3:
                        tienda.setNumDomTie(at)
                    elif b==4:
                        tienda.setOrientacionTie(at)
                    elif b==5:
                        tienda.setEntreCallesTie(at)
                    elif b==6:
                        tienda.setTelefonoTie(at)
                    elif b==7:
                        tienda.setMailTie(at)
                    elif b==8:
                        tienda.setClaveCol(at)
                    b+=1
                tiendas.append(tienda)
            return tiendas

    def getTiendasProcedure(self):
        self.myCursor.callproc('sp_mostrarTiendas')
        tiendas=[]
        datos=[]
        dato=str("")
        for result in self.myCursor.stored_results():
            for dato in result.fetchall():
                tienda=bd.Tienda()
                b=0
                dato=""
                for at in dato:
                    if b==0:
                        tienda.setClaveTie(at)
                        dato+=str(at)+" - "
                    elif b==1:
                        tienda.setFaperturaTie(at)
                    elif b==2:
                        tienda.setCalleTie(at)
                    elif b==3:
                        tienda.setNumDomTie(at)
                    elif b==4:
                        tienda.setOrientacionTie(at)
                    elif b==5:
                        tienda.setEntreCallesTie(at)
                    elif b==6:
                        tienda.setTelefonoTie(at)
                    elif b==7:
                        tienda.setMailTie(at)
                    elif b==8:
                        tienda.setClaveCol(at)
                        domicilio,clave=tablaDirecciones.getColonia("",at)
                        domicilio,clave=tablaDirecciones.getCodigoPostal("",clave)
                        dato,clave=tablaDirecciones.getCiudad(dato,clave)
                        dato+="EST "
                        dato=tablaDirecciones.getEstado(dato,clave)
                    b+=1
                tiendas.append(tienda)
                datos.append(dato)
            return datos,tiendas

    def  getCantidadEmProcedure(self, cve_tie):
        args=[f"{cve_tie}"]
        self.myCursor.callproc('sp_cantidadEmpleados',args)
        for result in self.myCursor.stored_results():
            return result.fetchall()

    def  getCantidadVhProcedure(self, cve_tie):
        args=[f"{cve_tie}"]
        self.myCursor.callproc('sp_cantidadVehiculos',args)
        for result in self.myCursor.stored_results():
            return result.fetchall()

    def isEmptyTiendasProcedure(self):
        self.myCursor.callproc('sp_isEmptyTiendas')
        for result in self.myCursor.stored_results():
            if result.fetchall()==0:
                return True
            else:
                return False

    def agregarTiendaProcedure(self,tienda):
        args = [f'{tienda.getFaperturaTie()}',f'{tienda.getCalleTie()}',f'{tienda.getNumDomTie()}',f'{tienda.getOrientacionTie()}',f'{tienda.getEntreCallesTie()}',f'{tienda.getTelefonoTie()}',f'{tienda.getMailTie()}',f'{tienda.getClaveCol()}']
        self.myCursor.callproc('sp_agregarTienda', args)

    def aceptarTiendaProcedure(self):
        self.myCursor.callproc('sp_confirmartienda')

    def cancelarTiendaProcedure(self):
        self.myCursor.callproc('sp_cancelartienda')

    def listarTiendas(self):
        a = self.ejecutar("select * from tienda","listar")
        tiendas=[]
        for i in range(0,len(a)):
            tienda=bd.Tienda()
            b=0
            for at in a[i]:
                if b==0:
                    tienda.setClaveTie(at)
                elif b==1:
                    tienda.setFaperturaTie(at)
                elif b==2:
                    tienda.setCalleTie(at)
                elif b==3:
                    tienda.setNumDomTie(at)
                elif b==4:
                    tienda.setOrientacionTie(at)
                elif b==5:
                    tienda.setEntreCallesTie(at)
                elif b==6:
                    tienda.setTelefonoTie(at)
                elif b==7:
                    tienda.setMailTie(at)
                elif b==8:
                    tienda.setClaveCol(at)
                b+=1
            tiendas.append(tienda)
        return tiendas

    def getTiendas(self):
        a = self.ejecutar("select * from tienda","listar")
        tiendas=[]
        datos=[]
        dato=str("")
        for i in range(0,len(a)):
            tienda=bd.Tienda()
            b=0
            dato=""
            for at in a[i]:
                if b==0:
                    tienda.setClaveTie(at)
                    dato+=str(at)+" - "
                elif b==1:
                    tienda.setFaperturaTie(at)
                elif b==2:
                    tienda.setCalleTie(at)
                elif b==3:
                    tienda.setNumDomTie(at)
                elif b==4:
                    tienda.setOrientacionTie(at)
                elif b==5:
                    tienda.setEntreCallesTie(at)
                elif b==6:
                    tienda.setTelefonoTie(at)
                elif b==7:
                    tienda.setMailTie(at)
                elif b==8:
                    tienda.setClaveCol(at)
                    domicilio,clave=tablaDirecciones.getColonia("",at)
                    domicilio,clave=tablaDirecciones.getCodigoPostal("",clave)
                    dato,clave=tablaDirecciones.getCiudad(dato,clave)
                    dato+="EST "
                    dato=tablaDirecciones.getEstado(dato,clave)
                b+=1
            tiendas.append(tienda)
            datos.append(dato)
        return datos,tiendas

    def  getCantidadEm(self, cve_tie):
        a = self.ejecutar(f"select count(folio_con) from contrato where cve_tie = {cve_tie}","listar")
        return a[0][0]

    def  getCantidadVh(self, cve_tie):
        a = self.ejecutar(f"select count(ns_veh) from vehiculo where cve_tie = {cve_tie}","listar")
        return a[0][0]    

    def isEmptyTie(self):
        a=self.ejecutar("select count(*) from tienda","listar")
        if a[0][0]==0:
            return True
        else:
            return False

    

    