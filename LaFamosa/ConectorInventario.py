import mysql.connector
from datetime import *
import bd

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
