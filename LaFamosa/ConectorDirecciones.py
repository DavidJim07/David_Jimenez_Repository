import mysql.connector
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