import mysql.connector
from datetime import *
import bd

class TablaProveedores(object):
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

    def listarProveedoresProcedure(self):
        self.myCursor.callproc('sp_mostrarProveedores')
        proveedores=[]
        for result in self.myCursor.stored_results():
            for dato in result.fetchall():
                proveedor=bd.Proveedor()
                b=0
                for at in dato:
                    if b==0:
                        proveedor.setClaveProv(at)
                    elif b==1:
                        proveedor.setNomEmpProv(at)
                    elif b==2:
                        proveedor.setCalleProv(at)
                    elif b==3:
                        proveedor.setNumDomProv(at)
                    elif b==4:
                        proveedor.setOrientacionProv(at)
                    elif b==5:
                        proveedor.setEntreCallesProv(at)
                    elif b==6:
                        proveedor.setTelefonoProv(at)
                    elif b==7:
                        proveedor.setMailProv(at)
                    elif b==8:
                        proveedor.setClaveCol(at)
                    b+=1
                proveedores.append(proveedor)
        return proveedores

    def buscarRepresentanteProcedure(self,cve_prov):
        args = [f'{cve_prov}']
        self.myCursor.callproc('sp_buscarRepresentante',args)
        representante=bd.Representante()
        b=0
        for result in self.myCursor.stored_results():
            for dato in result.fetchall():
                for at in dato:
                    if b==0:
                        representante.setNumRep(at)
                    elif b==1:
                        representante.setFechaRep(at)
                    elif b==2:
                        representante.setClavePer(at)
                    elif b==3:
                        representante.setClaveProv(at)
                    b+=1
        return representante

    def getPersonaProcedure(self,cve_per):
        args = [f'{cve_per}']
        self.myCursor.callproc('sp_mostrarEmpleadoPersona', args)
        persona=bd.Persona()
        for result in self.myCursor.stored_results():
            for dato in result.fetchall():
                b=0
                for at in dato:
                    if b==0:
                        persona.setClavePer(at)
                    elif b==1:
                        persona.setNomPer(at)
                    elif b==2:
                        persona.setApPer(at)
                    elif b==3:
                        persona.setAmPer(at)
                    elif b==4:
                        persona.setCallePer(at)
                    elif b==5:
                        persona.setNumDomPer(at)
                    elif b==6:
                        persona.setOrientacionPer(at)
                    elif b==7:
                        persona.setEntreCallesPer(at)
                    elif b==8:
                        persona.setTelefonoPer(at)
                    elif b==9:
                        persona.setMailPer(at)
                    elif b==10:
                        persona.setSexoPer(at)
                    elif b==11:
                        persona.setFnacimientoPer(at)
                    elif b==12:
                        persona.setEdoCivilPer(at)
                    elif b==13:
                        persona.setColPer(at)
                    elif b==14:
                        persona.setCURPPer(at)
                    b+=1
        return persona

    def buscarPersonaCurpProcedure(self,curp_per):
        args = [f'{curp_per}']
        self.myCursor.callproc('sp_buscarPersonaCurp', args)
        persona=bd.Persona()
        for result in self.myCursor.stored_results():
            for dato in result.fetchall():
                b=0
                for at in dato:
                    if b==0:
                        persona.setClavePer(at)
                    elif b==1:
                        persona.setNomPer(at)
                    elif b==2:
                        persona.setApPer(at)
                    elif b==3:
                        persona.setAmPer(at)
                    elif b==4:
                        persona.setCallePer(at)
                    elif b==5:
                        persona.setNumDomPer(at)
                    elif b==6:
                        persona.setOrientacionPer(at)
                    elif b==7:
                        persona.setEntreCallesPer(at)
                    elif b==8:
                        persona.setTelefonoPer(at)
                    elif b==9:
                        persona.setMailPer(at)
                    elif b==10:
                        persona.setSexoPer(at)
                    elif b==11:
                        persona.setFnacimientoPer(at)
                    elif b==12:
                        persona.setEdoCivilPer(at)
                    elif b==13:
                        persona.setColPer(at)
                    elif b==14:
                        persona.setCURPPer(at)
                    b+=1
        return persona

    def agregarProveedorProcedure(self,persona,proveedor):
        args = [f'{proveedor.getNomEmpProv()}',f'{proveedor.getCalleProv()}',f'{proveedor.getNumDomProv()}',f'{proveedor.getOrientacionProv()}',f'{proveedor.getEntreCallesProv()}',
        f'{proveedor.getTelefonoProv()}',f'{proveedor.getMailProv()}',f'{proveedor.getClaveCol()}',f'{persona.getNomPer()}',f'{persona.getApPer()}',f'{persona.getAmPer()}',
        f'{persona.getCallePer()}',f'{persona.getNumDomPer()}',f'{persona.getOrientacionPer()}',f'{persona.getEntreCallesPer()}',
        f'{persona.getTelefonoPer()}',f'{persona.getMailPer()}',f'{persona.getSexoPer()}',f'{persona.getFnacimientoPer()}',f'{persona.getEdoCivilPer()}',f'{persona.getColPer()}',f'{persona.getCURPPer()}']
        self.myCursor.callproc('sp_agregarProveedorProcedure', args)

    def confirmarProveedorProcedure(self):
        self.myCursor.callproc('sp_confirmarproveedor')

    def cancelarProveedoroProcedure(self):
        self.myCursor.callproc('sp_cancelarproveedor')

    