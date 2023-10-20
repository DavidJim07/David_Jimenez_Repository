import mysql.connector
from datetime import *
import bd

class TablaDirecciones(object):
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

    def getEstadosProcedure(self):
        self.myCursor.callproc('sp_mostrarEstados')
        estados=[]
        datos=[]
        cadena=str("")
        for result in self.myCursor.stored_results():
            for dato in result.fetchall():
                estado=bd.Estado()
                b=0
                cadena=""
                for at in dato:
                    if b==0:
                        estado.setClaveEst(at)
                    elif b==1:
                        estado.setNomEst(at)
                        cadena+=str(at)
                    b+=1
                datos.append(cadena)
                estados.append(estado)
            return datos,estados

    def getCiudadesProcedure(self,cve_est):
        args = [f'{cve_est}']
        self.myCursor.callproc('sp_mostrarCiudades',args)
        ciudades=[]
        datos=[]
        cadena=str("")
        for result in self.myCursor.stored_results():
            for dato in result.fetchall():
                ciudad=bd.Ciudad()
                b=0
                cadena=""
                for at in dato:
                    if b==0:
                        ciudad.setClaveCiu(at)
                    elif b==1:
                        ciudad.setNomCiu(at)
                        cadena+=str(at)
                    elif b==2:
                        ciudad.setClaveEst(at)
                    b+=1
                datos.append(cadena)
                ciudades.append(ciudad)
            return datos,ciudades

    def getCodigosPostalesProcedure(self,cve_ciu):
        args = [f'{cve_ciu}']
        self.myCursor.callproc('sp_mostrarCodigosPostales',args)
        codigos=[]
        datos=[]
        cadena=str("")
        for result in self.myCursor.stored_results():
            for dato in result.fetchall():
                codigo=bd.CodigoPostal()
                b=0
                cadena=""
                for at in dato:
                    if b==0:
                        codigo.setClaveCod(at)
                        cadena+=str(at)
                    elif b==1:
                        codigo.setClaveCiu(at)
                    b+=1
                datos.append(cadena)
                codigos.append(codigo)
            return datos,codigos

    def getColoniasProcedure(self,cve_cod):
        args = [f'{cve_cod}']
        self.myCursor.callproc('sp_mostrarColonias',args)
        colonias=[]
        datos=[]
        cadena=str("")
        for result in self.myCursor.stored_results():
            for dato in result.fetchall():
                colonia=bd.Colonia()
                b=0
                cadena=""
                for at in dato:
                    if b==0:
                        colonia.setClaveCol(at)
                    elif b==1:
                        colonia.setNomCol(at)
                        cadena+=str(at)
                    elif b==2:
                        colonia.setClaveCod(at)
                    b+=1
                datos.append(cadena)
                colonias.append(colonia)
            return datos,colonias

    def getEstados(self):
        a = self.ejecutar("select * from estado","listar")
        estados=[]
        datos=[]
        dato=str("")
        for i in range(0,len(a)):
            estado=bd.Estado()
            b=0
            dato=""
            for at in a[i]:
                if b==0:
                    estado.setClaveEst(at)
                elif b==1:
                    estado.setNomEst(at)
                    dato+=str(at)
                b+=1
            datos.append(dato)
            estados.append(estado)
        return datos,estados

    def getCiudades(self,cve_est):
        a = self.ejecutar(f"select * from ciudad where cve_est = {cve_est}","listar")
        ciudades=[]
        datos=[]
        dato=str("")
        for i in range(0,len(a)):
            ciudad=bd.Ciudad()
            b=0
            dato=""
            for at in a[i]:
                if b==0:
                    ciudad.setClaveCiu(at)
                elif b==1:
                    ciudad.setNomCiu(at)
                    dato+=str(at)
                elif b==2:
                    ciudad.setClaveEst(at)
                b+=1
            datos.append(dato)
            ciudades.append(ciudad)
        return datos,ciudades

    def getCodigoPostales(self,cve_ciu):
        a = self.ejecutar(f"select * from codigoPostal where cve_cui = {cve_ciu}","listar")
        codigos=[]
        datos=[]
        dato=str("")
        for i in range(0,len(a)):
            codigo=bd.CodigoPostal()
            b=0
            dato=""
            for at in a[i]:
                if b==0:
                    codigo.setClaveCod(at)
                    dato+=str(at)
                elif b==1:
                    codigo.setClaveCiu(at)
                b+=1
            datos.append(dato)
            codigos.append(codigo)
        return datos,codigos

