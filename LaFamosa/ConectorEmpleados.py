import mysql.connector
from datetime import *
import bd

domicilio=str("")

class TablaEmpleados(object):
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

    def listarEmpleadosProcedure(self):
        self.myCursor.callproc('sp_mostrarEmpleados')
        #self.ejecutar('sp_mostrarEmpleados',"llamar")
        #for result in self.myCursor.stored_results():
         #   print(result.fetchall())
        contratos=[]
        for result in self.myCursor.stored_results():
            for dato in result.fetchall():
                contrato=bd.Contrato()
                b=0
                for at in dato:
                    if b==0:
                        contrato.setClaveCon(at)
                    elif b==1:
                        contrato.setFechaInicioCon(at)
                    elif b==2:
                        contrato.setFechaFinCon(at)
                    elif b==3:
                        contrato.setPuestoCon(at)
                    elif b==4:
                        contrato.setSueldoCon(at)
                    elif b==5:
                        contrato.setPeriodoSueldoCon(at)
                    elif b==6:
                        contrato.setHentradaCon(at)
                    elif b==7:
                        contrato.setHsalidaCon(at)
                    elif b==8:
                        contrato.setHIniComidaCon(at)
                    elif b==9:
                        contrato.setHFinComidaCon(at)
                    elif b==10:
                        contrato.setComisionesCon(at)
                    elif b==11:
                        contrato.setClaveTie(at)
                    elif b==12:
                        contrato.setClavePer(at)
                    b+=1
                contratos.append(contrato)
        return contratos

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

    def buscarEmpleadoProcedure(self,folio_con):
        args=[f"{folio_con}"]
        self.myCursor.callproc('sp_buscarEmpleado',args)
        for result in self.myCursor.stored_results():
            for dato in result.fetchall():
                contrato=bd.Contrato()
                b=0
                for at in dato:
                    if b==0:
                        contrato.setClaveCon(at)
                    elif b==1:
                        contrato.setFechaInicioCon(at)
                    elif b==2:
                        contrato.setFechaFinCon(at)
                    elif b==3:
                        contrato.setPuestoCon(at)
                    elif b==4:
                        contrato.setSueldoCon(at)
                    elif b==5:
                        contrato.setPeriodoSueldoCon(at)
                    elif b==6:
                        contrato.setHentradaCon(at)
                    elif b==7:
                        contrato.setHsalidaCon(at)
                    elif b==8:
                        contrato.setHIniComidaCon(at)
                    elif b==9:
                        contrato.setHFinComidaCon(at)
                    elif b==10:
                        contrato.setComisionesCon(at)
                    elif b==11:
                        contrato.setClaveTie(at)
                    elif b==12:
                        contrato.setClavePer(at)
                    b+=1
                return contrato

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

    def isEmptyEmpleadoProcedure(self):
        self.myCursor.callproc('sp_isEmptyEmpleados')
        for result in self.myCursor.stored_results():
            if result.fetchall()==0:
                return True
            else:
                return False

    def agregarContratoProcedure(self,persona,contrato):
        args = [f'{persona.getNomPer()}',f'{persona.getApPer()}',f'{persona.getAmPer()}',f'{persona.getCallePer()}',f'{persona.getNumDomPer()}',f'{persona.getOrientacionPer()}',f'{persona.getEntreCallesPer()}',
        f'{persona.getTelefonoPer()}',f'{persona.getMailPer()}',f'{persona.getSexoPer()}',f'{persona.getFnacimientoPer()}',f'{persona.getEdoCivilPer()}',f'{persona.getColPer()}',f'{persona.getCURPPer()}',
        f'{contrato.getFechaInicioCon()}',f'{contrato.getFechaFinCon()}',f'{contrato.getPuestoCon()}',f'{contrato.getSueldoCon()}',f'{contrato.getPeriodoSueldoCon()}',f'{contrato.getHIniComidaCon()}',f'{contrato.getHFinComidaCon()}',f'{contrato.getClaveTie()}',]
        self.myCursor.callproc('sp_personacontrato', args)

    def confirmarContratoProcedure(self):
        self.myCursor.callproc('sp_confirmarcontrato')

    def cancelarContratoProcedure(self):
        self.myCursor.callproc('sp_cancelarcontrato')

    def listarEmpleados(self):
        a = self.ejecutar("select * from contrato","listar")
        contratos=[]
        for i in range(0,len(a)):
            contrato=bd.Contrato()
            b=0
            for at in a[i]:
                if b==0:
                    contrato.setClaveCon(at)
                elif b==1:
                    contrato.setFechaInicioCon(at)
                elif b==2:
                    contrato.setFechaFinCon(at)
                elif b==3:
                    contrato.setPuestoCon(at)
                elif b==4:
                    contrato.setSueldoCon(at)
                elif b==5:
                    contrato.setPeriodoSueldoCon(at)
                elif b==6:
                    contrato.setHentradaCon(at)
                elif b==7:
                    contrato.setHsalidaCon(at)
                elif b==8:
                    contrato.setHIniComidaCon(at)
                elif b==9:
                    contrato.setHFinComidaCon(at)
                elif b==10:
                    contrato.setComisionesCon(at)
                elif b==11:
                    contrato.setClaveTie(at)
                elif b==12:
                    contrato.setClavePer(at)
                b+=1
            contratos.append(contrato)
        return contratos

    def getPersona(self,cve_per):
        a = self.ejecutar(f"select * from persona where cve_per = {cve_per}","listar")
        persona=bd.Persona()
        for i in range(0,len(a)):
            b=0
            for at in a[i]:
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
    
    """
    def getNombre(self, cve_per):
        a = self.ejecutar(f"select nom_per, ap_per, am_per from persona where cve_per = {cve_per}","listar")
        nombre=str("")
        for i in range(0,len(a)):
            b=0
            for at in a[i]:
                if b==0:
                    nombre+=at+" "
                elif b==1:
                    nombre+=at+" "
                elif b==2:
                    nombre+=at
        return nombre
    """

    def buscarEmpleado(self, folio_con):
        return self.ejecutar(f"select * from contrato where folio_con = {folio_con}","buscar")

    def isEmptyEm(self):
        a=self.ejecutar("select count(*) from contrato","listar")
        if a[0][0]==0:
            return True
        else:
            return False