#--------------------------------------------------------------------------------------------------------------
    def getColonias(self, cve_cod):
        a = self.ejecutar(f"select * from colonia where cve_cod = {cve_cod}","listar")
        colonias=[]
        datos=[]
        dato=str("")
        for i in range(0,len(a)):
            colonia=bd.Colonia()
            b=0
            dato=""
            for at in a[i]:
                if b==0:
                    colonia.setClaveCol(at)
                elif b==1:
                    colonia.setNomCol(at)
                    dato+=str(at)
                elif b==2:
                    colonia.setClaveCod(at)
                b+=1
            datos.append(dato)
            colonias.append(colonia)
        return datos,colonias

    def getColonia(self,salida, cve_col):
        a = self.ejecutar(f"select * from colonia where cve_col = {cve_col}","listar")
        salida+="COL "
        nextClave=0
        for i in range(0,len(a)):
            salida+=a[i][1]+", "
            nextClave=int(a[i][2])
        return salida,nextClave
        #self.getCodigoPostal(salida,nextClave)

    def getCodigoPostal(self,salida, cve_cod):
        a = self.ejecutar(f"select * from codigoPostal where cve_cod = {cve_cod}","listar")
        salida+="CP "
        nextClave=0
        for i in range(0,len(a)):
            salida+=str(a[i][0])+", "
            nextClave=int(a[i][1])
        return salida,nextClave

    def getCiudad(self,salida, cve_ciu):
        a = self.ejecutar(f"select * from ciudad where cve_ciu = {cve_ciu}","listar")
        nextClave=0
        for i in range(0,len(a)):
            salida+=a[i][1]+" "
            nextClave=int(a[i][2])
        return salida,nextClave

    def getEstado(self,salida, cve_est):
        a = self.ejecutar(f"select * from estado where cve_est = {cve_est}","listar")
        salida+=a[0][1]
        return salida

    def getDomicilio(self,itera,salida,clave):
        if itera==0:
            a = self.ejecutar(f"select * from colonia where cve_col = {clave}","listar")
            salida+="COL "
            nextClave=0
            for i in range(0,len(a)):
                salida+=a[i][1]+", "
                nextClave=int(a[i][2])
            return salida,nextClave
            self.getDomicilio(1,salida,nextClave)
        elif itera==1:
            a = self.ejecutar(f"select * from codigoPostal where cve_cod = {clave}","listar")
            salida+="CP "
            nextClave=0
            for i in range(0,len(a)):
                salida+=str(a[i][0])+", "
                nextClave=int(a[i][1])
            self.getDomicilio(2,salida,nextClave)
        elif itera==2:
            a = self.ejecutar(f"select * from ciudad where cve_cui = {clave}","listar")
            nextClave=0
            for i in range(0,len(a)):
                salida+=a[i][1]+" "
                nextClave=int(a[i][2])
            self.getDomicilio(3,salida,nextClave)
        elif itera==3:
            a = self.ejecutar(f"select * from estado where cve_est = {clave}","listar")
            salida+=a[0][1]
            domicilio=salida
            return domicilio

tablaDirecciones=TablaDirecciones("lafamosa","root","lobito200")

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

    def listarProductosProcedure(self):
        self.myCursor.callproc('sp_mostrarProducto')
        productos=[]
        for result in self.myCursor.stored_results():
            for dato in result.fetchall():
                producto=bd.Producto()
                b=0
                for at in dato:
                    if b==0:
                        producto.setCodbarPro(at)
                    elif b==1:
                        producto.setNomPro(at)
                    elif b==2:
                        producto.setTipoPro(at)
                    elif b==3:
                        producto.setMarcaPro(at)
                    elif b==4:
                        producto.setColorPro(at)
                    elif b==5:
                        producto.setGarantiaPro(at)
                    elif b==6:
                        producto.setUmedidaGarantiaPro(at)
                    elif b==7:
                        producto.setPresentacionPro(at)
                    elif b==8:
                        producto.setModeloPro(at)
                    elif b==9:
                        producto.setAltoPro(at)
                    elif b==10:
                        producto.setLargoPro(at)
                    elif b==11:
                        producto.setAnchoPro(at)
                    elif b==10:
                        producto.setContenidoPro(at)
                    elif b==12:
                        producto.setUmedidaPro(at)
                    elif b==14:
                        producto.setCodigoPro(at)
                    b+=1
                productos.append(producto)
        return productos

    def buscarPrecioVentaProcedure(self,codb_pro):
        args = [f'{codb_pro}']
        self.myCursor.callproc('sp_getPrecioVenta',args)
        precioVenta=bd.PrecioVenta()
        b=0
        for result in self.myCursor.stored_results():
            for dato in result.fetchall():
                for at in dato:
                    if b==0:
                        precioVenta.setClavePre(at)
                    elif b==1:
                        precioVenta.setFechaPre(at)
                    elif b==2:
                        precioVenta.setPrecioPre(at)
                    elif b==3:
                        precioVenta.setCodbarPro(at)
                    b+=1
        return precioVenta

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

    def getProveedoresProcedure(self):
        a = self.ejecutar("select * from proveedor","listar")
        proveedores=[]
        datos=[]
        dato=""
        for i in range(0,len(a)):
            proveedor=bd.Proveedor()
            b=0
            dato=""
            for at in a[i]:
                if b==0:
                    proveedor.setClaveProv(at)
                elif b==1:
                    proveedor.setNomEmpProv(at)
                    dato+=str(at)
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
            datos.append(dato)
            proveedores.append(proveedor)
        return datos,proveedores

    def getProveedorProcedure(self,cve_prov):
        args = [f'{cve_prov}']
        self.myCursor.callproc('sp_buscarProveedor',args)
        proveedor=bd.Proveedor()
        for result in self.myCursor.stored_results():
            for dato in result.fetchall():
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
        return proveedor

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
    
    def isEmptyProveedorProcedure(self):
        self.myCursor.callproc('sp_isemptyproveedor')
        for result in self.myCursor.stored_results():
            if result.fetchall()==0:
                return True
            else:
                return False

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

    def getCantidadEmProcedure(self, cve_tie):
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

    def getTiendasDisponiblesProcedure(self,codbar):
        args=[f'{codbar}']
        self.myCursor.callproc('sp_buscartiendasdisponibles',args)
        tiendas=[]
        datos=[]
        dato=str("")
        for result in self.myCursor.stored_results():
            for dato in result.fetchall():
                print(result.fetchall())
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

    def getTiendasConsulta(self,codBar_pro):
        a = self.ejecutar(f"select * from tienda where tienda.cve_tie not in(select cve_tie from minmax where codbar_pro={codBar_pro}) group by tienda.cve_tie;","listar")
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

class TablaProductos(object):
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

    def listarProductosProcedure(self):
        self.myCursor.callproc('sp_mostrarProducto')
        productos=[]
        for result in self.myCursor.stored_results():
            for dato in result.fetchall():
                producto=bd.Producto()
                b=0
                for at in dato:
                    if b==0:
                        producto.setCodbarPro(at)
                    elif b==1:
                        producto.setNomPro(at)
                    elif b==2:
                        producto.setTipoPro(at)
                    elif b==3:
                        producto.setMarcaPro(at)
                    elif b==4:
                        producto.setColorPro(at)
                    elif b==5:
                        producto.setGarantiaPro(at)
                    elif b==6:
                        producto.setUmedidaGarantiaPro(at)
                    elif b==7:
                        producto.setPresentacionPro(at)
                    elif b==8:
                        producto.setModeloPro(at)
                    elif b==9:
                        producto.setAltoPro(at)
                    elif b==10:
                        producto.setLargoPro(at)
                    elif b==11:
                        producto.setAnchoPro(at)
                    elif b==10:
                        producto.setContenidoPro(at)
                    elif b==12:
                        producto.setUmedidaPro(at)
                    elif b==14:
                        producto.setCodigoPro(at)
                    b+=1
                productos.append(producto)
        return productos

    def getProductosProcedure(self):
        a = self.ejecutar(f"select * from producto;","listar")
        productos=[]
        datos=[]
        dato=str("")
        for i in range(0,len(a)):
            producto=bd.Producto()
            b=0
            dato=""
            for at in a[i]:
                if b==0:
                    producto.setCodbarPro(at)
                elif b==1:
                    producto.setNomPro(at)
                    dato+=at
                elif b==2:
                    producto.setTipoPro(at)
                elif b==3:
                    producto.setMarcaPro(at)
                elif b==4:
                    producto.setColorPro(at)
                elif b==5:
                    producto.setGarantiaPro(at)
                elif b==6:
                    producto.setUmedidaGarantiaPro(at)
                elif b==7:
                    producto.setPresentacionPro(at)
                elif b==8:
                    producto.setModeloPro(at)
                elif b==9:
                    producto.setAltoPro(at)
                elif b==10:
                    producto.setLargoPro(at)
                elif b==11:
                    producto.setAnchoPro(at)
                elif b==10:
                    producto.setContenidoPro(at)
                elif b==12:
                    producto.setUmedidaPro(at)
                elif b==14:
                    producto.setCodigoPro(at)
                b+=1
            productos.append(producto)
            datos.append(dato)
        return datos,productos

    def buscarPrecioVentaProcedure(self,codb_pro):
        args = [f'{codb_pro}']
        self.myCursor.callproc('sp_getPrecioVenta',args)
        precioVenta=bd.PrecioVenta()
        b=0
        for result in self.myCursor.stored_results():
            for dato in result.fetchall():
                for at in dato:
                    if b==0:
                        precioVenta.setClavePre(at)
                    elif b==1:
                        precioVenta.setFechaPre(at)
                    elif b==2:
                        precioVenta.setPrecioPre(at)
                    elif b==3:
                        precioVenta.setCodbarPro(at)
                    b+=1
        return precioVenta

    def isEmptyProductoProcedure(self):
        self.myCursor.callproc('sp_isemptyproducto')
        for result in self.myCursor.stored_results():
            if result.fetchall()==0:
                return True
            else:
                return False

    def getProductoProcedure(self,codigo_pro):
        args=[f"{codigo_pro}"]
        self.myCursor.callproc('sp_buscarCodigoBarras',args)
        producto=bd.Producto()
        for result in self.myCursor.stored_results():
            for dato in result.fetchall():
                b=0
                for at in dato:
                    if b==0:
                        producto.setCodbarPro(at)
                    elif b==1:
                        producto.setNomPro(at)
                    elif b==2:
                        producto.setTipoPro(at)
                    elif b==3:
                        producto.setMarcaPro(at)
                    elif b==4:
                        producto.setColorPro(at)
                    elif b==5:
                        producto.setGarantiaPro(at)
                    elif b==6:
                        producto.setUmedidaGarantiaPro(at)
                    elif b==7:
                        producto.setPresentacionPro(at)
                    elif b==8:
                        producto.setModeloPro(at)
                    elif b==9:
                        producto.setAltoPro(at)
                    elif b==10:
                        producto.setLargoPro(at)
                    elif b==11:
                        producto.setAnchoPro(at)
                    elif b==10:
                        producto.setContenidoPro(at)
                    elif b==12:
                        producto.setUmedidaPro(at)
                    elif b==14:
                        producto.setCodigoPro(at)
                    b+=1
        return producto

    def guardarProductoProcedure(self,producto,precioVenta):
        args=[f'{producto.getNomPro()}',f'{producto.getTipoPro()}',f'{producto.getMarcaPro()}',f'{producto.getColorPro()}',f'{producto.getGarantiaPro()}',f'{producto.getPresentacionPro()}',f'{producto.getModeloPro()}',f'{producto.getAltoPro()}',f'{producto.getLargoPro()}',f'{producto.getAnchoPro()}',f'{producto.getContenidoPro()}',f'{producto.getUmedidaPro()}',f'{producto.getCodigoPro()}',
                f"{precioVenta}"]
        self.myCursor.callproc('sp_agregarProducto',args)
        for result in self.myCursor.stored_results():
            return result.fetchall()

    def guardarMinimoMaximoProcedure(self,minmax):
        args=[f'{minmax.getMinMinMax()}',f'{minmax.getMaxMinMax()}',f'{minmax.getCodbarPro()}',f'{minmax.getClaveTie()}']
        self.myCursor.callproc('sp_agregarminmax',args)

    def getTiendasDisponiblesProcedure(self,codbar):
        args=[f'{codbar}']
        self.myCursor.callproc('sp_buscartiendasdisponibles',args)
        tiendas=[]
        datos=[]
        dato=str("")
        for result in self.myCursor.stored_results():
            x=result.fetchall()
            print(x)
            for dato in x:
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

    def aceptarProductoProcedure(self):
        self.myCursor.callproc('sp_confirmarproducto')

    def cancelarProductoProcedure(self):
        self.myCursor.callproc('sp_cancelarproducto')

    
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

    def cantidadSubResurtidosProcedure(self,cve_res):
        args=[f'{cve_res}']
        self.myCursor.callproc('sp_mostrarCantidadResurtidos',args)
        for result in self.myCursor.stored_results():
            return result.fetchall()

    def guardarResurtidoProcedure(self,resurtir):
        args=[f'{resurtir.getTotalRes()}',f'{resurtir.getClaveProv()}',f'{resurtir.getClaveTie()}']
        self.myCursor.callproc('sp_resurtido',args)
        for result in self.myCursor.stored_results():
            return result.fetchall()

    def guardarRenglonResurtidoProcedure(self,renglonResurtir):
        args=[f'{resurtir.getTotalRes()}',f'{resurtir.getClaveProv()}',f'{resurtir.getClaveTie()}']
        self.myCursor.callproc('sp_resurtido',args)

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

    def isEmptyResurtidos(self):
        self.myCursor.callproc('sp_isEmptyResurtidos')
        for result in self.myCursor.stored_results():
            if result.fetchall()==0:
                return True
            else:
                return False
