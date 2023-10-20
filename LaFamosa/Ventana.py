from calendar import calendar
from logging import exception
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
from tkinter import font
from tkinter import ttk
from tkinter.ttk import Treeview
import tkinter.ttk as tkk
import tkinter
from datetime import *

import ConectorEmpleados,ConectorTiendas,ConectorDirecciones,ConectorProveedor,ConectorInventario, Conector,bd
from tkcalendar import *

tablaEmpleados=Conector.TablaEmpleados("lafamosa","root","lobito200")
tablaTiendas=Conector.TablaTienda("lafamosa","root","lobito200")
tablaDirecciones=Conector.TablaDirecciones("lafamosa","root","lobito200")
tablaProveedores=Conector.TablaProveedores("lafamosa","root","lobito200")
tablaProductos=Conector.TablaProductos("lafamosa","root","lobito200")
tablaResurtidos=Conector.TablaResurtidos("lafamosa","root","lobito200")

container=Frame
def setContainer(container1):
    global container
    container=container1

def getContainer():
    global container
    return container

class Ventana(Tk):
    def __init__(self):
        super().__init__()
        self.state("zoomed")
        self.title("La Famosa")
        #self.iconbitmap("dm 150.ico")
        self.resizable(True,True)
        self.config(background='lightgray')
        #self.resizable(False,False)

        self.menuBar=Menu(self)
        self.config(menu=self.menuBar)
        #SE CREAN LAS OPCIONES DEL MENU CON SUS SUBOPCIONES
        self.menuTiendas=Menu(self.menuBar,tearoff=0)
        self.menuTiendas.add_command(label="Agregar Tienda",command=self.registrarTiendas)
        self.menuTiendas.add_command(label="Consultar/Modificar Tienda",command=self.consultarUsuarios)
        self.menuTiendas.add_command(label="Listar Tiendas",command=self.listarTiendas)
        self.menuBar.add_cascade(label="       Tiendas       ",menu=self.menuTiendas)

        self.menuEmpleados=Menu(self.menuBar,tearoff=0)
        self.menuEmpleados.add_command(label="Agregar Empleado",command=self.registrarEmpleados)
        self.menuEmpleados.add_command(label="Consultar/Modificar Empleados",command=self.consultarLibros)
        self.menuEmpleados.add_command(label="Registrar Checador",command=self.modificarLibros)
        self.menuEmpleados.add_command(label="Listar Empleados",command=self.listarEmpleados)
        self.menuBar.add_cascade(label="     Empleados    ",menu=self.menuEmpleados)

        self.menuProveedores=Menu(self.menuBar,tearoff=0)
        self.menuProveedores.add_command(label="Agregar Proveedor",command=self.registrarProveedores)
        self.menuProveedores.add_command(label="Consultar/Modificar Proveedor",command=self.consultarPrestamos)
        self.menuProveedores.add_command(label="Cambiar Representante",command=self.devolverPrestamos)
        self.menuProveedores.add_command(label="Listar Proveedores",command=self.listarProveedores)
        self.menuBar.add_cascade(label="    Proveedores   ",menu=self.menuProveedores)

        self.menuInventario=Menu(self.menuBar,tearoff=0)
        self.menuInventario.add_command(label="Agregar Producto",command=self.registrarProductos)
        self.menuInventario.add_command(label="Consultar/Modificar Producto",command=self.consultarUsuarios)
        self.menuInventario.add_command(label="Agregar Resurtido",command=self.registrarResurtidos)
        self.menuInventario.add_command(label="Consultar/Modificar Resurtido",command=self.eliminarUsuarios)
        self.menuInventario.add_command(label="Listar Productos",command=self.listarProductos)
        self.menuInventario.add_command(label="Listar Resurtidos",command=self.listarResurtidos)
        self.menuBar.add_cascade(label="      Inventario    ",menu=self.menuInventario)

        self.menuClientes=Menu(self.menuBar,tearoff=0)
        self.menuClientes.add_command(label="Agregar Cliente",command=self.modificarUsuarios)
        self.menuClientes.add_command(label="Consultar/Modificar Cliente",command=self.consultarUsuarios)
        self.menuClientes.add_command(label="Listar Clientes",command=self.listarUsuarios)
        self.menuBar.add_cascade(label="       Clientes      ",menu=self.menuClientes)

        self.menuVentas=Menu(self.menuBar,tearoff=0)
        self.menuVentas.add_command(label="Agregar Venta",command=self.modificarUsuarios)
        self.menuVentas.add_command(label="Consultar Venta",command=self.consultarUsuarios)
        self.menuVentas.add_command(label="Listar Ventas",command=self.listarUsuarios)
        self.menuBar.add_cascade(label="        Ventas        ",menu=self.menuVentas)

        self.menuDevoluciones=Menu(self.menuBar,tearoff=0)
        self.menuDevoluciones.add_command(label="Agregar Devolución",command=self.modificarUsuarios)
        self.menuDevoluciones.add_command(label="Consultar/Modificar Devolución",command=self.consultarUsuarios)
        self.menuDevoluciones.add_command(label="Listar Devoluciones",command=self.listarUsuarios)
        self.menuBar.add_cascade(label="   Devoluciones   ",menu=self.menuDevoluciones)

        Grid.rowconfigure(self,0,weight=1) 
        Grid.columnconfigure(self,0,weight=1)
        self.panelInicio()

        self.mainloop()

    def panelInicio(self):
        panelListarEmpleados = PanelInicio(self)
        panelListarEmpleados.grid(column=0, row=0,)
    #METODOS OYENTE PARA LAS OPCIONES

    #TIENDAS 
    def listarTiendas(self):
        if not tablaTiendas.isEmptyTiendasProcedure():
            self.container=getContainer()
            for conElement in self.container.winfo_children():
                if not isinstance(conElement,Menu):
                    conElement.destroy()
            panelListarTiendas = PanelListarTiendas(self)
            panelListarTiendas.grid(column=0, row=0)
        else:
            mb.showinfo(title="Error",message="No hay tiendas registradas")

    def registrarTiendas(self):
        self.container=getContainer()
        for conElement in self.container.winfo_children():
            if not isinstance(conElement,Menu):
                conElement.destroy()
        panelRegistrarTiendas = PanelRegistroTiendas(self)
        panelRegistrarTiendas.grid(column=0, row=0)
        
    def consultarUsuarios(self):
        print("im")
    
    def modificarUsuarios(self):
        print("im")
        
    def eliminarUsuarios(self):
        print("im")
            
    def listarUsuarios(self):
        print("im")

    def registrarEmpleados(self):
        self.container=getContainer()
        for conElement in self.container.winfo_children():
            if not isinstance(conElement,Menu):
                conElement.destroy()
        panelRegistrarEmpleados = PanelRegistroEmpleados(self)
        panelRegistrarEmpleados.grid(column=0, row=0)

    def listarEmpleados(self):
        if not tablaEmpleados.isEmptyEmpleadoProcedure():
            self.container=getContainer()
            for conElement in self.container.winfo_children():
                if not isinstance(conElement,Menu):
                    conElement.destroy()
            panelListarEmpleados = PanelListarEmpleados(self)
            panelListarEmpleados.grid(column=0, row=0, sticky="nsew")
        else:
            mb.showinfo(title="Error",message="No hay empleados registrados")

    def iniciarLibros(self):
        print("im")

    def iniciarProductowdfveves(self):
        print("im")
#LISTAR PROVEEDORES
    def registrarProveedores(self):
        self.container=getContainer()
        for conElement in self.container.winfo_children():
            if not isinstance(conElement,Menu):
                conElement.destroy()
        panelRegistrarProveedores = PanelRegistroProveedores(self)
        panelRegistrarProveedores.grid(column=0, row=0)

    def listarProveedores(self):
        if not tablaProveedores.isEmptyProveedorProcedure():
            self.container=getContainer()
            for conElement in self.container.winfo_children():
                if not isinstance(conElement,Menu):
                    conElement.destroy()
            panelListarProveedores = PanelListarProveedores(self)
            panelListarProveedores.grid(column=0, row=0)
        else:
            mb.showinfo(title="Error",message="No hay proveedores registrados")
        
    def listarLibros(self):
        print("im")

    def consultarLibros(self):
        print("im")

    def registrarProductos(self):
        self.container=getContainer()
        for conElement in self.container.winfo_children():
            if not isinstance(conElement,Menu):
                conElement.destroy()
        panelRegistrarProductos = PanelRegistroProductos(self)
        panelRegistrarProductos.grid(column=0, row=0)

    def listarProductos(self):
        if not tablaProductos.isEmptyProductoProcedure():
            self.container=getContainer()
            for conElement in self.container.winfo_children():
                if not isinstance(conElement,Menu):
                    conElement.destroy()
            panelListarProductos = PanelListarProductos(self)
            panelListarProductos.grid(column=0, row=0)
        else:
            mb.showinfo(title="Error",message="No hay productos registrados")
        
    def modificarLibros(self):
        print("im")
        
    def eliminarLibros(self):
        print("im")

    def registrarResurtidos(self):
        self.container=getContainer()
        for conElement in self.container.winfo_children():
            if not isinstance(conElement,Menu):
                conElement.destroy()
        panelregistrarResurtidos = PanelRegistroResurtidos(self)
        panelregistrarResurtidos.grid(column=0, row=0)

    def listarResurtidos(self):
        if not tablaResurtidos.isEmptyResurtidos():
            self.container=getContainer()
            for conElement in self.container.winfo_children():
                if not isinstance(conElement,Menu):
                    conElement.destroy()
            panelListarResurtidos = PanelListarResurtidos(self)
            panelListarResurtidos.grid(column=0, row=0)
        else:
            mb.showinfo(title="Error",message="No hay resurtidos registrados")

    def registrarPrestamos(self):
        print("im")
    
    def consultarPrestamos(self):
        print("im")
            
    def modificarPrestamos(self):
        print("im")
            
    def devolverPrestamos(self):
        print("im")
        
    def listarPrestamos(self):
        print("im")
    

#PANELES PARA CREAR EVENTOS
class PanelInicio(Frame):
    def __init__(self, container):
        super().__init__(container)
        self.config(background='lightgray')
        self.columnconfigure(0,weight=1)
        self.columnconfigure(0,weight=3)
        self.container=container
        setContainer(container)
        self.__create_widgets()

    def __create_widgets(self):
        fuente= "Helvetica 12 "
        self.ejemplo=Label(self, text='Prueba de panel inico',font = fuente,bg='lightgray').grid(column=0, row=1, sticky=tkinter.W)
        self.botonSalir=Button(self, text='Cerrar', font=fuente, command=self.onSalir).grid(column=0, row=2)
        #self.cal = Calendar(self, selectmode = 'day') .grid(column=2, row=1)
        fecha=datetime.now()
        año=fecha.year-18
        self.my_combobox_tiendas=tkk.Combobox(self,width=18,font = fuente,state="readonly")
        self.cal = DateEntry(self)#
        self.cal.grid(column=0, row=0, sticky=tkinter.W)
        #self.boton = Button(self, text="ok", command=self.print_sel).grid(column=1, row=2)

        for widget in self.winfo_children():
            widget.grid(padx=5, pady=5)

    def onSalir(self):
        for conElement in self.container.winfo_children():
            if not isinstance(conElement,Menu):
                conElement.destroy()

#REGISTRAR NUEVAS TIENDAS
class PanelRegistroTiendas(Frame):
    def __init__(self, container):
        super().__init__(container)
        self.config(bg='lightgray')
        self.columnconfigure(0,weight=1)
        self.columnconfigure(0,weight=3)
        setContainer(container)
        self.__create_widgets()

    def __create_widgets(self):
        fuente= "Helvetica 12 "
        self.lblDatos=Label(self,text="DATOS DE LA TIENDA",font = fuente,bg='lightgray').grid(column=1,row=0)
        
        self.lblfechaApertura=Label(self,text="Fecha apetura",font = fuente,bg='lightgray').grid(column=0,row=1)

        self.fechaApertura=DateEntry(self,selectmode='day', width=57)
        self.fechaApertura.grid(column=1, row=1)

        self.lblNumeroTelefonico=Label(self,text="Número telefonico",font = fuente,bg='lightgray').grid(column=0,row=2)

        self.numeroTelefonico_var=StringVar()
        self.numeroTelefonico_var.set("")
        self.entradaNumeroTelefonico=Entry(self, width=40, textvariable=self.numeroTelefonico_var,font = fuente)
        self.entradaNumeroTelefonico.grid(column=1,row=2)
        #self.entradaNumeroTelefonico.bind("<FocusIn>", self.foc_in_num)
        self.entradaNumeroTelefonico.focus()
        self.entradaNumeroTelefonico.bind("<Return>", self.onEntNum)

        self.lblCorreoElectronico=Label(self,text="Correo electronico",font = fuente,bg='lightgray').grid(column=0,row=3)

        self.correoElectronico_var=StringVar()
        self.correoElectronico_var.set("Ingrese el correo electronico")
        self.entradaCorreoElectronico=Entry(self, width=40, textvariable=self.correoElectronico_var,font = fuente)
        self.entradaCorreoElectronico.grid(column=1,row=3)
        self.entradaCorreoElectronico.bind("<FocusIn>", self.foc_in_cor)
        self.entradaCorreoElectronico.bind("<Return>", self.onEntCorreo)

        self.lblEstado=Label(self,text="Estado",font = fuente,bg='lightgray').grid(column=0,row=4)

        self.my_combobox_estado=tkk.Combobox(self,width=38,font = fuente,state="readonly")
        self.my_combobox_estado.grid(column=1,row=4)
        self.nomEst, self.datoEst = tablaDirecciones.getEstadosProcedure()
        self.my_combobox_estado.set(self.nomEst[0])
        self.my_combobox_estado['values']=self.nomEst
        self.my_combobox_estado.bind("<<ComboboxSelected>>", self.onSeleccionEstado)
        self.my_combobox_estado.bind("<Return>", self.onEntEstado)

        self.lblCiudad=Label(self,text="Ciudad",font = fuente,bg='lightgray').grid(column=0,row=5)

        self.my_combobox_ciudad=tkk.Combobox(self,width=38,font = fuente,state=tkinter.DISABLED)
        self.my_combobox_ciudad.grid(column=1,row=5)
        self.my_combobox_ciudad.bind("<<ComboboxSelected>>", self.onSeleccionCiudad)
        self.my_combobox_ciudad.bind("<Return>", self.onEntCiudad)

        self.lblCodigoPostal=Label(self,text="Codigo postal",font = fuente,bg='lightgray').grid(column=0,row=6)

        self.my_combobox_codigoPostal=tkk.Combobox(self,width=38,font = fuente,state=tkinter.DISABLED)
        self.my_combobox_codigoPostal.grid(column=1,row=6)
        self.my_combobox_codigoPostal.bind("<<ComboboxSelected>>", self.onSeleccionCodigo)
        self.my_combobox_codigoPostal.bind("<Return>", self.onEntCodigo)

        self.lblColonia=Label(self,text="Colonia",font = fuente,bg='lightgray').grid(column=0,row=7)

        self.my_combobox_colonia=tkk.Combobox(self,width=38,font = fuente,state=tkinter.DISABLED)
        self.my_combobox_colonia.grid(column=1,row=7)
        self.my_combobox_colonia.bind("<<ComboboxSelected>>", self.onSeleccionColonia)
        self.my_combobox_colonia.bind("<Return>", self.onEntColonia)

        self.lblCalle=Label(self,text="Calle",font = fuente,bg='lightgray').grid(column=0,row=8)

        self.calle_var=StringVar()
        self.calle_var.set("Ingrese la calle")
        self.entradaCalle=Entry(self, width=40, textvariable=self.calle_var,font = fuente)
        self.entradaCalle.grid(column=1,row=8)
        self.entradaCalle.bind("<FocusIn>", self.foc_in_calle)
        self.entradaCalle.bind("<Return>", self.onEntCalle)

        self.lblEntreCalle=Label(self,text="Entre Calles",font = fuente,bg='lightgray').grid(column=0,row=9)

        self.entreCalle_var=StringVar()
        self.entreCalle_var.set("Ingrese las calles")
        self.entradaEntreCalle=Entry(self, width=40, textvariable=self.entreCalle_var,font = fuente)
        self.entradaEntreCalle.grid(column=1,row=9)
        self.entradaEntreCalle.bind("<FocusIn>", self.foc_in_entreCalle)
        self.entradaEntreCalle.bind("<Return>", self.onEntEntreCalle)

        self.lblNumero=Label(self,text="Número Casa",font = fuente,bg='lightgray').grid(column=0,row=10)

        self.numero_var=StringVar()
        self.numero_var.set("Ingrese el número")
        self.entradaNumero=Entry(self, width=40, textvariable=self.numero_var,font = fuente)
        self.entradaNumero.grid(column=1,row=10)
        self.entradaNumero.bind("<FocusIn>", self.foc_in_numero)
        self.entradaNumero.bind("<Return>", self.onEntNumero)

        self.lblOrientacion=Label(self,text="Orientación",font = fuente,bg='lightgray').grid(column=0,row=11)
        
        self.my_combobox_orientacion=tkk.Combobox(self,width=38,font = fuente,state="readonly")
        self.my_combobox_orientacion.grid(column=1,row=11)
        self.opciones=["Norte","Sur","Oeste","Este"]
        self.my_combobox_orientacion.set("Norte")
        self.my_combobox_orientacion['values']=self.opciones
        self.my_combobox_orientacion.bind("<Return>", self.onEntOrientacion)

        myFont = font.Font(family='Roboto', size='14')
        self.lblSeparador0=Label(self,text="          ",font = fuente,bg='lightgray').grid(column=1,row=12)
        self.lblSeparador1=Label(self,text="          ",font = fuente,bg='lightgray').grid(column=2,row=12)
        self.botonGuardar=Button(self, text='Guardar',font=myFont,command=self.onGuardarTienda).grid(column=1, row=13)
        self.botonSalir=Button(self, text='Salir',font=myFont,command=self.onSalir).grid(column=2, row=13)	
        for widget in self.winfo_children():
            widget.grid(padx=5, pady=2)

    def onSeleccionEstado(self,event):
        clave=0
        if self.my_combobox_estado.current()!=-1:
            clave=self.my_combobox_estado.current()
        estado=bd.Estado()
        estado=self.datoEst.__getitem__(clave)
        self.my_combobox_ciudad.config(state='readonly')
        self.nomCiu, self.datoCiu = tablaDirecciones.getCiudadesProcedure(estado.getClaveEst())
        self.my_combobox_ciudad.set(self.nomCiu[0])
        self.my_combobox_ciudad['values']=self.nomCiu
        self.onSeleccionCiudad

    def onSeleccionCiudad(self,event):
        clave=0
        if self.my_combobox_ciudad.current()!=-1:
            clave=self.my_combobox_ciudad.current()
        ciudad=bd.Ciudad()
        ciudad=self.datoCiu.__getitem__(clave)
        self.my_combobox_codigoPostal.config(state='readonly')
        self.nomCod, self.datoCod = tablaDirecciones.getCodigosPostalesProcedure(ciudad.getClaveCiu())
        self.my_combobox_codigoPostal.set(self.nomCod[0])
        self.my_combobox_codigoPostal['values']=self.nomCod
        self.onSeleccionCodigo

    def onSeleccionCodigo(self,event):
        clave=0
        if self.my_combobox_codigoPostal.current()!=-1:
            clave=self.my_combobox_codigoPostal.current()
        codigo=bd.CodigoPostal()
        codigo=self.datoCod.__getitem__(clave)
        self.my_combobox_colonia.config(state='readonly')
        self.nomCol, self.datoCol = tablaDirecciones.getColoniasProcedure(codigo.getClaveCod())
        self.my_combobox_colonia.set(self.nomCol[0])
        self.my_combobox_colonia['values']=self.nomCol
        self.onSeleccionColonia

    def onSeleccionColonia(self,event):
        clave=0
        if self.my_combobox_colonia.current()!=-1:
            clave=self.my_combobox_colonia.current()
        self.colonia=bd.Colonia()
        self.colonia=self.datoCol.__getitem__(clave)

    def onGuardarTienda(self):
        tienda = self.getDatos()
        if tienda!=None:
            tablaTiendas.agregarTiendaProcedure(tienda)
            if mb.askyesno(message="Se va a registrar una nueva tienda\n¿Desea continuar?", title="Agregar Tienda"):
                tablaTiendas.aceptarTiendaProcedure()
                mb.showinfo("Agregar Tienda","Tienda registrada con exito")
                self.reiniciarCajas()
            else:
                tablaTiendas.cancelarTiendaProcedure()

    def onSalir(self):
        self.destroy()

    def foc_in_num(self, * args):
        if self.numeroTelefonico_var.get()=="Ingrese el número telefonico":
            self.numeroTelefonico_var.set("")
            self.entradaNumeroTelefonico.focus()
    def foc_in_cor(self, * args):
        if self.correoElectronico_var.get()=="Ingrese el correo electronico":
            self.correoElectronico_var.set("")
            self.entradaCorreoElectronico.focus()
    def foc_in_calle(self, * args):
        if self.calle_var.get()=="Ingrese la calle":
            self.calle_var.set("")
            self.entradaCalle.focus()
    def foc_in_entreCalle(self, * args):
        if self.entreCalle_var.get()=="Ingrese las calles":
            self.entreCalle_var.set("")
            self.entradaEntreCalle.focus()
    def foc_in_numero(self, * args):
        if self.numero_var.get()=="Ingrese el número":
            self.numero_var.set("")
            self.entradaNumero.focus()

    def onEntNum(self,event):
        self.entradaCorreoElectronico.focus()
    def onEntCorreo(self,event):
        self.my_combobox_estado.focus()
    def onEntCodigo(self,event):
        self.onSeleccionCodigo('<<ComboboxSelected>>')
        self.my_combobox_colonia.focus()
    def onEntEstado(self,event):
        self.onSeleccionEstado('<<ComboboxSelected>>')
        self.my_combobox_ciudad.focus()
    def onEntCiudad(self,event):
        self.onSeleccionCiudad('<<ComboboxSelected>>')
        self.my_combobox_codigoPostal.focus()
    def onEntColonia(self,event):
        self.onSeleccionColonia('<<ComboboxSelected>>')
        self.entradaCalle.focus()
    def onEntCalle(self,event):
        self.entradaEntreCalle.focus()
    def onEntEntreCalle(self,event):
        self.entradaNumero.focus()
    def onEntNumero(self,event):
        self.my_combobox_orientacion.focus()
    def onEntOrientacion(self,event):
        self.onGuardarTienda()

    def reiniciarCajas(self):
        fecha=datetime.now()
        año=fecha.year
        mes=fecha.month
        dia=fecha.day
        self.fechaApertura.set_date(date=date(año,mes,dia))
        self.numeroTelefonico_var.set("")
        self.correoElectronico_var.set("Ingrese el correo electronico")
        self.my_combobox_estado.set(self.nomEst[0])
        self.my_combobox_ciudad.configure(state=tkinter.DISABLED)
        self.my_combobox_ciudad.set("")
        self.my_combobox_codigoPostal.configure(state=tkinter.DISABLED)
        self.my_combobox_codigoPostal.set("")
        self.my_combobox_colonia.configure(state=tkinter.DISABLED)
        self.my_combobox_colonia.set("")
        self.calle_var.set("Ingrese la calle")
        self.entreCalle_var.set("Ingrese las calles")
        self.numero_var.set("Ingrese el número")
        self.my_combobox_orientacion.set("Norte")
        self.entradaNumeroTelefonico.focus()

    def validarVacios(self):
        if self.entradaNumeroTelefonico.get()=="" or self.entradaNumeroTelefonico.get()=="Ingrese el número telefonico":
            return False,2," ya que no puede quedar vacio"
        elif self.entradaCorreoElectronico.get()=="" or self.entradaCorreoElectronico.get()=="Ingrese el correo electronico":
            return False,3," ya que no puede quedar vacio"
        elif self.entradaCalle.get()=="" or self.entradaCalle.get()=="Ingrese la calle":
            return False,8," ya que no puede quedar vacio"
        elif self.entradaEntreCalle.get()=="" or self.entradaEntreCalle.get()=="Ingrese las calles":
            return False,9," ya que no puede quedar vacio"
        elif self.entradaNumero.get()=="" or self.entradaNumero.get()=="Ingrese el número":
            return False,10," ya que no puede quedar vacio"

        fecha=datetime.now()
        año=fecha.year
        mes=fecha.month
        dia=fecha.day
        fecha=str(año)
        if mes<10:
            fecha+="-0"+str(mes)
        else:
            fecha+="-"+str(mes)
        if dia<10:
            fecha+="-0"+str(dia)
        else:
            fecha+="-"+str(dia)
        if str(self.fechaApertura.get_date())==fecha:
            if not mb.askyesno(message="La fecha de apertura no ha sido modificada \n¿Desea continuar?", title="Agregar Tienda"):
                return False,0,""
        
        try:
            self.colonia.getClaveCol()
            return True,-1,""
        except:
            return False,7," no hay colonia seleccionada"

    def getDatos(self):
        valido,campo,error=self.validarVacios()
        if valido:
            tienda=bd.Tienda()
            tienda.setClaveTie(None)
            tienda.setFaperturaTie(self.fechaApertura.get_date())
            tienda.setCalleTie(self.entradaCalle.get())
            tienda.setNumDomTie(self.entradaNumero.get())
            tienda.setOrientacionTie(self.my_combobox_orientacion.get())
            tienda.setEntreCallesTie(self.entradaEntreCalle.get())
            tienda.setTelefonoTie(self.entradaNumeroTelefonico.get())
            tienda.setMailTie(self.entradaCorreoElectronico.get())
            tienda.setClaveCol(self.colonia.getClaveCol())
            return tienda
        else:
            if campo!=0:
                mb.showinfo("Agregar Tienda","Error el campo "+str(campo)+str(error))
            return None

#LISTAR LAS TIENDAS QUE HAY
class PanelListarTiendas(Frame):

    def __init__(self, container):
        super().__init__(container)
        self.config(background='lightgray')
        self.columnconfigure(0,weight=1)
        self.columnconfigure(0,weight=3)
        self.container=container
        setContainer(container)
        self.__create_widgets()
        self.crearTabla()
    
    def __create_widgets(self):
        fuente= "Helvetica 12 "
        self.botonSalir=Button(self, text='Salir', font=fuente, command=self.onSalir).grid(column=1, row=3)

        for widget in self.winfo_children():
            widget.grid(padx=5, pady=5)

    def crearTabla(self):
        self.tabla=Treeview(self)
        self.tabla['columns'] = ("Telefono","Correo electronico","C.Empleados","C.Vehiculos","Domicilio")
        self.tabla.column('#0', width=50,anchor=CENTER)
        self.tabla.column('Telefono', width=75,anchor=CENTER)
        self.tabla.column('Correo electronico', width=100,anchor=CENTER)
        self.tabla.column('C.Empleados', width=100,anchor=CENTER)
        self.tabla.column('C.Vehiculos', width=75,anchor=CENTER)
        self.tabla.column('Domicilio', width=350,anchor=CENTER)
        self.tabla.heading('#0',text='Clave Tienda',anchor=CENTER)
        self.tabla.heading('Telefono',text='Telefono',anchor=CENTER)
        self.tabla.heading('Correo electronico',text='Correo electronico',anchor=CENTER)
        self.tabla.heading('C.Empleados',text='C.Empleados',anchor=CENTER)
        self.tabla.heading('C.Vehiculos',text='C.Vehiculos',anchor=CENTER)
        self.tabla.heading('Domicilio',text='Domicilio',anchor=CENTER)
        self.tabla.grid(column=1,row=0,ipadx=265,ipady=180)
        self.agregarDatos()
        return self.tabla

    def agregarDatos(self):
        self.onLimpiarTabla()
        count=0
        tiendas=tablaTiendas.listarTiendasProcedure()
        for tienda in tiendas:
            domicilio=tienda.parteDomicilio()
            domicilio,clave=tablaDirecciones.getColonia(domicilio,tienda.getClaveCol())
            domicilio,clave=tablaDirecciones.getCodigoPostal(domicilio,clave)
            domicilio,clave=tablaDirecciones.getCiudad(domicilio,clave)
            domicilio=tablaDirecciones.getEstado(domicilio,clave)
            self.tabla.insert(parent='',index='end',iid=count, text=tienda.getClaveTie(),
                values=(tienda.getTelefonoTie(),tienda.getMailTie(),tablaTiendas.getCantidadEmProcedure(tienda.getClaveTie()),tablaTiendas.getCantidadVhProcedure(tienda.getClaveTie()),domicilio))
            count += 1

    def onLimpiarTabla(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
    
    def onSalir(self):
        for conElement in self.container.winfo_children():
            if not isinstance(conElement,Menu):
                conElement.destroy()

#REGISTRAR EMPLEADOS
class PanelRegistroEmpleados(Frame):
    def __init__(self, container):
        super().__init__(container)
        self.config(bg='lightgray')
        self.columnconfigure(0,weight=1)
        self.columnconfigure(0,weight=3)
        setContainer(container)
        self.__create_widgets()

    def __create_widgets(self):
        fuente= "Helvetica 12 "
        self.lblDatos=Label(self,text="DATOS PERSONALES",font = fuente,bg='lightgray').grid(column=1,row=0)

        self.lblCurp=Label(self,text="CURP",font=fuente,bg='lightgray').grid(column=0,row=1)

        self.curp_var=StringVar()
        self.curp_var.set("")
        self.entradaCurp=Entry(self, width=40, textvariable=self.curp_var,font=fuente)
        self.entradaCurp.grid(column=1,row=1)
        #self.entradaNombre.bind("<FocusIn>", self.foc_in_no)
        self.entradaCurp.focus()
        self.entradaCurp.bind("<Return>", self.onEntCurp)

        self.lblNombre=Label(self,text="Nombre",font=fuente,bg='lightgray').grid(column=0,row=2)

        self.nombre_var=StringVar()
        self.nombre_var.set("Ingrese el nombre")
        self.entradaNombre=Entry(self, width=40, textvariable=self.nombre_var,font=fuente,takefocus=False)
        self.entradaNombre.grid(column=1,row=2)
        self.entradaNombre.bind("<FocusIn>", self.foc_in_no)
        #self.entradaNombre.focus()
        self.entradaNombre.bind("<Return>", self.onEntNombre)
        
        self.lblApellidoPaterno=Label(self,text="Apellido Paterno",font=fuente,bg='lightgray').grid(column=0,row=3)

        self.apellidoPaterno_var=StringVar()
        self.apellidoPaterno_var.set("Ingrese el apellido paterno")
        self.entradaApellidoPaterno=Entry(self, width=40, textvariable=self.apellidoPaterno_var,font=fuente)
        self.entradaApellidoPaterno.grid(column=1,row=3)
        self.entradaApellidoPaterno.bind("<FocusIn>", self.foc_in_ap)
        self.entradaApellidoPaterno.bind("<Return>", self.onEntAP)
        
        self.lblApellidoMaterno=Label(self,text="Apellido Materno",font = fuente,bg='lightgray').grid(column=0,row=4)

        self.apellidoMaterno_var=StringVar()
        self.apellidoMaterno_var.set("Ingrese el apellido materno")
        self.entradaApellidoMaterno=Entry(self, width=40, textvariable=self.apellidoMaterno_var,font = fuente)
        self.entradaApellidoMaterno.grid(column=1,row=4)
        self.entradaApellidoMaterno.bind("<FocusIn>", self.foc_in_am)
        self.entradaApellidoMaterno.bind("<Return>", self.onEntAM)

        self.lblGenero=Label(self,text="Seleccione el género",font = fuente,bg='lightgray').grid(column=0,row=5)
        
        self.my_combobox_genero=tkk.Combobox(self,width=38,font = fuente,state="readonly")
        self.my_combobox_genero.grid(column=1,row=5)
        self.opciones=["Masculino","Femenino"]
        self.my_combobox_genero.set("Masculino")
        self.my_combobox_genero['values']=self.opciones
        #print(self.my_combobox_genero.current())
        self.my_combobox_genero.bind("<Return>", self.onEntCaja)

        self.lblFechaNacimiento=Label(self,text="Fecha de nacimiento",font = fuente,bg='lightgray').grid(column=0,row=6)
        fecha=datetime.now()
        año=fecha.year-18
        #self.fechaNacimiento1 = Calendar(self, year=año, month=1, day=1).grid(column=1, row=6)
        #self.frame = Frame().grid(column=1, row=6)
        self.fechaNacimiento = DateEntry(self,year=año,month=1,day=1, width=57)
        self.fechaNacimiento.grid(column=1, row=6)

        self.lblNumeroTelefonico=Label(self,text="Número telefonico",font = fuente,bg='lightgray').grid(column=0,row=7)

        self.numeroTelefonico_var=StringVar()
        self.numeroTelefonico_var.set("Ingrese el número telefonico")
        self.entradaNumeroTelefonico=Entry(self, width=40, textvariable=self.numeroTelefonico_var,font = fuente)
        self.entradaNumeroTelefonico.grid(column=1,row=7)
        self.entradaNumeroTelefonico.bind("<FocusIn>", self.foc_in_num)
        self.entradaNumeroTelefonico.bind("<Return>", self.onEntNum)

        self.lblCorreoElectronico=Label(self,text="Correo electronico",font = fuente,bg='lightgray').grid(column=0,row=8)

        self.correoElectronico_var=StringVar()
        self.correoElectronico_var.set("Ingrese el correo electronico")
        self.entradaCorreoElectronico=Entry(self, width=40, textvariable=self.correoElectronico_var,font = fuente)
        self.entradaCorreoElectronico.grid(column=1,row=8)
        self.entradaCorreoElectronico.bind("<FocusIn>", self.foc_in_cor)
        self.entradaCorreoElectronico.bind("<Return>", self.onEntCorreo)

        self.lblEstadoCivil=Label(self,text="Estado Civil",font = fuente,bg='lightgray').grid(column=0,row=9)

        self.estadoCivil_var=StringVar()
        self.estadoCivil_var.set("Ingrese el estado civil")
        self.entradaEstadoCivil=Entry(self, width=40, textvariable=self.estadoCivil_var,font = fuente)
        self.entradaEstadoCivil.grid(column=1,row=9)
        self.entradaEstadoCivil.bind("<FocusIn>", self.foc_in_edoci)
        self.entradaEstadoCivil.bind("<Return>", self.onEntEstadoCivil)

        self.lblDomicilio=Label(self,text="DATOS DOMICILIO",font = fuente,bg='lightgray').grid(column=1,row=10)

        self.lblEstado=Label(self,text="Estado",font = fuente,bg='lightgray').grid(column=0,row=11)

        self.my_combobox_estado=tkk.Combobox(self,width=38,font = fuente,state="readonly")
        self.my_combobox_estado.grid(column=1,row=11)
        self.nomEst, self.datoEst = tablaDirecciones.getEstadosProcedure()
        self.my_combobox_estado.set(self.nomEst[0])
        self.my_combobox_estado['values']=self.nomEst
        self.my_combobox_estado.bind("<<ComboboxSelected>>", self.onSeleccionEstado)
        self.my_combobox_estado.bind("<Return>", self.onEntEstado)

        self.lblCiudad=Label(self,text="Ciudad",font = fuente,bg='lightgray').grid(column=0,row=12)

        self.my_combobox_ciudad=tkk.Combobox(self,width=38,font = fuente,state=tkinter.DISABLED)
        self.my_combobox_ciudad.grid(column=1,row=12)
        self.my_combobox_ciudad.bind("<<ComboboxSelected>>", self.onSeleccionCiudad)
        self.my_combobox_ciudad.bind("<Return>", self.onEntCiudad)

        self.lblCodigoPostal=Label(self,text="Codigo postal",font = fuente,bg='lightgray').grid(column=0,row=13)

        self.my_combobox_codigoPostal=tkk.Combobox(self,width=38,font = fuente,state=tkinter.DISABLED)
        self.my_combobox_codigoPostal.grid(column=1,row=13)
        self.my_combobox_codigoPostal.bind("<<ComboboxSelected>>", self.onSeleccionCodigo)
        self.my_combobox_codigoPostal.bind("<Return>", self.onEntCodigo)

        self.lblColonia=Label(self,text="Colonia",font = fuente,bg='lightgray').grid(column=0,row=14)

        self.my_combobox_colonia=tkk.Combobox(self,width=38,font = fuente,state=tkinter.DISABLED)
        self.my_combobox_colonia.grid(column=1,row=14)
        self.my_combobox_colonia.bind("<<ComboboxSelected>>", self.onSeleccionColonia)
        self.my_combobox_colonia.bind("<Return>", self.onEntColonia)

        self.lblCalle=Label(self,text="Calle",font = fuente,bg='lightgray').grid(column=0,row=15)

        self.calle_var=StringVar()
        self.calle_var.set("Ingrese la calle")
        self.entradaCalle=Entry(self, width=40, textvariable=self.calle_var,font = fuente)
        self.entradaCalle.grid(column=1,row=15)
        self.entradaCalle.bind("<FocusIn>", self.foc_in_calle)
        self.entradaCalle.bind("<Return>", self.onEntCalle)

        self.lblEntreCalle=Label(self,text="Entre Calles",font = fuente,bg='lightgray').grid(column=0,row=16)

        self.entreCalle_var=StringVar()
        self.entreCalle_var.set("Ingrese las calles")
        self.entradaEntreCalle=Entry(self, width=40, textvariable=self.entreCalle_var,font = fuente)
        self.entradaEntreCalle.grid(column=1,row=16)
        self.entradaEntreCalle.bind("<FocusIn>", self.foc_in_entreCalle)
        self.entradaEntreCalle.bind("<Return>", self.onEntEntreCalle)

        self.lblNumero=Label(self,text="Número Casa",font = fuente,bg='lightgray').grid(column=0,row=17)

        self.numero_var=StringVar()
        self.numero_var.set("Ingrese el número")
        self.entradaNumero=Entry(self, width=40, textvariable=self.numero_var,font = fuente)
        self.entradaNumero.grid(column=1,row=17)
        self.entradaNumero.bind("<FocusIn>", self.foc_in_numero)
        self.entradaNumero.bind("<Return>", self.onEntNumero)

        self.lblOrientacion=Label(self,text="Orientación",font = fuente,bg='lightgray').grid(column=0,row=18)
        
        self.my_combobox_orientacion=tkk.Combobox(self,width=38,font = fuente,state="readonly")
        self.my_combobox_orientacion.grid(column=1,row=18)
        self.opciones=["Norte","Sur","Oeste","Este"]
        self.my_combobox_orientacion.set("Norte")
        self.my_combobox_orientacion['values']=self.opciones
        self.my_combobox_orientacion.bind("<Return>", self.onEntOrientacion)

        #self.lblSeparador=Label(self,text="     ",font = fuente,bg='lightgray').grid(column=0,row=18)
        #self.lblFechas=Label(self,text="FECHAS A ESCOJER",font = fuente,bg='lightgray').grid(column=1,row=19)
        #self.cal1=DateEntry(self,selectmode='day', width=27)
        #self.cal1.grid(column=0,row=20)
        #self.cal2=DateEntry(self,selectmode='day', width=27)
        #self.cal3=DateEntry(self,selectmode='day', width=27)

        self.lblNumero=Label(self,text="DATOS DEL CONTRATO",font = fuente,bg='lightgray').grid(column=3,row=0)

        self.lblFechaInicio=Label(self,text="Fecha inicio",font = fuente,bg='lightgray').grid(column=2,row=1)
        self.fechaInicio=DateEntry(self,selectmode='day', width=27)
        self.fechaInicio.grid(column=3, row=1)

        self.lblFechaFin=Label(self,text="Fecha fin",font = fuente,bg='lightgray').grid(column=2,row=2)
        self.fechaFin=DateEntry(self,selectmode='day', width=27)
        self.fechaFin.grid(column=3, row=2)

        self.lblPuesto=Label(self,text="Puesto",font = fuente,bg='lightgray').grid(column=2,row=3)

        self.puesto_var=StringVar()
        self.puesto_var.set("Ingrese el puesto que va a ocupar")
        self.entradaPuesto=Entry(self, width=20, textvariable=self.puesto_var,font = fuente)
        self.entradaPuesto.grid(column=3,row=3)
        self.entradaPuesto.bind("<FocusIn>", self.foc_in_puesto)
        self.entradaPuesto.bind("<Return>", self.onEntPuesto)

        self.lblSueldo=Label(self,text="Sueldo",font = fuente,bg='lightgray').grid(column=2,row=4)

        self.sueldo_var=StringVar()
        self.sueldo_var.set("Ingrese el sueldo a percibir")
        self.entradaSueldo=Entry(self, width=20, textvariable=self.sueldo_var,font = fuente)
        self.entradaSueldo.grid(column=3,row=4)
        self.entradaSueldo.bind("<FocusIn>", self.foc_in_sueldo)
        self.entradaSueldo.bind("<Return>", self.onEntSueldo)

        self.lblPeriodoSueldo=Label(self,text="Periodo sueldo",font = fuente,bg='lightgray').grid(column=2,row=5)
        
        self.my_combobox_periodoSueldo=tkk.Combobox(self,width=18,font = fuente,state="readonly")
        self.my_combobox_periodoSueldo.grid(column=3,row=5)
        self.opcionesPeriodo=["Diario","Semanal","Quincenal","Mensual","Bimestral","Anual"]
        self.my_combobox_periodoSueldo.set("Quincenal")
        self.my_combobox_periodoSueldo['values']=self.opcionesPeriodo
        self.my_combobox_periodoSueldo.bind("<Return>", self.onEntPeriodoSueldo)

        self.lblHoraInicioComida=Label(self,text="Hora Inicio Comida",font = fuente,bg='lightgray').grid(column=2,row=6)

        self.my_combobox_horaInicioComida=tkk.Combobox(self,width=18,font = fuente,state="readonly")
        self.my_combobox_horaInicioComida.grid(column=3,row=6)
        self.opcionesInicio=["11","12","13","14","15","16","17","18","19"]
        self.my_combobox_horaInicioComida.set(self.opcionesInicio[0])
        self.my_combobox_horaInicioComida['values']=self.opcionesInicio
        self.my_combobox_horaInicioComida.bind("<<ComboboxSelected>>", self.onCalcularHora)
        self.my_combobox_horaInicioComida.bind("<Return>", self.onEntHoraInicioCom)

        self.my_combobox_horaInicioComida2=tkk.Combobox(self,width=9,font = fuente,state="readonly")
        self.my_combobox_horaInicioComida2.grid(column=4,row=6)
        self.opcionesInicio2=["00","10","20","30","40","50"]
        self.my_combobox_horaInicioComida2.set(self.opcionesInicio2[0])
        self.my_combobox_horaInicioComida2['values']=self.opcionesInicio2
        self.my_combobox_horaInicioComida2.bind("<<ComboboxSelected>>", self.onCalcularHora)
        self.my_combobox_horaInicioComida2.bind("<Return>", self.onEntHoraInicioCom2)
        
        self.lblHoraFinComida=Label(self,text="Hora Fin Comida",font = fuente,bg='lightgray').grid(column=2,row=7)

        self.horaFin_var=StringVar()
        self.horaFin_var.set("12:00")
        self.entradaHoraFin=Entry(self, width=20, textvariable=self.horaFin_var,font = fuente,state=tkinter.DISABLED)
        self.entradaHoraFin.grid(column=3,row=7)
        """
        self.my_combobox_horaFiComida=tkk.Combobox(self,width=18,font = fuente,state="readonly")
        self.my_combobox_horaFiComida.grid(column=3,row=7)
        self.opcionesFin=["11","12","13","14","15","16","17","18","19","20"]
        self.my_combobox_horaFiComida.set(self.opciones[1])
        self.my_combobox_horaFiComida['values']=self.opciones
        self.my_combobox_horaFiComida.bind("<Return>", self.onEntHoraFinCom)

        self.my_combobox_horaFiComida2=tkk.Combobox(self,width=9,font = fuente,state="readonly")
        self.my_combobox_horaFiComida2.grid(column=4,row=7)
        self.opcionesFin2=["00","10","20","30","40","50","60"]
        self.my_combobox_horaFiComida2.set(self.opciones[0])
        self.my_combobox_horaFiComida2['values']=self.opciones
        self.my_combobox_horaFiComida2.bind("<Return>", self.onEntHoraFinCom2)
        """
        self.lblTiendas=Label(self,text="Tiendas",font = fuente,bg='lightgray').grid(column=2,row=8)
        
        self.my_combobox_tiendas=tkk.Combobox(self,width=18,font = fuente,state="readonly")
        self.my_combobox_tiendas.grid(column=3,row=8)
        self.a, self.b = tablaTiendas.getTiendas()
        self.my_combobox_tiendas.set(self.a[0])
        self.my_combobox_tiendas['values']=self.a
        self.my_combobox_tiendas.bind("<Return>", self.onEntTiendas)

        self.lblSeparador0=Label(self,text="          ",font = fuente,bg='lightgray').grid(column=1,row=21)
        self.lblSeparador1=Label(self,text="          ",font = fuente,bg='lightgray').grid(column=2,row=21)
        myFont = font.Font(family='Roboto', size='14')
        self.botonGuardar=Button(self, text='Guardar',font=myFont,command=self.onGuardarEmpleado).grid(column=1, row=22)
        self.botonSalir=Button(self, text='Salir',font=myFont,command=self.onSalir).grid(column=2, row=22)

        for widget in self.winfo_children():
            widget.grid(padx=5, pady=2)

    def onSeleccionEstado(self,event):
        clave=0
        if self.my_combobox_estado.current()!=-1:
            clave=self.my_combobox_estado.current()
        estado=bd.Estado()
        estado=self.datoEst.__getitem__(clave)
        self.my_combobox_ciudad.config(state='readonly')
        self.nomCiu, self.datoCiu = tablaDirecciones.getCiudadesProcedure(estado.getClaveEst())
        self.my_combobox_ciudad.set(self.nomCiu[0])
        self.my_combobox_ciudad['values']=self.nomCiu
        self.onSeleccionCiudad

    def onSeleccionCiudad(self,event):
        clave=0
        if self.my_combobox_ciudad.current()!=-1:
            clave=self.my_combobox_ciudad.current()
        ciudad=bd.Ciudad()
        ciudad=self.datoCiu.__getitem__(clave)
        self.my_combobox_codigoPostal.config(state='readonly')
        self.nomCod, self.datoCod = tablaDirecciones.getCodigosPostalesProcedure(ciudad.getClaveCiu())
        self.my_combobox_codigoPostal.set(self.nomCod[0])
        self.my_combobox_codigoPostal['values']=self.nomCod
        self.onSeleccionCodigo

    def onSeleccionCodigo(self,event):
        clave=0
        if self.my_combobox_codigoPostal.current()!=-1:
            clave=self.my_combobox_codigoPostal.current()
        codigo=bd.CodigoPostal()
        codigo=self.datoCod.__getitem__(clave)
        self.my_combobox_colonia.config(state='readonly')
        self.nomCol, self.datoCol = tablaDirecciones.getColoniasProcedure(codigo.getClaveCod())
        self.my_combobox_colonia.set(self.nomCol[0])
        self.my_combobox_colonia['values']=self.nomCol
        self.onSeleccionColonia

    def onSeleccionColonia(self,event):
        clave=0
        if self.my_combobox_colonia.current()!=-1:
            clave=self.my_combobox_colonia.current()
        self.colonia=bd.Colonia()
        self.colonia=self.datoCol.__getitem__(clave)

    def onCalcularHora(self,event):
        self.my_combobox_horaInicioComida2.config(state='readonly')
        hora = int(self.my_combobox_horaInicioComida.get())
        minutos= self.my_combobox_horaInicioComida2.get()

        cadena=""
        if hora!=19:
            hora+=1
            if minutos!="00":
                cadena=str(hora)+":"+minutos
            else:
                cadena=str(hora)+":00"
        else:
            self.my_combobox_horaInicioComida2.set(self.opcionesInicio2[0])
            self.my_combobox_horaInicioComida2.config(state=tkinter.DISABLED)
            cadena="20:00"
        self.horaFin_var.set(cadena)

    def onGuardarEmpleado(self):
        persona,contrato = self.getDatos()
        if persona!=None and contrato!=None:
            tablaEmpleados.agregarContratoProcedure(persona,contrato)
            if mb.askyesno(message="Se va a registrar un nuevo empleado\n¿Desea continuar?", title="Agregar Empleado"):
                tablaEmpleados.confirmarContratoProcedure()
                mb.showinfo("Agregar Empleado","Empleado registrado con exito")
                self.reiniciarCajas()
            else:
                tablaEmpleados.cancelarContratoProcedure()

    def onSalir(self):
        self.destroy()

    def foc_in_no(self, * args):
        if self.nombre_var.get()=="Ingrese el nombre":
            self.nombre_var.set("")
            self.entradaNombre.focus()
    def foc_in_ap(self, * args):
        if self.apellidoPaterno_var.get()=="Ingrese el apellido paterno":
            self.apellidoPaterno_var.set("")
            self.entradaApellidoPaterno.focus()
    def foc_in_am(self, * args):
        if self.apellidoMaterno_var.get()=="Ingrese el apellido materno":
            self.apellidoMaterno_var.set("")
            self.entradaApellidoMaterno.focus()
    def foc_in_num(self, * args):
        if self.numeroTelefonico_var.get()=="Ingrese el número telefonico":
            self.numeroTelefonico_var.set("")
            self.entradaNumeroTelefonico.focus()
    def foc_in_cor(self, * args):
        if self.correoElectronico_var.get()=="Ingrese el correo electronico":
            self.correoElectronico_var.set("")
            self.entradaCorreoElectronico.focus()
    def foc_in_edoci(self, * args):
        if self.estadoCivil_var.get()=="Ingrese el estado civil":
            self.estadoCivil_var.set("")
            self.entradaEstadoCivil.focus()
    def foc_in_calle(self, * args):
        if self.calle_var.get()=="Ingrese la calle":
            self.calle_var.set("")
            self.entradaCalle.focus()
    def foc_in_entreCalle(self, * args):
        if self.entreCalle_var.get()=="Ingrese las calles":
            self.entreCalle_var.set("")
            self.entradaEntreCalle.focus()
    def foc_in_numero(self, * args):
        if self.numero_var.get()=="Ingrese el número":
            self.numero_var.set("")
            self.entradaNumero.focus()
    def foc_in_puesto(self, * args):
        if self.puesto_var.get()=="Ingrese el puesto que va a ocupar":
            self.puesto_var.set("")
    def foc_in_sueldo(self, * args):
        if self.sueldo_var.get()=="Ingrese el sueldo a percibir":
            self.sueldo_var.set("")

    def onEntCurp(self,event):
        if len(self.curp_var.get())>20:
            mb.showinfo(title="Error",message="El campo de la CURP exede los 20 caracteres")
        else:
            if len(self.curp_var.get())!=0:
                persona=tablaEmpleados.buscarPersonaCurpProcedure(self.curp_var.get())
                if persona!=None:
                    try:
                        mb.showinfo(title="Error de existencia",message=f"Ya existe una persona registrada con la CURP: '{persona.getCURPPer()}' ")
                    except:
                        self.entradaNombre.focus()
                else:
                    self.entradaNombre.focus()
            else:
                mb.showinfo(title="Error",message="La CURP no tiene caracteres aún")
    def onEntNombre(self,event):
        self.entradaApellidoPaterno.focus()
    def onEntAP(self,event):
        self.entradaApellidoMaterno.focus()
    def onEntAM(self,event):
        self.my_combobox_genero.focus()
    def onEntCaja(self,event):
        self.entradaNumeroTelefonico.focus()
    def onEntNum(self,event):
        self.entradaCorreoElectronico.focus()
    def onEntCorreo(self,event):
        self.entradaEstadoCivil.focus()
    def onEntEstadoCivil(self,event):
        self.my_combobox_estado.focus()
    def onEntCodigo(self,event):
        self.onSeleccionCodigo('<<ComboboxSelected>>')
        self.my_combobox_colonia.focus()
    def onEntEstado(self,event):
        self.onSeleccionEstado('<<ComboboxSelected>>')
        self.my_combobox_ciudad.focus()
    def onEntCiudad(self,event):
        self.onSeleccionCiudad('<<ComboboxSelected>>')
        self.my_combobox_codigoPostal.focus()
    def onEntColonia(self,event):
        self.onSeleccionColonia('<<ComboboxSelected>>')
        self.entradaCalle.focus()
    def onEntCalle(self,event):
        self.entradaEntreCalle.focus()
    def onEntEntreCalle(self,event):
        self.entradaNumero.focus()
    def onEntNumero(self,event):
        self.my_combobox_orientacion.focus()
    def onEntOrientacion(self,event):
        self.entradaPuesto.focus()
    def onEntPuesto(self,event):
        self.entradaSueldo.focus()
    def onEntSueldo(self,event):
        self.my_combobox_periodoSueldo.focus()
    def onEntPeriodoSueldo(self,event):
        self.onCalcularHora('<<ComboboxSelected>>')
        self.my_combobox_horaInicioComida.focus()
    def onEntHoraInicioCom(self,event):
        self.onCalcularHora('<<ComboboxSelected>>')
        self.my_combobox_horaInicioComida2.focus()
    def onEntHoraInicioCom2(self,event):
        self.my_combobox_tiendas.focus()
    def onEntTiendas(self,event):
        self.onGuardarEmpleado()

    def convertirFecha(self,fecha):
        x = str(fecha)
        numero=""
        numeros=[]
        for i in x:
            if i=="-":
                numeros.append(numero)
                numero=""
            else:
                numero+=i
        numeros.append(numero)
        return numeros
    def validarCurp(self):
        if len(self.curp_var.get())>20:
            mb.showinfo(title="Error",message="El campo de la CURP exede los 20 caracteres")
            return False
        else:
            persona=tablaEmpleados.buscarPersonaCurpProcedure(self.curp_var.get())
            print()
            if persona!=None:
                try:
                    mb.showinfo(title="Error de existencia",message=f"Ya existe una persona registrada con la CURP: '{persona.getCURPPer()}' ")
                    return False
                except:
                    return True
            else:
                return True

    def validarVacios(self):
        num1=self.convertirFecha(self.fechaInicio.get_date())
        num2=self.convertirFecha(self.fechaFin.get_date())
        fechaInicio=date(int(num1[0]),int(num1[1]),int(num1[2]))
        fechaFin=date(int(num2[0]),int(num2[1]),int(num2[2]))
        fecha=datetime.now()
        año=fecha.year
        mes=fecha.month
        dia=fecha.day
        fech=str(año-18)+"-01-01"
        fech1=str(año)+str(mes)+str(dia)
        
        if self.entradaCurp.get()=="":
            return False,1," ya que no puede quedar vacio"
        else:
            x=self.validarCurp()
            if not x:
                return False,0,""
        if self.entradaNombre.get()=="" or self.entradaNombre.get()=="Ingrese el nombre":
            return False,2," ya que no puede quedar vacio"
        elif self.entradaApellidoPaterno.get()=="" or self.entradaApellidoPaterno.get()=="Ingrese el apellido paterno":
            return False,3
        elif self.entradaApellidoMaterno.get()=="" or self.entradaApellidoMaterno.get()=="Ingrese el apellido materno":
            return False,4," ya que no puede quedar vacio"
        elif str(self.fechaNacimiento.get_date())==fech:
            if not mb.askyesno(message="La fecha de nacimiento no ha sido modificada \n¿Desea continuar?", title="Agregar Empleado"):
                    return False,0,""
        elif self.entradaNumeroTelefonico.get()=="" or self.entradaNumeroTelefonico.get()=="Ingrese el número telefonico":
            return False,7," ya que no puede quedar vacio"
        elif self.entradaCorreoElectronico.get()=="" or self.entradaCorreoElectronico.get()=="Ingrese el correo electronico":
            return False,8," ya que no puede quedar vacio"
        elif self.entradaEstadoCivil.get()=="" or self.entradaEstadoCivil.get()=="Ingrese el estado civil":
            return False,9," ya que no puede quedar vacio"
        elif self.entradaCalle.get()=="" or self.entradaCalle.get()=="Ingrese la calle":
            return False,14," ya que no puede quedar vacio"
        elif self.entradaEntreCalle.get()=="" or self.entradaEntreCalle.get()=="Ingrese las calles":
            return False,15," ya que no puede quedar vacio"
        elif self.entradaNumero.get()=="" or self.entradaNumero.get()=="Ingrese el número":
            return False,16," ya que no puede quedar vacio"
        elif self.entradaPuesto.get()=="" or self.entradaPuesto.get()=="Ingrese el puesto que va a ocupar":
            return False,20," ya que no puede quedar vacio"
        elif self.entradaSueldo.get()=="" or self.entradaSueldo.get()=="Ingrese el sueldo a percibir":
            return False,21," ya que no puede quedar vacio"
        
        if str(self.fechaFin.get_date())==fech1:
                mb.showinfo(title="Agregar Empleado",message=f"La fecha de fin del contrato no ha sido modificada")
                return False,0,""
        else:
            if fechaFin<=fechaInicio:
                mb.showinfo(title="Agregar Empleado",message=f"La fecha de fin del contrato es menor que la de inicio")
                return False,0,""

        try:
            x = float(self.entradaSueldo.get())
            try:
                self.colonia.getClaveCol()
                return True,-1,""
            except:
                return False,21," no hay colonia seleccionada"
        except:
            return False,21," ya que no es una cantidad numerica"

    def reiniciarCajas(self): 
        self.curp_var.set("")
        self.nombre_var.set("Ingrese el nombre")
        self.apellidoPaterno_var.set("Ingrese el apellido paterno")
        self.apellidoMaterno_var.set("Ingrese el apellido materno")
        self.my_combobox_genero.set("Masculino")
        fecha=datetime.now()
        año=fecha.year
        mes=fecha.month
        dia=fecha.day
        self.fechaNacimiento.set_date(date=date((año-18),1,1))
        self.numeroTelefonico_var.set("Ingrese el número telefonico")
        self.correoElectronico_var.set("Ingrese el correo electronico")
        self.estadoCivil_var.set("Ingrese el estado civil")
        self.my_combobox_estado.set(self.nomEst[0])
        self.my_combobox_ciudad.configure(state=tkinter.DISABLED)
        self.my_combobox_ciudad.set("")
        self.my_combobox_codigoPostal.configure(state=tkinter.DISABLED)
        self.my_combobox_codigoPostal.set("")
        self.my_combobox_colonia.configure(state=tkinter.DISABLED)
        self.my_combobox_colonia.set("")
        self.calle_var.set("Ingrese la calle")
        self.entreCalle_var.set("Ingrese las calles")
        self.numero_var.set("Ingrese el número")
        self.my_combobox_orientacion.set("Norte")
        self.fechaInicio.set_date(date=date(año,mes,dia))
        self.fechaFin.set_date(date=date(año,mes,dia))
        self.puesto_var.set("Ingrese el puesto que va a ocupar")
        self.sueldo_var.set("Ingrese el sueldo a percibir")
        self.my_combobox_periodoSueldo.set("Quincenal")
        self.my_combobox_horaInicioComida.set("11")
        self.my_combobox_horaInicioComida2.set("00")
        self.horaFin_var.set("12:00")
        self.my_combobox_tiendas.set(self.a[0])

    def getDatos(self):
        valido,campo,error=self.validarVacios()
        if valido:
            persona=bd.Persona()
            contrato=bd.Contrato()
            persona.setClavePer(None)
            persona.setNomPer(self.entradaNombre.get())
            persona.setApPer(self.entradaApellidoPaterno.get())
            persona.setAmPer(self.entradaApellidoMaterno.get())
            persona.setCallePer(self.entradaCalle.get())
            persona.setNumDomPer(self.entradaNumero.get())
            persona.setOrientacionPer(self.my_combobox_orientacion.get())
            persona.setEntreCallesPer(self.entradaEntreCalle.get())
            persona.setTelefonoPer(self.entradaNumeroTelefonico.get())
            persona.setMailPer(self.entradaCorreoElectronico.get())
            persona.setSexoPer(self.my_combobox_genero.get())
            persona.setFnacimientoPer(self.fechaNacimiento.get_date())
            persona.setEdoCivilPer(self.entradaEstadoCivil.get())
            persona.setColPer(self.colonia.getClaveCol())
            persona.setCURPPer(self.entradaCurp.get())

            contrato.setClaveCon(None)
            contrato.setFechaInicioCon(self.fechaInicio.get_date())
            contrato.setFechaFinCon(self.fechaFin.get_date())
            contrato.setPuestoCon(self.entradaPuesto.get())
            contrato.setSueldoCon(self.entradaSueldo.get())
            contrato.setPeriodoSueldoCon(self.my_combobox_periodoSueldo.get())
            contrato.setHentradaCon("11:00:00")
            contrato.setHsalidaCon("20:00:00")
            contrato.setHIniComidaCon(str(self.my_combobox_horaInicioComida.get()+":"+self.my_combobox_horaInicioComida2.get()+":00"))
            contrato.setHFinComidaCon(str(self.entradaHoraFin.get()+":00"))
            contrato.setComisionesCon(0)
            tienda=self.b.__getitem__(self.my_combobox_tiendas.current())
            contrato.setClaveTie(tienda.getClaveTie())
            return persona,contrato
        else:
            if campo!=0:
                mb.showinfo("Agregar Empleado","Error el campo "+str(campo)+str(error))
            return None,None

#LISTAR CONTRATOS DE EMPLEADOS
class PanelListarEmpleados(Frame):
    def __init__(self, container):
        super().__init__(container)
        self.config(background='lightgray')
        self.columnconfigure(0,weight=1)
        self.columnconfigure(0,weight=3)
        self.container=container
        setContainer(container)
        self.__create_widgets()
        self.crearTabla()
    
    def __create_widgets(self):
        fuente= "Helvetica 12 "
        self.botonSalir=Button(self, text='Salir', font=fuente, command=self.onSalir).grid(column=1, row=2, padx=5, pady=5)

        for widget in self.winfo_children():
            widget.grid(padx=5, pady=5)

    def crearTabla(self):
        self.grid_rowconfigure(0,weight=1) 
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=0)
        self.grid_columnconfigure(1,weight=1)
        #self.grid_rowconfigure(2,weight=0) 
        #self.grid_columnconfigure(2,weight=1)
        #self.grid_rowconfigure(3,weight=1)
        #self.grid_rowconfigure(4,weight=0)
        self.tabla=Treeview(self)
        self.tabla['columns'] = ("Nombre","Puesto","Telefono","Correo electronico","Domicilio")
        self.tabla.column('#0', width=50,anchor=CENTER)
        self.tabla.column('Nombre', width=100,anchor=CENTER)
        self.tabla.column('Puesto', width=75,anchor=CENTER)
        self.tabla.column('Telefono', width=75,anchor=CENTER)
        self.tabla.column('Correo electronico', width=100,anchor=CENTER)
        self.tabla.column('Domicilio', width=350,anchor=CENTER)
        self.tabla.heading('#0',text='Folio Contrato',anchor=CENTER)
        self.tabla.heading('Nombre',text='Nombre',anchor=CENTER)
        self.tabla.heading('Puesto',text='Puesto',anchor=CENTER)
        self.tabla.heading('Telefono',text='Telefono',anchor=CENTER)
        self.tabla.heading('Correo electronico',text='Correo electronico',anchor=CENTER)
        self.tabla.heading('Domicilio',text='Domicilio',anchor=CENTER)

        self.xscroll = tk.Scrollbar(self, orient="horizontal", command=self.tabla.xview)
        self.yscroll = tk.Scrollbar(self, orient="horizontal", command=self.tabla.yview)
        self.tabla.configure(xscrollcommand=self.xscroll.set, width=1150)
        #self.tabla.configure(yscrollcommand=self.yscroll.set)

        self.tabla.grid(column=0,row=0,sticky="nsew",padx=10, pady=10, columnspan=3)
        self.xscroll.grid(column=0, row=1, sticky="ew", columnspan=3)
        #self.yscroll.grid(column=1, row=0, sticky="ew", columnspan=3)
        self.agregarDatos()
        return self.tabla

    def agregarDatos(self):
        self.onLimpiarTabla()
        count=0
        contratos=tablaEmpleados.listarEmpleadosProcedure()
        for contrato in contratos:
            persona=tablaEmpleados.getPersonaProcedure(contrato.getClavePer())
            domicilio=persona.parteDomicilio()
            domicilio,clave=tablaDirecciones.getColonia(domicilio,persona.getColPer())
            domicilio,clave=tablaDirecciones.getCodigoPostal(domicilio,clave)
            domicilio,clave=tablaDirecciones.getCiudad(domicilio,clave)
            domicilio=tablaDirecciones.getEstado(domicilio,clave)
            self.tabla.insert(parent='',index='end',iid=count, text=contrato.getClaveCon(),
                values=(persona.salidaNombre(),contrato.getPuestoCon(),persona.getTelefonoPer(),persona.getMailPer(),domicilio))
            count += 1

    def onLimpiarTabla(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
    
    def onSalir(self):
        for conElement in self.container.winfo_children():
            if not isinstance(conElement,Menu):
                conElement.destroy()

#REGISTRAR PROVEEDORES
class PanelRegistroProveedores(Frame):
    def __init__(self, container):
        super().__init__(container)
        self.config(bg='lightgray')
        self.columnconfigure(0,weight=1)
        self.columnconfigure(0,weight=3)
        setContainer(container)
        self.__create_widgets()

    def __create_widgets(self):
        fuente= "Helvetica 12 "
        self.lblDatos=Label(self,text="DATOS DEL PROVEEDOR",font = fuente,bg='lightgray').grid(column=1,row=0)

        self.lblNombre=Label(self,text="Nombre Empresa",font=fuente,bg='lightgray').grid(column=0,row=1)

        self.nombre_var=StringVar()
        self.nombre_var.set("")
        self.entradaNombre=Entry(self, width=40, textvariable=self.nombre_var,font=fuente)
        self.entradaNombre.grid(column=1,row=1)
        self.entradaNombre.focus()
        self.entradaNombre.bind("<Return>", self.onEntNombre)

        self.lblNumeroTelefonico=Label(self,text="Número telefonico",font=fuente,bg='lightgray').grid(column=0,row=2)

        self.numeroTelefonico_var=StringVar()
        self.numeroTelefonico_var.set("Ingrese el número telefonico")
        self.entradaNumeroTelefonico=Entry(self, width=40, textvariable=self.numeroTelefonico_var,font = fuente)
        self.entradaNumeroTelefonico.grid(column=1,row=2)
        self.entradaNumeroTelefonico.bind("<FocusIn>", self.foc_in_num)
        self.entradaNumeroTelefonico.bind("<Return>", self.onEntNum)

        self.lblCorreoElectronico=Label(self,text="Correo electronico",font = fuente,bg='lightgray').grid(column=0,row=3)

        self.correoElectronico_var=StringVar()
        self.correoElectronico_var.set("Ingrese el correo electronico")
        self.entradaCorreoElectronico=Entry(self, width=40, textvariable=self.correoElectronico_var,font = fuente)
        self.entradaCorreoElectronico.grid(column=1,row=3)
        self.entradaCorreoElectronico.bind("<FocusIn>", self.foc_in_cor)
        self.entradaCorreoElectronico.bind("<Return>", self.onEntCorreo)

        self.lblEstado=Label(self,text="Estado",font = fuente,bg='lightgray').grid(column=0,row=4)

        self.my_combobox_estado=tkk.Combobox(self,width=38,font = fuente,state="readonly")
        self.my_combobox_estado.grid(column=1,row=4)
        self.nomEst, self.datoEst = tablaDirecciones.getEstadosProcedure()
        self.my_combobox_estado.set(self.nomEst[0])
        self.my_combobox_estado['values']=self.nomEst
        self.my_combobox_estado.bind("<<ComboboxSelected>>", self.onSeleccionEstado)
        self.my_combobox_estado.bind("<Return>", self.onEntEstado)

        self.lblCiudad=Label(self,text="Ciudad",font = fuente,bg='lightgray').grid(column=0,row=5)

        self.my_combobox_ciudad=tkk.Combobox(self,width=38,font = fuente,state=tkinter.DISABLED)
        self.my_combobox_ciudad.grid(column=1,row=5)
        self.my_combobox_ciudad.bind("<<ComboboxSelected>>", self.onSeleccionCiudad)
        self.my_combobox_ciudad.bind("<Return>", self.onEntCiudad)

        self.lblCodigoPostal=Label(self,text="Codigo postal",font = fuente,bg='lightgray').grid(column=0,row=6)

        self.my_combobox_codigoPostal=tkk.Combobox(self,width=38,font = fuente,state=tkinter.DISABLED)
        self.my_combobox_codigoPostal.grid(column=1,row=6)
        self.my_combobox_codigoPostal.bind("<<ComboboxSelected>>", self.onSeleccionCodigo)
        self.my_combobox_codigoPostal.bind("<Return>", self.onEntCodigo)

        self.lblColonia=Label(self,text="Colonia",font = fuente,bg='lightgray').grid(column=0,row=7)

        self.my_combobox_colonia=tkk.Combobox(self,width=38,font = fuente,state=tkinter.DISABLED)
        self.my_combobox_colonia.grid(column=1,row=7)
        self.my_combobox_colonia.bind("<<ComboboxSelected>>", self.onSeleccionColonia)
        self.my_combobox_colonia.bind("<Return>", self.onEntColonia)

        self.lblCalle=Label(self,text="Calle",font = fuente,bg='lightgray').grid(column=0,row=8)

        self.calle_var=StringVar()
        self.calle_var.set("Ingrese la calle")
        self.entradaCalle=Entry(self, width=40, textvariable=self.calle_var,font = fuente)
        self.entradaCalle.grid(column=1,row=8)
        self.entradaCalle.bind("<FocusIn>", self.foc_in_calle)
        self.entradaCalle.bind("<Return>", self.onEntCalle)

        self.lblEntreCalle=Label(self,text="Entre Calles",font = fuente,bg='lightgray').grid(column=0,row=9)

        self.entreCalle_var=StringVar()
        self.entreCalle_var.set("Ingrese las calles")
        self.entradaEntreCalle=Entry(self, width=40, textvariable=self.entreCalle_var,font = fuente)
        self.entradaEntreCalle.grid(column=1,row=9)
        self.entradaEntreCalle.bind("<FocusIn>", self.foc_in_entreCalle)
        self.entradaEntreCalle.bind("<Return>", self.onEntEntreCalle)

        self.lblNumero=Label(self,text="Número Casa",font = fuente,bg='lightgray').grid(column=0,row=10)

        self.numero_var=StringVar()
        self.numero_var.set("Ingrese el número")
        self.entradaNumero=Entry(self, width=40, textvariable=self.numero_var,font = fuente)
        self.entradaNumero.grid(column=1,row=10)
        self.entradaNumero.bind("<FocusIn>", self.foc_in_numero)
        self.entradaNumero.bind("<Return>", self.onEntNumero)

        self.lblOrientacion=Label(self,text="Orientación",font = fuente,bg='lightgray').grid(column=0,row=11)
        
        self.my_combobox_orientacion=tkk.Combobox(self,width=38,font = fuente,state="readonly")
        self.my_combobox_orientacion.grid(column=1,row=11)
        self.opciones=["Norte","Sur","Oeste","Este"]
        self.my_combobox_orientacion.set("Norte")
        self.my_combobox_orientacion['values']=self.opciones
        self.my_combobox_orientacion.bind("<Return>", self.onEntOrientacion)

        self.lblDatos1=Label(self,text="DATOS DEL REPRESENTANTE",font = fuente,bg='lightgray').grid(column=3,row=0)

        self.lblCurp=Label(self,text="CURP",font=fuente,bg='lightgray').grid(column=2,row=1)

        self.curp_var=StringVar()
        self.curp_var.set("Ingrese la CURP")
        self.entradaCurp=Entry(self, width=40, textvariable=self.curp_var,font=fuente)
        self.entradaCurp.grid(column=3,row=1)
        self.entradaCurp.bind("<FocusIn>", self.foc_in_curp)
        self.entradaCurp.bind("<Return>", self.onEntCurp)

        self.lblNombrePer=Label(self,text="Nombre",font=fuente,bg='lightgray').grid(column=2,row=2)

        self.nombrePer_var=StringVar()
        self.nombrePer_var.set("Ingrese el nombre")
        self.entradaNombrePer=Entry(self, width=40, textvariable=self.nombrePer_var,font=fuente,takefocus=False)
        self.entradaNombrePer.grid(column=3,row=2)
        self.entradaNombrePer.bind("<FocusIn>", self.foc_in_no)
        self.entradaNombrePer.bind("<Return>", self.onEntNombrePer)
        
        self.lblApellidoPaterno=Label(self,text="Apellido Paterno",font=fuente,bg='lightgray').grid(column=2,row=3)

        self.apellidoPaterno_var=StringVar()
        self.apellidoPaterno_var.set("Ingrese el apellido paterno")
        self.entradaApellidoPaterno=Entry(self, width=40, textvariable=self.apellidoPaterno_var,font=fuente)
        self.entradaApellidoPaterno.grid(column=3,row=3)
        self.entradaApellidoPaterno.bind("<FocusIn>", self.foc_in_ap)
        self.entradaApellidoPaterno.bind("<Return>", self.onEntAP)
        
        self.lblApellidoMaterno=Label(self,text="Apellido Materno",font = fuente,bg='lightgray').grid(column=2,row=4)

        self.apellidoMaterno_var=StringVar()
        self.apellidoMaterno_var.set("Ingrese el apellido materno")
        self.entradaApellidoMaterno=Entry(self, width=40, textvariable=self.apellidoMaterno_var,font = fuente)
        self.entradaApellidoMaterno.grid(column=3,row=4)
        self.entradaApellidoMaterno.bind("<FocusIn>", self.foc_in_am)
        self.entradaApellidoMaterno.bind("<Return>", self.onEntAM)

        self.lblGenero=Label(self,text="Seleccione el género",font = fuente,bg='lightgray').grid(column=2,row=5)
        
        self.my_combobox_genero=tkk.Combobox(self,width=38,font = fuente,state="readonly")
        self.my_combobox_genero.grid(column=3,row=5)
        self.opciones=["Masculino","Femenino"]
        self.my_combobox_genero.set("Masculino")
        self.my_combobox_genero['values']=self.opciones
        #print(self.my_combobox_genero.current())
        self.my_combobox_genero.bind("<Return>", self.onEntCaja)

        self.lblFechaNacimiento=Label(self,text="Fecha de nacimiento",font = fuente,bg='lightgray').grid(column=2,row=6)
        fecha=datetime.now()
        año=fecha.year-18
        self.fechaNacimiento = DateEntry(self,year=año,month=1,day=1, width=57)
        self.fechaNacimiento.grid(column=3, row=6)

        self.lblNumeroTelefonico1=Label(self,text="Número telefonico",font = fuente,bg='lightgray').grid(column=2,row=7)

        self.numeroTelefonico1_var=StringVar()
        self.numeroTelefonico1_var.set("Ingrese el número telefonico")
        self.entradaNumeroTelefonico1=Entry(self, width=40, textvariable=self.numeroTelefonico1_var,font = fuente)
        self.entradaNumeroTelefonico1.grid(column=3,row=7)
        self.entradaNumeroTelefonico1.bind("<FocusIn>", self.foc_in_num1)
        self.entradaNumeroTelefonico1.bind("<Return>", self.onEntNum1)

        self.lblCorreoElectronico1=Label(self,text="Correo electronico",font = fuente,bg='lightgray').grid(column=2,row=8)

        self.correoElectronico1_var=StringVar()
        self.correoElectronico1_var.set("Ingrese el correo electronico")
        self.entradaCorreoElectronico1=Entry(self, width=40, textvariable=self.correoElectronico1_var,font = fuente)
        self.entradaCorreoElectronico1.grid(column=3,row=8)
        self.entradaCorreoElectronico1.bind("<FocusIn>", self.foc_in_cor1)
        self.entradaCorreoElectronico1.bind("<Return>", self.onEntCorreo1)

        self.lblEstadoCivil=Label(self,text="Estado Civil",font = fuente,bg='lightgray').grid(column=2,row=9)

        self.estadoCivil_var=StringVar()
        self.estadoCivil_var.set("Ingrese el estado civil")
        self.entradaEstadoCivil=Entry(self, width=40, textvariable=self.estadoCivil_var,font = fuente)
        self.entradaEstadoCivil.grid(column=3,row=9)
        self.entradaEstadoCivil.bind("<FocusIn>", self.foc_in_edoci)
        self.entradaEstadoCivil.bind("<Return>", self.onEntEstadoCivil)

        self.lblEstado1=Label(self,text="Estado",font = fuente,bg='lightgray').grid(column=2,row=10)

        self.my_combobox_estado1=tkk.Combobox(self,width=38,font = fuente,state="readonly")
        self.my_combobox_estado1.grid(column=3,row=10)
        self.nomEst1, self.datoEst1 = tablaDirecciones.getEstadosProcedure()
        self.my_combobox_estado1.set(self.nomEst1[0])
        self.my_combobox_estado1['values']=self.nomEst1
        self.my_combobox_estado1.bind("<<ComboboxSelected>>", self.onSeleccionEstado1)
        self.my_combobox_estado1.bind("<Return>", self.onEntEstado1)

        self.lblCiudad1=Label(self,text="Ciudad",font = fuente,bg='lightgray').grid(column=2,row=11)

        self.my_combobox_ciudad1=tkk.Combobox(self,width=38,font = fuente,state=tkinter.DISABLED)
        self.my_combobox_ciudad1.grid(column=3,row=11)
        self.my_combobox_ciudad1.bind("<<ComboboxSelected>>", self.onSeleccionCiudad1)
        self.my_combobox_ciudad1.bind("<Return>", self.onEntCiudad1)

        self.lblCodigoPostal1=Label(self,text="Codigo postal",font = fuente,bg='lightgray').grid(column=2,row=12)

        self.my_combobox_codigoPostal1=tkk.Combobox(self,width=38,font = fuente,state=tkinter.DISABLED)
        self.my_combobox_codigoPostal1.grid(column=3,row=12)
        self.my_combobox_codigoPostal1.bind("<<ComboboxSelected>>", self.onSeleccionCodigo1)
        self.my_combobox_codigoPostal1.bind("<Return>", self.onEntCodigo1)

        self.lblColonia1=Label(self,text="Colonia",font = fuente,bg='lightgray').grid(column=2,row=13)

        self.my_combobox_colonia1=tkk.Combobox(self,width=38,font = fuente,state=tkinter.DISABLED)
        self.my_combobox_colonia1.grid(column=3,row=13)
        self.my_combobox_colonia1.bind("<<ComboboxSelected>>", self.onSeleccionColonia1)
        self.my_combobox_colonia1.bind("<Return>", self.onEntColonia1)

        self.lblCalle1=Label(self,text="Calle",font = fuente,bg='lightgray').grid(column=2,row=14)

        self.calle1_var=StringVar()
        self.calle1_var.set("Ingrese la calle")
        self.entradaCalle1=Entry(self, width=40, textvariable=self.calle1_var,font = fuente)
        self.entradaCalle1.grid(column=3,row=14)
        self.entradaCalle1.bind("<FocusIn>", self.foc_in_calle1)
        self.entradaCalle1.bind("<Return>", self.onEntCalle1)

        self.lblEntreCalle1=Label(self,text="Entre Calles",font = fuente,bg='lightgray').grid(column=2,row=15)

        self.entreCalle1_var=StringVar()
        self.entreCalle1_var.set("Ingrese las calles")
        self.entradaEntreCalle1=Entry(self, width=40, textvariable=self.entreCalle1_var,font = fuente)
        self.entradaEntreCalle1.grid(column=3,row=15)
        self.entradaEntreCalle1.bind("<FocusIn>", self.foc_in_entreCalle1)
        self.entradaEntreCalle1.bind("<Return>", self.onEntEntreCalle1)

        self.lblNumero1=Label(self,text="Número Casa",font = fuente,bg='lightgray').grid(column=2,row=16)

        self.numero1_var=StringVar()
        self.numero1_var.set("Ingrese el número")
        self.entradaNumero1=Entry(self, width=40, textvariable=self.numero1_var,font = fuente)
        self.entradaNumero1.grid(column=3,row=16)
        self.entradaNumero1.bind("<FocusIn>", self.foc_in_numero1)
        self.entradaNumero1.bind("<Return>", self.onEntNumero1)

        self.lblOrientacion1=Label(self,text="Orientación",font = fuente,bg='lightgray').grid(column=2,row=17)
        
        self.my_combobox_orientacion1=tkk.Combobox(self,width=38,font = fuente,state="readonly")
        self.my_combobox_orientacion1.grid(column=3,row=17)
        self.opciones=["Norte","Sur","Oeste","Este"]
        self.my_combobox_orientacion1.set("Norte")
        self.my_combobox_orientacion1['values']=self.opciones
        self.my_combobox_orientacion1.bind("<Return>", self.onEntOrientacion1)

        self.lblSeparador0=Label(self,text="          ",font = fuente,bg='lightgray').grid(column=1,row=21)
        self.lblSeparador1=Label(self,text="          ",font = fuente,bg='lightgray').grid(column=2,row=21)
        myFont = font.Font(family='Roboto', size='14')
        self.botonGuardar=Button(self, text='Guardar',font=myFont,command=self.onGuardarProveedor).grid(column=1, row=22)
        self.botonSalir=Button(self, text='Salir',font=myFont,command=self.onSalir).grid(column=2, row=22)

        for widget in self.winfo_children():
            widget.grid(padx=5, pady=2)

    def onSeleccionEstado(self,event):
        clave=0
        if self.my_combobox_estado.current()!=-1:
            clave=self.my_combobox_estado.current()
        estado=bd.Estado()
        estado=self.datoEst.__getitem__(clave)
        self.my_combobox_ciudad.config(state='readonly')
        self.nomCiu, self.datoCiu = tablaDirecciones.getCiudadesProcedure(estado.getClaveEst())
        self.my_combobox_ciudad.set(self.nomCiu[0])
        self.my_combobox_ciudad['values']=self.nomCiu
        self.onSeleccionCiudad
    def onSeleccionCiudad(self,event):
        clave=0
        if self.my_combobox_ciudad.current()!=-1:
            clave=self.my_combobox_ciudad.current()
        ciudad=bd.Ciudad()
        ciudad=self.datoCiu.__getitem__(clave)
        self.my_combobox_codigoPostal.config(state='readonly')
        self.nomCod, self.datoCod = tablaDirecciones.getCodigosPostalesProcedure(ciudad.getClaveCiu())
        self.my_combobox_codigoPostal.set(self.nomCod[0])
        self.my_combobox_codigoPostal['values']=self.nomCod
        self.onSeleccionCodigo
    def onSeleccionCodigo(self,event):
        clave=0
        if self.my_combobox_codigoPostal.current()!=-1:
            clave=self.my_combobox_codigoPostal.current()
        codigo=bd.CodigoPostal()
        codigo=self.datoCod.__getitem__(clave)
        self.my_combobox_colonia.config(state='readonly')
        self.nomCol, self.datoCol = tablaDirecciones.getColoniasProcedure(codigo.getClaveCod())
        self.my_combobox_colonia.set(self.nomCol[0])
        self.my_combobox_colonia['values']=self.nomCol
        self.onSeleccionColonia
    def onSeleccionColonia(self,event):
        clave=0
        if self.my_combobox_colonia.current()!=-1:
            clave=self.my_combobox_colonia.current()
        self.colonia=bd.Colonia()
        self.colonia=self.datoCol.__getitem__(clave)

    def onSeleccionEstado1(self,event):
        clave=0
        if self.my_combobox_estado1.current()!=-1:
            clave=self.my_combobox_estado1.current()
        estado=bd.Estado()
        estado=self.datoEst1.__getitem__(clave)
        self.my_combobox_ciudad1.config(state='readonly')
        self.nomCiu1, self.datoCiu1 = tablaDirecciones.getCiudadesProcedure(estado.getClaveEst())
        self.my_combobox_ciudad1.set(self.nomCiu1[0])
        self.my_combobox_ciudad1['values']=self.nomCiu1
        self.onSeleccionCiudad1
    def onSeleccionCiudad1(self,event):
        clave=0
        if self.my_combobox_ciudad1.current()!=-1:
            clave=self.my_combobox_ciudad1.current()
        ciudad=bd.Ciudad()
        ciudad=self.datoCiu1.__getitem__(clave)
        self.my_combobox_codigoPostal1.config(state='readonly')
        self.nomCod1, self.datoCod1 = tablaDirecciones.getCodigosPostalesProcedure(ciudad.getClaveCiu())
        self.my_combobox_codigoPostal1.set(self.nomCod1[0])
        self.my_combobox_codigoPostal1['values']=self.nomCod1
        self.onSeleccionCodigo1
    def onSeleccionCodigo1(self,event):
        clave=0
        if self.my_combobox_codigoPostal1.current()!=-1:
            clave=self.my_combobox_codigoPostal1.current()
        codigo=bd.CodigoPostal()
        codigo=self.datoCod1.__getitem__(clave)
        self.my_combobox_colonia1.config(state='readonly')
        self.nomCol1, self.datoCol1 = tablaDirecciones.getColoniasProcedure(codigo.getClaveCod())
        self.my_combobox_colonia1.set(self.nomCol1[0])
        self.my_combobox_colonia1['values']=self.nomCol1
        self.onSeleccionColonia1
    def onSeleccionColonia1(self,event):
        clave=0
        if self.my_combobox_colonia1.current()!=-1:
            clave=self.my_combobox_colonia1.current()
        self.colonia1=bd.Colonia()
        self.colonia1=self.datoCol1.__getitem__(clave)

    def onGuardarProveedor(self):
        persona,proveedor = self.getDatos()
        if persona!=None and proveedor!=None:
            tablaProveedores.agregarProveedorProcedure(persona,proveedor)
            if mb.askyesno(message="Se va a registrar un nuevo proveedor\n¿Desea continuar?", title="Agregar Proveedor"):
                tablaProveedores.confirmarProveedorProcedure()
                mb.showinfo("Agregar Proveedor","Proveedor registrado con exito")
                self.reiniciarCajas()
            else:
                tablaProveedores.cancelarProveedoroProcedure()

    def onSalir(self):
        self.destroy()

    def foc_in_ap(self, * args):
        if self.apellidoPaterno_var.get()=="Ingrese el apellido paterno":
            self.apellidoPaterno_var.set("")
            self.entradaApellidoPaterno.focus()
    def foc_in_am(self, * args):
        if self.apellidoMaterno_var.get()=="Ingrese el apellido materno":
            self.apellidoMaterno_var.set("")
            self.entradaApellidoMaterno.focus()
    def foc_in_num(self, * args):
        if self.numeroTelefonico_var.get()=="Ingrese el número telefonico":
            self.numeroTelefonico_var.set("")
            self.entradaNumeroTelefonico.focus()
    def foc_in_cor(self, * args):
        if self.correoElectronico_var.get()=="Ingrese el correo electronico":
            self.correoElectronico_var.set("")
            self.entradaCorreoElectronico.focus()
    def foc_in_edoci(self, * args):
        if self.estadoCivil_var.get()=="Ingrese el estado civil":
            self.estadoCivil_var.set("")
            self.entradaEstadoCivil.focus()
    def foc_in_calle(self, * args):
        if self.calle_var.get()=="Ingrese la calle":
            self.calle_var.set("")
            self.entradaCalle.focus()
    def foc_in_entreCalle(self, * args):
        if self.entreCalle_var.get()=="Ingrese las calles":
            self.entreCalle_var.set("")
            self.entradaEntreCalle.focus()
    def foc_in_numero(self, * args):
        if self.numero_var.get()=="Ingrese el número":
            self.numero_var.set("")
            self.entradaNumero.focus()
    
    def foc_in_curp(self, * args):
        if self.curp_var.get()=="Ingrese la CURP":
            self.curp_var.set("")
            self.entradaCurp.focus()
    def foc_in_no(self, * args):
        if self.nombrePer_var.get()=="Ingrese el nombre":
            self.nombrePer_var.set("")
            self.entradaNombrePer.focus()
    def foc_in_ap(self, * args):
        if self.apellidoPaterno_var.get()=="Ingrese el apellido paterno":
            self.apellidoPaterno_var.set("")
            self.entradaApellidoPaterno.focus()
    def foc_in_am(self, * args):
        if self.apellidoMaterno_var.get()=="Ingrese el apellido materno":
            self.apellidoMaterno_var.set("")
            self.entradaApellidoMaterno.focus()
    def foc_in_num1(self, * args):
        if self.numeroTelefonico1_var.get()=="Ingrese el número telefonico":
            self.numeroTelefonico1_var.set("")
            self.entradaNumeroTelefonico1.focus()
    def foc_in_cor1(self, * args):
        if self.correoElectronico1_var.get()=="Ingrese el correo electronico":
            self.correoElectronico1_var.set("")
            self.entradaCorreoElectronico1.focus()
    def foc_in_edoci(self, * args):
        if self.estadoCivil_var.get()=="Ingrese el estado civil":
            self.estadoCivil_var.set("")
            self.entradaEstadoCivil.focus()
    def foc_in_calle1(self, * args):
        if self.calle1_var.get()=="Ingrese la calle":
            self.calle1_var.set("")
            self.entradaCalle1.focus()
    def foc_in_entreCalle1(self, * args):
        if self.entreCalle1_var.get()=="Ingrese las calles":
            self.entreCalle1_var.set("")
            self.entradaEntreCalle1.focus()
    def foc_in_numero1(self, * args):
        if self.numero1_var.get()=="Ingrese el número":
            self.numero1_var.set("")
            self.entradaNumero1.focus()

    def onEntNombre(self,event):
        self.entradaNumeroTelefonico.focus()
    def onEntNum(self,event):
        self.entradaCorreoElectronico.focus()
    def onEntCorreo(self,event):
        self.my_combobox_estado.focus()
    def onEntCodigo(self,event):
        self.onSeleccionCodigo('<<ComboboxSelected>>')
        self.my_combobox_colonia.focus()
    def onEntEstado(self,event):
        self.onSeleccionEstado('<<ComboboxSelected>>')
        self.my_combobox_ciudad.focus()
    def onEntCiudad(self,event):
        self.onSeleccionCiudad('<<ComboboxSelected>>')
        self.my_combobox_codigoPostal.focus()
    def onEntColonia(self,event):
        self.onSeleccionColonia('<<ComboboxSelected>>')
        self.entradaCalle.focus()
    def onEntCalle(self,event):
        self.entradaEntreCalle.focus()
    def onEntEntreCalle(self,event):
        self.entradaNumero.focus()
    def onEntNumero(self,event):
        self.my_combobox_orientacion.focus()
    def onEntOrientacion(self,event):
        self.entradaCurp.focus()
    def onEntCurp(self,event):
        if len(self.curp_var.get())>20:
            mb.showinfo(title="Error",message="El campo de la CURP exede los 20 caracteres")
        else:
            if len(self.curp_var.get())!=0:
                persona=tablaProveedores.buscarPersonaCurpProcedure(self.curp_var.get())
                if persona!=None:
                    try:
                        mb.showinfo(title="Error de existencia",message=f"Ya existe una persona registrada con la CURP: '{persona.getCURPPer()}' ")
                    except:
                        self.entradaNombrePer.focus()
                else:
                    self.entradaNombrePer.focus()
            else:
                mb.showinfo(title="Error",message="La CURP no tiene caracteres aún")
    def onEntNombrePer(self,event):
        self.entradaApellidoPaterno.focus()
    def onEntAP(self,event):
        self.entradaApellidoMaterno.focus()
    def onEntAM(self,event):
        self.my_combobox_genero.focus()
    def onEntCaja(self,event):
        self.entradaNumeroTelefonico1.focus()
    def onEntNum1(self,event):
        self.entradaCorreoElectronico1.focus()
    def onEntCorreo1(self,event):
        self.entradaEstadoCivil.focus()
    def onEntEstadoCivil(self,event):
        self.my_combobox_estado1.focus()
    def onEntCodigo1(self,event):
        self.onSeleccionCodigo1('<<ComboboxSelected>>')
        self.my_combobox_colonia1.focus()
    def onEntEstado1(self,event):
        self.onSeleccionEstado1('<<ComboboxSelected>>')
        self.my_combobox_ciudad1.focus()
    def onEntCiudad1(self,event):
        self.onSeleccionCiudad1('<<ComboboxSelected>>')
        self.my_combobox_codigoPostal1.focus()
    def onEntColonia1(self,event):
        self.onSeleccionColonia1('<<ComboboxSelected>>')
        self.entradaCalle1.focus()
    def onEntCalle1(self,event):
        self.entradaEntreCalle1.focus()
    def onEntEntreCalle1(self,event):
        self.entradaNumero1.focus()
    def onEntNumero1(self,event):
        self.my_combobox_orientacion1.focus()
    def onEntOrientacion1(self,event):
        self.onGuardarProveedor()

    def validarCurp(self):
        if len(self.curp_var.get())>20:
            mb.showinfo(title="Error",message="El campo de la CURP exede los 20 caracteres")
            return False
        else:
            persona=tablaEmpleados.buscarPersonaCurpProcedure(self.curp_var.get())
            print()
            if persona!=None:
                try:
                    mb.showinfo(title="Error de existencia",message=f"Ya existe una persona registrada con la CURP: '{persona.getCURPPer()}' ")
                    return False
                except:
                    return True
            else:
                return True

    def validarVacios(self):
        fecha=datetime.now()
        año=fecha.year
        mes=fecha.month
        dia=fecha.day
        fech=str(año-18)+"-01-01"
        x=self.validarCurp()
        if self.entradaNombre.get()=="":
            return False,1," ya que no puede quedar vacio"
        elif self.entradaNumeroTelefonico.get()=="" or self.entradaNumeroTelefonico.get()=="Ingrese el número telefonico":
            return False,2," ya que no puede quedar vacio"
        elif self.entradaCorreoElectronico.get()=="" or self.entradaCorreoElectronico.get()=="Ingrese el correo electronico":
            return False,3," ya que no puede quedar vacio"
        elif self.entradaCalle.get()=="" or self.entradaCalle.get()=="Ingrese la calle":
            return False,8," ya que no puede quedar vacio"
        elif self.entradaEntreCalle.get()=="" or self.entradaEntreCalle.get()=="Ingrese las calles":
            return False,9," ya que no puede quedar vacio"
        elif self.entradaNumero.get()=="" or self.entradaNumero.get()=="Ingrese el número":
            return False,10," ya que no puede quedar vacio"
        elif self.entradaCurp.get()=="":
            return False,12," ya que no puede quedar vacio"
        elif not x:
            return False,0,""
        elif self.entradaNombrePer.get()=="" or self.entradaNombrePer.get()=="Ingrese el nombre":
            return False,13," ya que no puede quedar vacio"
        elif self.entradaApellidoPaterno.get()=="" or self.entradaApellidoPaterno.get()=="Ingrese el apellido paterno":
            return False,14," ya que no puede quedar vacio"
        elif self.entradaApellidoMaterno.get()=="" or self.entradaApellidoMaterno.get()=="Ingrese el apellido materno":
            return False,15," ya que no puede quedar vacio"
        elif self.entradaNumeroTelefonico1.get()=="" or self.entradaNumeroTelefonico1.get()=="Ingrese el número telefonico":
            return False,18," ya que no puede quedar vacio"
        elif self.entradaCorreoElectronico1.get()=="" or self.entradaCorreoElectronico1.get()=="Ingrese el correo electronico":
            return False,19," ya que no puede quedar vacio"
        elif self.entradaEstadoCivil.get()=="" or self.entradaEstadoCivil.get()=="Ingrese el estado civil":
            return False,20," ya que no puede quedar vacio"
        elif self.entradaCalle1.get()=="" or self.entradaCalle1.get()=="Ingrese la calle":
            return False,25," ya que no puede quedar vacio"
        elif self.entradaEntreCalle1.get()=="" or self.entradaEntreCalle1.get()=="Ingrese las calles":
            return False,26," ya que no puede quedar vacio"
        elif self.entradaNumero1.get()=="" or self.entradaNumero1.get()=="Ingrese el número":
            return False,27," ya que no puede quedar vacio"

        if str(self.fechaNacimiento.get_date())==fech:
            if not mb.askyesno(message="La fecha de nacimiento no ha sido modificada \n¿Desea continuar?", title="Agregar Empleado"):
                return False,0,""

        try:
            self.colonia.getClaveCol()
            try:
                self.colonia1.getClaveCol()
                return True,-1,""
            except:
                return False,24," no hay colonia de representante seleccionada"
        except:
            return False,7," no hay colonia de proveedor seleccionada"
        

    def reiniciarCajas(self):
        self.nombre_var.set("")
        self.numeroTelefonico_var.set("Ingrese el número telefonico")
        self.correoElectronico_var.set("Ingrese el correo electronico")
        self.my_combobox_estado.set(self.nomEst[0])
        self.my_combobox_ciudad.configure(state=tkinter.DISABLED)
        self.my_combobox_ciudad.set("")
        self.my_combobox_codigoPostal.configure(state=tkinter.DISABLED)
        self.my_combobox_codigoPostal.set("")
        self.my_combobox_colonia.configure(state=tkinter.DISABLED)
        self.my_combobox_colonia.set("")
        self.calle_var.set("Ingrese la calle")
        self.entreCalle_var.set("Ingrese las calles")
        self.numero_var.set("Ingrese el número")
        self.my_combobox_orientacion.set("Norte")

        self.curp_var.set("Ingrese la CURP")
        self.nombrePer_var.set("Ingrese el nombre")
        self.apellidoPaterno_var.set("Ingrese el apellido paterno")
        self.apellidoMaterno_var.set("Ingrese el apellido materno")
        self.my_combobox_genero.set("Masculino")
        fecha=datetime.now()
        año=fecha.year
        self.fechaNacimiento.set_date(date=date((año-18),1,1))
        self.numeroTelefonico1_var.set("Ingrese el número telefonico")
        self.correoElectronico1_var.set("Ingrese el correo electronico")
        self.estadoCivil_var.set("Ingrese el estado civil")
        self.my_combobox_estado1.set(self.nomEst1[0])
        self.my_combobox_ciudad1.configure(state=tkinter.DISABLED)
        self.my_combobox_ciudad1.set("")
        self.my_combobox_codigoPostal1.configure(state=tkinter.DISABLED)
        self.my_combobox_codigoPostal1.set("")
        self.my_combobox_colonia1.configure(state=tkinter.DISABLED)
        self.my_combobox_colonia1.set("")
        self.calle1_var.set("Ingrese la calle")
        self.entreCalle1_var.set("Ingrese las calles")
        self.numero1_var.set("Ingrese el número")
        self.my_combobox_orientacion1.set("Norte")
        self.entradaNombre.focus()

    def getDatos(self):
        valido,campo,error=self.validarVacios()
        if valido:
            persona=bd.Persona()
            proveedor=bd.Proveedor()

            proveedor.setClaveProv(None)
            proveedor.setNomEmpProv(self.entradaNombre.get())
            proveedor.setCalleProv(self.entradaCalle1.get())
            proveedor.setNumDomProv(self.entradaNumero.get())
            proveedor.setOrientacionProv(self.my_combobox_orientacion.get())
            proveedor.setEntreCallesProv(self.entradaEntreCalle.get())
            proveedor.setTelefonoProv(self.entradaNumeroTelefonico.get())
            proveedor.setMailProv(self.entradaCorreoElectronico.get())
            proveedor.setClaveCol(self.colonia.getClaveCol())

            persona.setClavePer(None)
            persona.setNomPer(self.entradaNombrePer.get())
            persona.setApPer(self.entradaApellidoPaterno.get())
            persona.setAmPer(self.entradaApellidoMaterno.get())
            persona.setCallePer(self.entradaCalle1.get())
            persona.setNumDomPer(self.entradaNumero1.get())
            persona.setOrientacionPer(self.my_combobox_orientacion1.get())
            persona.setEntreCallesPer(self.entradaEntreCalle1.get())
            persona.setTelefonoPer(self.entradaNumeroTelefonico1.get())
            persona.setMailPer(self.entradaCorreoElectronico1.get())
            persona.setSexoPer(self.my_combobox_genero.get())
            persona.setFnacimientoPer(self.fechaNacimiento.get_date())
            persona.setEdoCivilPer(self.entradaEstadoCivil.get())
            persona.setColPer(self.colonia1.getClaveCol())
            persona.setCURPPer(self.entradaCurp.get())

            return persona,proveedor
        else:
            if campo!=0:
                mb.showinfo("Agregar Proveedor","Error el campo "+str(campo)+str(error))
            return None,None

#LISTAR PROVEEDORES
class PanelListarProveedores(Frame):
    def __init__(self, container):
        super().__init__(container)
        self.config(background='lightgray')
        self.columnconfigure(0,weight=1)
        self.columnconfigure(0,weight=3)
        self.container=container
        setContainer(container)
        self.__create_widgets()
        self.crearTabla()
    
    def __create_widgets(self):
        fuente= "Helvetica 12 "
        self.botonSalir=Button(self, text='Salir', font=fuente, command=self.onSalir).grid(column=1, row=3)

        for widget in self.winfo_children():
            widget.grid(padx=5, pady=5)

    def crearTabla(self):
        self.tabla=Treeview(self)
        self.tabla['columns'] = ("Nombre","Telefono","Correo electronico","Representante","Domicilio")
        self.tabla.column('#0', width=50,anchor=CENTER)
        self.tabla.column('Nombre', width=100,anchor=CENTER)
        self.tabla.column('Telefono', width=75,anchor=CENTER)
        self.tabla.column('Correo electronico', width=100,anchor=CENTER)
        self.tabla.column('Representante', width=100,anchor=CENTER)
        self.tabla.column('Domicilio', width=350,anchor=CENTER)
        self.tabla.heading('#0',text='Clave Proveedor',anchor=CENTER)
        self.tabla.heading('Nombre',text='Nombre',anchor=CENTER)
        self.tabla.heading('Telefono',text='Telefono',anchor=CENTER)
        self.tabla.heading('Correo electronico',text='Correo electronico',anchor=CENTER)
        self.tabla.heading('Representante',text='Representante',anchor=CENTER)
        self.tabla.grid(column=1,row=0,ipadx=265,ipady=180)
        self.agregarDatos()
        return self.tabla

    def agregarDatos(self):
        self.onLimpiarTabla()
        count=0
        proveedores=tablaProveedores.listarProveedoresProcedure()
        for proveedor in proveedores:
            repres=tablaProveedores.buscarRepresentanteProcedure(proveedor.getClaveProv())
            persona=tablaProveedores.getPersonaProcedure(repres.getClavePer())
            domicilio=proveedor.parteDomicilio()
            domicilio,clave=tablaDirecciones.getColonia(domicilio,proveedor.getClaveCol())
            domicilio,clave=tablaDirecciones.getCodigoPostal(domicilio,clave)
            domicilio,clave=tablaDirecciones.getCiudad(domicilio,clave)
            domicilio=tablaDirecciones.getEstado(domicilio,clave)
            self.tabla.insert(parent='',index='end',iid=count, text=proveedor.getClaveProv(),
                values=(proveedor.getNomEmpProv(),proveedor.getTelefonoProv(),proveedor.getMailProv(),persona.salidaNombre(), domicilio))
            count += 1

    def onLimpiarTabla(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
    
    def onSalir(self):
        for conElement in self.container.winfo_children():
            if not isinstance(conElement,Menu):
                conElement.destroy()

#REGISTRAR PRODUCTOS
class PanelRegistroProductos(Frame):
    def __init__(self, container):
        super().__init__(container)
        self.config(bg='lightgray')
        self.columnconfigure(0,weight=1)
        self.columnconfigure(0,weight=3)
        setContainer(container)
        self.__create_widgets()

    def __create_widgets(self):
        fuente= "Helvetica 12 "
        self.lblDatos=Label(self,text="DATOS DEL PRODUCTO",font = fuente,bg='lightgray').grid(column=1,row=0)
        
        self.lblCodigoBarras=Label(self,text="Codigo de Barras",font=fuente,bg='lightgray').grid(column=0,row=1)

        self.codbar_var=StringVar()
        self.codbar_var.set("")
        self.entradaCodbar=Entry(self, width=40, textvariable=self.codbar_var,font=fuente)
        self.entradaCodbar.grid(column=1,row=1)
        self.entradaCodbar.focus()
        self.entradaCodbar.bind("<Return>", self.onEntCodigo)

        self.lblNombre=Label(self,text="Nombre",font=fuente,bg='lightgray').grid(column=0,row=2)

        self.nombre_var=StringVar()
        self.nombre_var.set("Ingrese el nombre")
        self.entradaNombre=Entry(self, width=40, textvariable=self.nombre_var,font=fuente)
        self.entradaNombre.grid(column=1,row=2)
        self.entradaNombre.bind("<FocusIn>", self.foc_in_nombre)
        self.entradaNombre.bind("<Return>", self.onEntNombre)

        self.lblTipo=Label(self,text="Tipo",font=fuente,bg='lightgray').grid(column=0,row=3)

        self.tipo_var=StringVar()
        self.tipo_var.set("Ingrese el tipo")
        self.entradaTipo=Entry(self, width=40, textvariable=self.tipo_var,font=fuente)
        self.entradaTipo.grid(column=1,row=3)
        self.entradaTipo.bind("<FocusIn>", self.foc_in_tipo)
        self.entradaTipo.bind("<Return>", self.onEntTipo)

        self.lblMarca=Label(self,text="Marca",font=fuente,bg='lightgray').grid(column=0,row=4)

        self.marca_var=StringVar()
        self.marca_var.set("Ingrese la marca")
        self.entradaMarca=Entry(self, width=40, textvariable=self.marca_var,font=fuente)
        self.entradaMarca.grid(column=1,row=4)
        self.entradaMarca.bind("<FocusIn>", self.foc_in_marca)
        self.entradaMarca.bind("<Return>", self.onEntMarca)

        self.lblColor=Label(self,text="Color",font=fuente,bg='lightgray').grid(column=0,row=5)

        self.color_var=StringVar()
        self.color_var.set("Ingrese el color")
        self.entradaColor=Entry(self, width=40, textvariable=self.color_var,font=fuente)
        self.entradaColor.grid(column=1,row=5)
        self.entradaColor.bind("<FocusIn>", self.foc_in_color)
        self.entradaColor.bind("<Return>", self.onEntColor)

        self.lblGarantia=Label(self,text="Garantia",font=fuente,bg='lightgray').grid(column=0,row=6)

        self.garantia_var=StringVar()
        self.garantia_var.set("Ingresa los dias de la garantia")
        self.entradaGarantia=Entry(self, width=40, textvariable=self.garantia_var,font=fuente)
        self.entradaGarantia.grid(column=1,row=6)
        self.entradaGarantia.bind("<FocusIn>", self.foc_in_garantia)
        self.entradaGarantia.bind("<Return>", self.onEntGarantia)

        self.lblPresentacion=Label(self,text="Presentacion",font=fuente,bg='lightgray').grid(column=0,row=7)

        self.presentacion_var=StringVar()
        self.presentacion_var.set("Ingresa la presentación")
        self.entradaPresentacion=Entry(self, width=40, textvariable=self.presentacion_var,font=fuente)
        self.entradaPresentacion.grid(column=1,row=7)
        self.entradaPresentacion.bind("<FocusIn>", self.foc_in_presetacion)
        self.entradaPresentacion.bind("<Return>", self.onEntPresentacion)

        self.lblModelo=Label(self,text="Modelo",font=fuente,bg='lightgray').grid(column=0,row=8)

        self.modelo_var=StringVar()
        self.modelo_var.set("Ingrese el modelo")
        self.entradaModelo=Entry(self, width=40, textvariable=self.modelo_var,font=fuente)
        self.entradaModelo.grid(column=1,row=8)
        self.entradaModelo.bind("<FocusIn>", self.foc_in_modelo)
        self.entradaModelo.bind("<Return>", self.onEntModelo)

        self.lblUnidadMeddida=Label(self,text="Unidad Medida",font=fuente,bg='lightgray').grid(column=0,row=9)

        self.lblAltoMedida=Label(self,text="mm",font=fuente,bg='lightgray')
        self.lblAltoMedida.grid(column=2,row=10)
        self.lblLargoMedida=Label(self,text="mm",font=fuente,bg='lightgray')
        self.lblLargoMedida.grid(column=2,row=11)
        self.lblAnchoMedida=Label(self,text="mm",font=fuente,bg='lightgray')
        self.lblAnchoMedida.grid(column=2,row=12)

        self.my_combobox_unidadMedida=tkk.Combobox(self,width=38,font = fuente,state="readonly")
        self.my_combobox_unidadMedida.grid(column=1,row=9)
        self.medida = ['Milímetro','Centímetros','Metro']
        self.my_combobox_unidadMedida.set(self.medida[0])
        self.my_combobox_unidadMedida['values']=self.medida
        self.my_combobox_unidadMedida.bind("<<ComboboxSelected>>", self.modificarMedida)
        self.my_combobox_unidadMedida.bind("<Return>", self.onEntUnidadMedida)

        self.lblAlto=Label(self,text="Alto",font=fuente,bg='lightgray').grid(column=0,row=10)

        self.alto_var=StringVar()
        self.alto_var.set("Ingresa el alto del producto")
        self.entradaAlto=Entry(self, width=40, textvariable=self.alto_var,font=fuente)
        self.entradaAlto.grid(column=1,row=10)
        self.entradaAlto.bind("<FocusIn>", self.foc_in_alto)
        self.entradaAlto.bind("<Return>", self.onEntAlto)

        self.lblLargo=Label(self,text="Largo",font=fuente,bg='lightgray').grid(column=0,row=11)

        self.largo_var=StringVar()
        self.largo_var.set("Ingresa el largo del producto")
        self.entradaLargo=Entry(self, width=40, textvariable=self.largo_var,font=fuente)
        self.entradaLargo.grid(column=1,row=11)
        self.entradaLargo.bind("<FocusIn>", self.foc_in_largo)
        self.entradaLargo.bind("<Return>", self.onEntLargo)

        self.lblAncho=Label(self,text="Ancho",font=fuente,bg='lightgray').grid(column=0,row=12)

        self.ancho_var=StringVar()
        self.ancho_var.set("Ingresa el ancho del producto")
        self.entradaAncho=Entry(self, width=40, textvariable=self.ancho_var,font=fuente)
        self.entradaAncho.grid(column=1,row=12)
        self.entradaAncho.bind("<FocusIn>", self.foc_in_ancho)
        self.entradaAncho.bind("<Return>", self.onEntAncho)

        self.lblContenido=Label(self,text="Contenido",font=fuente,bg='lightgray').grid(column=0,row=13)

        self.contenido_var=StringVar()
        self.contenido_var.set("Ingrese el contenido")
        self.entradaContenido=Entry(self, width=40, textvariable=self.contenido_var,font=fuente)
        self.entradaContenido.grid(column=1,row=13)
        self.entradaContenido.bind("<FocusIn>", self.foc_in_contenido)
        self.entradaContenido.bind("<Return>", self.onEntContenido)

        self.lblPrecioVenta=Label(self,text="Precio venta",font=fuente,bg='lightgray').grid(column=0,row=14)

        self.precioventa_var=StringVar()
        self.precioventa_var.set("Ingresa el precio de venta")
        self.entradaPrecioVenta=Entry(self, width=40, textvariable=self.precioventa_var,font=fuente)
        self.entradaPrecioVenta.grid(column=1,row=14)
        self.entradaPrecioVenta.bind("<FocusIn>", self.foc_in_precioventa)
        self.entradaPrecioVenta.bind("<Return>", self.onEntPrecioVenta)

        self.lblSeparador0=Label(self,text="          ",font = fuente,bg='lightgray').grid(column=1,row=15)
        self.lblSeparador1=Label(self,text="          ",font = fuente,bg='lightgray').grid(column=2,row=15)
        myFont = font.Font(family='Roboto', size='14')
        self.botonGuardar=Button(self, text='Guardar',font=myFont,command=self.onGuardarProducto)
        self.botonGuardar.grid(column=1, row=16)
        self.botonSalir=Button(self, text='Salir',font=myFont,command=self.onSalir)
        self.botonSalir.grid(column=2, row=16)
        self.lblSeparador7=Label(self,text="          ",font = fuente,bg='lightgray').grid(column=4,row=16)
        self.botonTerminar=Button(self, text='Terminar',font=myFont,command=self.terminar,state=tkinter.DISABLED)
        self.botonTerminar.grid(column=4, row=16)

        self.lblDatos=Label(self,text="DATOS DEL STOCK MINIMO-MAXIMO",font = fuente,bg='lightgray').grid(column=4,row=0)
        
        self.lblMinimo=Label(self,text="Minimo",font=fuente,bg='lightgray').grid(column=3,row=1)

        self.minimo_var=StringVar()
        self.minimo_var.set("Ingresar el stock minimo")
        self.entradaMinimo=Entry(self, width=40, textvariable=self.minimo_var,font=fuente,state=tkinter.DISABLED)
        self.entradaMinimo.grid(column=4,row=1)
        self.entradaMinimo.bind("<Return>", self.onEntMinimo)

        self.lblMaximo=Label(self,text="Maximo",font=fuente,bg='lightgray').grid(column=3,row=2)

        self.maximo_var=StringVar()
        self.maximo_var.set("Ingresar el stock maximo")
        self.entradaMaximo=Entry(self, width=40, textvariable=self.maximo_var,font=fuente,state=tkinter.DISABLED)
        self.entradaMaximo.grid(column=4,row=2)
        self.entradaMaximo.bind("<FocusIn>", self.foc_in_maximo)
        self.entradaMaximo.bind("<Return>", self.onEntMaximo)

        self.lblTiendas=Label(self,text="Tiendas",font = fuente,bg='lightgray').grid(column=3,row=3)
        
        self.my_combobox_tiendas=tkk.Combobox(self,width=38,font = fuente,state=tkinter.DISABLED)
        self.my_combobox_tiendas.grid(column=4,row=3)
        #self.my_combobox_tiendas.bind("<<ComboboxSelected>>", self.guardar)
        self.my_combobox_tiendas.bind("<Return>", self.onEntTiendas)

        self.lblSeparador2=Label(self,text="          ",font = fuente,bg='lightgray').grid(column=3,row=4)
        self.botonRegistrar=Button(self, text='Registrar',font=myFont,state=tkinter.DISABLED,command=self.guardarMinimoMaximo)
        self.botonRegistrar.grid(column=4, row=4)

        #self.radioValue = tkinter.IntVar() 
        #self.rdioOne = tkk.Radiobutton(self, text='Aplicar a todas',variable=self.radioValue)
        #self.rdioOne.grid(column=5,row=3)

        for widget in self.winfo_children():
            widget.grid(padx=5, pady=2)

    def modificarMedida(self,event):
        if self.my_combobox_unidadMedida.get()=='Milímetro':
            self.texto='mm'
        elif self.my_combobox_unidadMedida.get()=='Centímetros':
            self.texto='cm'
        else:
            self.texto='me'
        self.lblAltoMedida.configure(text=self.texto)
        self.lblLargoMedida.configure(text=self.texto)
        self.lblAnchoMedida.configure(text=self.texto)

    def terminar(self):
        if len(self.minimo_var.get())>0 or len(self.maximo_var.get())>0:
             if mb.askyesno(message="Los datos de las cjas no ha sido guardados\n¿Desea continuar?", title="Agregar Producto"):
                tablaProductos.aceptarProductoProcedure()
                self.reiniciarCajasProducto()

    def validarminimo(self):
        try:
            x = int(self.entradaMinimo.get())
            y = int(self.entradaMaximo.get())
            return True
        except:
            return False

    def guardarMinimoMaximo(self):
        if self.validarminimo():
            minmax=bd.MinMax()
            minmax.setMinMinMax(self.entradaMinimo.get())
            minmax.setMaxMinMax(self.entradaMaximo.get())
            minmax.setCodbarPro(self.clave)
            tienda=self.b.__getitem__(self.my_combobox_tiendas.current())
            minmax.setClaveTie(tienda.getClaveTie())
            self.botonTerminar.configure(state='normal')
            tablaProductos.guardarMinimoMaximoProcedure(minmax)
            self.reinicio()
        else:
            mb.showinfo("Agregar Producto","Error, los minimo o maximo no son una cantidad entera ")

    def reinicio(self):
        self.minimo_var.set("")
        self.maximo_var.set("Ingresar el stock maximo")
        self.cargartiendas(self.clave)
        self.entradaMinimo.focus()

    def cargartiendas(self,clave):
        self.clave=clave
        self.a, self.b = tablaTiendas.getTiendasConsulta(clave)
        if len(self.b)>=1:
            self.my_combobox_tiendas.set(self.a[0])
            self.my_combobox_tiendas['values']=self.a
        else:
            mb.showinfo("Agregar Producto","Error, ya no hay mas tiendas para aplicar")
            tablaProductos.aceptarProductoProcedure()
            self.reiniciarCajasProducto()

    def desactivarProducto(self):
        self.botonGuardar.configure(state=tkinter.DISABLED)
        self.entradaCodbar.configure(state='readonly')
        self.entradaNombre.configure(state='readonly')
        self.entradaTipo.configure(state='readonly')
        self.entradaMarca.configure(state='readonly')
        self.entradaColor.configure(state='readonly')
        self.entradaGarantia.configure(state='readonly')
        self.entradaPresentacion.configure(state='readonly')
        self.entradaModelo.configure(state='readonly')
        self.entradaAlto.configure(state='readonly')
        self.entradaLargo.configure(state='readonly')
        self.entradaAncho.configure(state='readonly')
        self.entradaContenido.configure(state='readonly')
        self.entradaPrecioVenta.configure(state=tkinter.DISABLED)
        self.my_combobox_unidadMedida.configure(state=tkinter.DISABLED)

    def activarMinimoMaximo(self,clave):
        self.minimo_var.set("")
        self.entradaMinimo.configure(state='normal')
        self.entradaMaximo.configure(state='normal')
        self.my_combobox_tiendas.configure(state='readonly')
        self.entradaMinimo.focus()
        self.botonRegistrar.configure(state='normal')
        self.cargartiendas(clave)

    def onGuardarProducto(self):
        producto,precioVenta = self.getDatosProducto()
        if producto!=None and precioVenta!=None:
            self.clave = tablaProductos.guardarProductoProcedure(producto,precioVenta)
            for i in self.clave:
                for x in i:
                    clave=x
            self.activarMinimoMaximo(clave)
            self.desactivarProducto()

    def onSalir(self):
        if mb.askyesno(message="Se van a deshacer todos los cambios realizados\n¿Desea continuar?", title="Agregar Producto"):
            tablaProductos.cancelarProductoProcedure()
            self.destroy()

    def foc_in_nombre(self, * args):
        if self.nombre_var.get()=="Ingrese el nombre":
            self.nombre_var.set("")
            self.entradaNombre.focus()
    def foc_in_tipo(self, * args):
        if self.tipo_var.get()=="Ingrese el tipo":
            self.tipo_var.set("")
            self.entradaTipo.focus()
    def foc_in_marca(self, * args):
        if self.marca_var.get()=="Ingrese la marca":
            self.marca_var.set("")
            self.entradaMarca.focus()
    def foc_in_color(self, * args):
        if self.color_var.get()=="Ingrese el color":
            self.color_var.set("")
            self.entradaColor.focus()
    def foc_in_garantia(self, * args):
        if self.garantia_var.get()=="Ingresa los dias de la garantia":
            self.garantia_var.set("")
            self.entradaGarantia.focus()
    def foc_in_presetacion(self, * args):
        if self.presentacion_var.get()=="Ingresa la presentación":
            self.presentacion_var.set("")
            self.entradaPresentacion.focus()
    def foc_in_modelo(self, * args):
        if self.modelo_var.get()=="Ingrese el modelo":
            self.modelo_var.set("")
            self.entradaModelo.focus()
    def foc_in_alto(self, * args):
        if self.alto_var.get()=="Ingresa el alto del producto":
            self.alto_var.set("")
            self.entradaAlto.focus()
    def foc_in_largo(self, * args):
        if self.largo_var.get()=="Ingresa el largo del producto":
            self.largo_var.set("")
            self.entradaLargo.focus()
    def foc_in_ancho(self, * args):
        if self.ancho_var.get()=="Ingresa el ancho del producto":
            self.ancho_var.set("")
            self.entradaAncho.focus()
    def foc_in_contenido(self, * args):
        if self.contenido_var.get()=="Ingrese el contenido":
            self.contenido_var.set("")
            self.entradaContenido.focus()
    def foc_in_precioventa(self, * args):
        if self.precioventa_var.get()=="Ingresa el precio de venta":
            self.precioventa_var.set("")
            self.entradaPrecioVenta.focus()
    def foc_in_maximo(self, * args):
        if self.maximo_var.get()=="Ingresar el stock maximo":
            self.maximo_var.set("")
            self.entradaMaximo.focus()

    def onEntCodigo(self,event):
        if len(self.codbar_var.get())>20:
            mb.showinfo(title="Error",message="El campo del Codigo exede los 20 caracteres")
        else:
            if len(self.codbar_var.get())!=0:
                producto=tablaProductos.getProductoProcedure(self.codbar_var.get())
                if producto!=None:
                    try:
                        mb.showinfo(title="Error de existencia",message=f"Ya existe un producto con este codigo: '{producto.getCodigoPro()}' ")
                    except:
                        self.entradaNombre.focus()
                else:
                    self.entradaNombre.focus()
            else:
                mb.showinfo(title="Error",message="El campo de codigo no tiene caracteres aún")
    def onEntNombre(self,event):
        self.entradaTipo.focus()
    def onEntTipo(self,event):
        self.entradaMarca.focus()
    def onEntMarca(self,event):
        self.entradaColor.focus()
    def onEntColor(self,event):
        self.entradaGarantia.focus()
    def onEntGarantia(self,event):
        self.entradaPresentacion.focus()
    def onEntPresentacion(self,event):
        self.entradaModelo.focus()
    def onEntModelo(self,event):
        self.modificarMedida
        self.my_combobox_unidadMedida.focus()
    def onEntUnidadMedida(self,event):
        self.entradaAlto.focus()
    def onEntAlto(self,event):
        self.entradaLargo.focus()
    def onEntLargo(self,event):
        self.entradaAncho.focus()
    def onEntAncho(self,event):
        self.entradaContenido.focus()
    def onEntContenido(self,event):
        self.entradaPrecioVenta.focus()
    def onEntPrecioVenta(self,event):
        self.onGuardarProducto()
    def onEntMinimo(self,event):
        self.entradaMaximo.focus()
    def onEntMaximo(self,event):
        self.my_combobox_tiendas.focus()
    def onEntTiendas(self,event):
        self.guardarMinimoMaximo()

    def validarCodigo(self):
        if len(self.codbar_var.get())>20:
            mb.showinfo(title="Error",message="El campo del Codigo exede los 20 caracteres")
            return False
        else:
            if len(self.codbar_var.get())!=0:
                producto=tablaProductos.getProductoProcedure(self.codbar_var.get())
                if producto!=None:
                    try:
                        mb.showinfo(title="Error de existencia",message=f"Ya existe un producto con este codigo: '{producto.getCodigoPro()}' ")
                        return False
                    except:
                        return True
                else:
                    return True
            else:
                mb.showinfo(title="Error",message="El campo de codigo no tiene caracteres aún")
                return False

    def validarPrecio(self):
        try:
            x = float(self.entradaPrecioVenta.get())
            return True
        except:
            return False

    def validarContenido(self):
        try:
            x = int(self.entradaContenido.get())
            return True
        except:
            return False

    def validarVaciosProducto(self):
        if self.entradaCodbar.get()=="":
            return False,1," ya que no puede quedar vacio"
        else:
            x=self.validarCodigo()
            if not x:
                return False,0,""
        if self.entradaNombre.get()=="" or self.entradaNombre.get()=="Ingrese el nombre":
            return False,2," ya que no puede quedar vacio"
        elif self.entradaTipo.get()=="" or self.entradaTipo.get()=="Ingrese el tipo":
            return False,3," ya que no puede quedar vacio"
        elif self.entradaMarca.get()=="" or self.entradaMarca.get()=="Ingrese la marca":
            return False,4," ya que no puede quedar vacio"
        elif self.entradaColor.get()=="" or self.entradaColor.get()=="Ingrese el color":
            return False,5," ya que no puede quedar vacio"
        elif self.entradaGarantia.get()=="" or self.entradaGarantia.get()=="Ingresa los dias de la garantia":
            return False,6," ya que no puede quedar vacio"
        elif self.entradaPresentacion.get()=="" or self.entradaPresentacion.get()=="Ingresa la presentación":
            return False,7," ya que no puede quedar vacio"
        elif self.entradaModelo.get()=="" or self.entradaModelo.get()=="Ingrese el modelo":
            return False,8," ya que no puede quedar vacio"
        elif self.entradaAlto.get()=="" or self.entradaAlto.get()=="Ingresa el alto del producto":
            return False,9," ya que no puede quedar vacio"
        elif self.entradaLargo.get()=="" or self.entradaLargo.get()=="Ingresa el largo del producto":
            return False,10," ya que no puede quedar vacio"
        elif self.entradaAncho.get()=="" or self.entradaAncho.get()=="Ingresa el ancho del producto":
            return False,11," ya que no puede quedar vacio"
        elif self.entradaContenido.get()=="" or self.entradaContenido.get()=="Ingrese el contenido":
            return False,12," ya que no puede quedar vacio"
        elif self.entradaPrecioVenta.get()=="" or self.entradaPrecioVenta.get()=="Ingresa el precio de venta":
            return False,13," ya que no puede quedar vacio"
        if self.validarContenido():
            if self.validarPrecio():
                return True,0,""
            else:
                return False,13," ya que no es una cantidad numerica"
        else:
            return False,12," ya que no es una cantidad numerica entera"

    def reiniciarCajasProducto(self): 
        self.codbar_var.set("")
        self.nombre_var.set("Ingrese el nombre")
        self.tipo_var.set("Ingrese el tipo")
        self.marca_var.set("Ingrese la marca")
        self.color_var.set("Ingrese el color")
        self.garantia_var.set("Ingresa los dias de la garantia")
        self.presentacion_var.set("Ingresa la presentación")
        self.modelo_var.set("Ingrese el modelo")
        self.my_combobox_unidadMedida.set("Milímetro")
        self.modificarMedida
        self.alto_var.set("Ingresa el alto del producto")
        self.largo_var.set("Ingresa el largo del producto")
        self.ancho_var.set("Ingresa el ancho del producto")
        self.contenido_var.set("Ingrese el contenido")
        self.precioventa_var.set("Ingresa el precio de venta")

        self.minimo_var.set("Ingresar el stock minimo")
        self.maximo_var.set("Ingresar el stock maximo")
        self.my_combobox_tiendas.set("")
        self.my_combobox_tiendas.configure(state=tkinter.DISABLED)
        self.entradaMinimo.configure(state=tkinter.DISABLED)
        self.entradaMaximo.configure(state=tkinter.DISABLED)
        self.botonRegistrar.configure(state=tkinter.DISABLED)
        self.botonTerminar.configure(state=tkinter.DISABLED)

        self.entradaCodbar.focus()

    def getDatosProducto(self):
        valido,campo,error=self.validarVaciosProducto()
        if valido:
            producto=bd.Producto()
            producto.setCodbarPro(None)
            producto.setNomPro(self.entradaNombre.get())
            producto.setTipoPro(self.entradaTipo.get())
            producto.setMarcaPro(self.entradaMarca.get())
            producto.setColorPro(self.entradaColor.get())
            producto.setGarantiaPro(self.entradaGarantia.get())
            producto.setUmedidaGarantiaPro(None)
            producto.setPresentacionPro(self.entradaPresentacion.get())
            producto.setModeloPro(self.entradaModelo.get())
            producto.setUmedidaPro(self.my_combobox_unidadMedida.get())
            producto.setAltoPro(self.entradaAlto.get())
            producto.setLargoPro(self.entradaLargo.get())
            producto.setAnchoPro(self.entradaAncho.get())
            producto.setContenidoPro(self.entradaContenido.get())
            producto.setCodigoPro(self.entradaCodbar.get())

            return producto,self.precioventa_var.get()
        else:
            if campo!=0:
                mb.showinfo("Agregar Producto","Error el campo "+str(campo)+str(error))
            return None,None

#LISTAR PRODUCTOS
class PanelListarProductos(Frame):
    def __init__(self, container):
        super().__init__(container)
        self.config(background='lightgray')
        self.columnconfigure(0,weight=1)
        self.columnconfigure(0,weight=3)
        self.container=container
        setContainer(container)
        self.__create_widgets()
        self.crearTabla()
    
    def __create_widgets(self):
        fuente= "Helvetica 12 "
        self.botonSalir=Button(self, text='Salir', font=fuente, command=self.onSalir).grid(column=1, row=3)

        for widget in self.winfo_children():
            widget.grid(padx=5, pady=5)

    def crearTabla(self):
        self.tabla=Treeview(self)
        self.tabla['columns'] = ("Nombre","Garantia","Dimensiones","Precio Venta Actual")
        self.tabla.column('#0', width=50,anchor=CENTER)
        self.tabla.column('Nombre', width=100,anchor=CENTER)
        self.tabla.column('Garantia', width=75,anchor=CENTER)
        self.tabla.column('Dimensiones', width=100,anchor=CENTER)
        self.tabla.column('Precio Venta Actual', width=200,anchor=CENTER)
        self.tabla.heading('#0',text='Codigo Barras',anchor=CENTER)
        self.tabla.heading('Nombre',text='Nombre',anchor=CENTER)
        self.tabla.heading('Garantia',text='Garantia',anchor=CENTER)
        self.tabla.heading('Dimensiones',text='Dimensiones',anchor=CENTER)
        self.tabla.heading('Precio Venta Actual',text='Precio Venta Actual',anchor=CENTER)
        self.tabla.grid(column=1,row=0,ipadx=420,ipady=180)
        self.agregarDatos()
        return self.tabla

    def agregarDatos(self):
        self.onLimpiarTabla()
        count=0
        productos=tablaProductos.listarProductosProcedure()
        for producto in productos:
            garantia=producto.getGarantiaPro()+" "+producto.getUmedidaGarantiaPro()
            dimensiones=producto.getAltoPro()+"x"+producto.getLargoPro()+"x"+producto.getAnchoPro()
            precio=tablaProductos.buscarPrecioVentaProcedure(producto.getCodbarPro())
            self.tabla.insert(parent='',index='end',iid=count, text=producto.getCodigoPro(),
                values=(producto.getNomPro(),garantia,dimensiones,precio.getPrecioPre()))
            count += 1

    def onLimpiarTabla(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
    
    def onSalir(self):
        for conElement in self.container.winfo_children():
            if not isinstance(conElement,Menu):
                conElement.destroy()

#REGISTRAR RESURTIDOS (NO VALIDA DEL TODO)
class PanelRegistroResurtidos(Frame):
    def __init__(self, container):
        super().__init__(container)
        self.config(bg='lightgray')
        self.columnconfigure(0,weight=1)
        self.columnconfigure(0,weight=3)
        setContainer(container)
        self.__create_widgets()

    def __create_widgets(self):
        fuente= "Helvetica 12 "
        self.lblDatos=Label(self,text="DATOS DEL RESURTIDO",font = fuente,bg='lightgray').grid(column=1,row=0)
        
        self.lblTotal=Label(self,text="Cantidad Total",font=fuente,bg='lightgray').grid(column=0,row=1)

        self.total_var=StringVar()
        self.total_var.set("")
        self.entradaTotal=Entry(self, width=40, textvariable=self.total_var,font=fuente)
        self.entradaTotal.grid(column=1,row=1)
        self.entradaTotal.focus()
        self.entradaTotal.bind("<Return>", self.onEntTotal)

        self.lblProveedores=Label(self,text="Proveedores",font = fuente,bg='lightgray').grid(column=0,row=2)
        
        self.my_combobox_proveedor=tkk.Combobox(self,width=38,font = fuente,state="readonly")
        self.my_combobox_proveedor.grid(column=1,row=2)
        self.nomProv, self.datosProv = tablaProveedores.getProveedoresProcedure()
        self.my_combobox_proveedor.set(self.nomProv[0])
        self.my_combobox_proveedor['values']=self.nomProv
        self.my_combobox_proveedor.bind("<Return>", self.onEntProveedor)

        self.lblTiendas=Label(self,text="Tiendas",font = fuente,bg='lightgray').grid(column=0,row=3)
        
        self.my_combobox_tiendas=tkk.Combobox(self,width=38,font = fuente,state="readonly")
        self.my_combobox_tiendas.grid(column=1,row=3)
        self.nomTie, self.datoTie = tablaTiendas.getTiendas()
        self.my_combobox_tiendas.set(self.nomTie[0])
        self.my_combobox_tiendas['values']=self.nomTie
        self.my_combobox_tiendas.bind("<Return>", self.onEntTiendas)

        self.botonTerminar=Button(self, text='Registrar',font=fuente,command=self.guardarResrtido)
        self.botonTerminar.grid(column=1, row=4)

        self.lblCantidad=Label(self,text="Cantidad",font = fuente,bg='lightgray').grid(column=0,row=5)
        self.cantidad_var=StringVar()
        self.cantidad_var.set("Ingrese la cantidad")
        self.entradaCantidad=Entry(self, width=40, textvariable=self.cantidad_var,font=fuente)
        self.entradaCantidad.grid(column=1,row=5)
        self.entradaCantidad.bind("<FocusIn>", self.foc_in_cant)
        self.entradaCantidad.bind("<Return>", self.onEntCantidad)

        self.lblFechaCaducidad=Label(self,text="Fecha de caducidad",font = fuente,bg='lightgray').grid(column=0,row=6)
        self.fechaCaducidad = DateEntry(self, width=57)
        self.fechaCaducidad.grid(column=1, row=6)

        self.lblPrecio=Label(self,text="Precio",font = fuente,bg='lightgray').grid(column=0,row=7)
        self.precio_var=StringVar()
        self.precio_var.set("Ingrese el precio")
        self.entradaPrecio=Entry(self, width=40, textvariable=self.precio_var,font=fuente)
        self.entradaPrecio.grid(column=1,row=7)
        self.entradaPrecio.bind("<FocusIn>", self.foc_in_precio)
        self.entradaPrecio.bind("<Return>", self.onEntPrecio)

        self.lblProductos=Label(self,text="Productos",font = fuente,bg='lightgray').grid(column=0,row=8)
        
        self.my_combobox_productos=tkk.Combobox(self,width=38,font = fuente,state="readonly")
        self.my_combobox_productos.grid(column=1,row=8)
        self.my_combobox_productos.bind("<Return>", self.onEntProducto)

        self.lblTiendas2=Label(self,text="Tiendas",font = fuente,bg='lightgray').grid(column=0,row=9)
        
        self.tiendas_var=StringVar()
        self.tiendas_var.set("")
        self.entradaTienda=Entry(self, width=40, textvariable=self.tiendas_var,font=fuente,state=tkinter.DISABLED)
        self.entradaTienda.grid(column=1,row=9)
        self.entradaTienda.bind("<FocusIn>", self.foc_in_precio)
        self.entradaTienda.bind("<Return>", self.onEntPrecio)

        self.botonSalir=Button(self, text='Salir',font=fuente,command=self.onSalir)
        self.botonSalir.grid(column=2, row=10)

        for widget in self.winfo_children():
            widget.grid(padx=5, pady=2)

    def onSalir(self):
        if mb.askyesno(message="Se van a deshacer todos los cambios realizados\n¿Desea continuar?", title="Agregar Producto"):
            tablaProductos.cancelarProductoProcedure()
            self.destroy()
    
    def onGuardarRenglon(self):
        renglon=self.getDatosRenglon()
        if renglon!=None:
            tienda=self.datoTie.__getitem__(self.my_combobox_tiendas.current())
            tablaResurtidos.guardarRenglonResurtidoProcedure(renglon,tienda.getClaveTie())
            self.reinciarCajas()
    def convertirFecha(self,fecha):
        x = str(fecha)
        numero=""
        numeros=[]
        for i in x:
            if i=="-":
                numeros.append(numero)
                numero=""
            else:
                numero+=i
        numeros.append(numero)
        return numeros

    def validarRenglon(self):
        num2=self.convertirFecha(self.fechaCaducidad.get_date())
        fechaCaducidad=date(int(num2[0]),int(num2[1]),int(num2[2]))
        fecha=datetime.now()
        if self.entradaCantidad.get()=="":
            return False,1," ya que no puede quedar vacio"
        elif fechaCaducidad<=fecha:
            return False,2," la fecha de garantia es menor o igual a la fecha actual"
        elif self.precio_var.get()=="" or self.precio_var=="Ingrese el precio":
            return False,3," ya que no puede quedar vacio"

        return True,0,""
    
    def getDatosRenglon(self):
        valido,campo,dato=self.validarRenglon()
        if valido:
            renglon=bd.RenglonResurtir()
            renglon.setNumRenRes(None)
            renglon.setCantidadRenRes(self.entradaCantidad.get())
            renglon.setfCaducidadRenREs(self.fechaCaducidad.get_date())
            producto=self.datoPro.__getitem__(self.my_combobox_productos.current())
            renglon.setPrecioRenRes(self.entradaPrecio.get())
            renglon.setCodbarPro(producto.getCodbarPro())
            producto=self.datoPro.__getitem__(self.my_combobox_productos.current())
            renglon.set(producto.getCodbarPro())
            renglon.setClaveRes(self.getClave)
            return renglon
        else:
            if campo!=0:
                mb.showinfo("Agregar Resurtido","Error el campo "+str(campo)+str(dato))
            return None

    def setClave(self,clave):
        self.clavee=clave

    def getClave(self):
        return self.clavee

    def cargarProductos(self):
        self.nomPro, self.datoPro = tablaProductos.getProductosProcedure()
        self.my_combobox_productos.set(self.nomPro[0])
        self.my_combobox_productos['values']=self.nomPro

    def reinciarCajas(self):
        fecha=datetime.now()
        self.cantidad_var.set("")
        self.precio_var.set("Ingrese el precio")
        self.fechaCaducidad.set_date(date(fecha.year,fecha.month,fecha.day))
        
    def guardarResrtido(self):
        resurtir=self.getDatosResurtido()
        if resurtir!=None:
            self.clave = tablaResurtidos.guardarResurtidoProcedure(resurtir)
            for i in self.clave:
                for x in i:
                    clave=x
            #self.activarMinimoMaximo(clave)
            self.cerrarResurtido()
            self.setClave(clave)
            self.entradaCantidad.focus()

    def validarResurtido(self):
        try:
            x = float(self.entradaTotal.get())
            return True
        except:
            return False

    def getDatosResurtido(self):
        if self.validarResurtido():
            resurtir=bd.Resurtir()
            resurtir.setClaveRes(None)
            resurtir.setFechaRes(None)
            resurtir.setTotalRes(self.entradaTotal.get())
            proveedor=self.datosProv.__getitem__(self.my_combobox_proveedor.current())
            resurtir.setClaveProv(proveedor.getClaveProv())
            tienda=self.datoTie.__getitem__(self.my_combobox_tiendas.current())
            resurtir.setClaveTie(tienda.getClaveTie())
            return resurtir
        else:
            mb.showinfo("Agregar Empleado","Error el campo 1 pues no es un número")
            return None

    #def 

    def cerrarResurtido(self):
        self.entradaTotal.configure(state=tkinter.DISABLED)
        self.my_combobox_tiendas.configure(state=tkinter.DISABLED)
        self.my_combobox_proveedor.configure(state=tkinter.DISABLED)
        self.botonTerminar.configure(state=tkinter.DISABLED)
        self.tiendas_var.set(self.my_combobox_tiendas.get())

    def foc_in_cant(self, * args):
        if self.cantidad_var.get()=="Ingrese la cantidad":
            self.cantidad_var.set("")
            self.entradaCantidad.focus()
    def foc_in_precio(self, * args):
        if self.precio_var.get()=="Ingrese el precio":
            self.precio_var.set("")
            self.entradaPrecio.focus()
    def onEntTotal(self,event):
        if self.validarResurtido():
            self.my_combobox_proveedor.focus()
        else:
            mb.showinfo("Agregar Resurtido","Error el campo 1, el total no es un numero")
    def onEntProveedor(self,event):
        self.my_combobox_tiendas.focus()
    def onEntTiendas(self,event):
        self.guardarResrtido()
    def onEntCantidad(self,event):
        self.entradaPrecio.focus()
    def onEntPrecio(self,event):
        self.my_combobox_productos.focus()
    def onEntProducto(self,event):
        self.entradaTienda.focus()
    def onEntTiendas2(self,event):
        self.my_combobox_productos.focus()

#LISTAR RESURTIDO
class PanelListarResurtidos(Frame):
    def __init__(self, container):
        super().__init__(container)
        self.config(background='lightgray')
        self.columnconfigure(0,weight=1)
        self.columnconfigure(0,weight=3)
        self.container=container
        setContainer(container)
        self.__create_widgets()
        self.crearTabla()
    
    def __create_widgets(self):
        fuente= "Helvetica 12 "
        self.botonSalir=Button(self, text='Salir', font=fuente, command=self.onSalir).grid(column=1, row=3)

        for widget in self.winfo_children():
            widget.grid(padx=5, pady=5)

    def crearTabla(self):
        self.tabla=Treeview(self)
        self.tabla['columns'] = ("Fecha Resurtido","Total","Proveedor","Cantidad de SubSurtidos","Clave tienda")
        self.tabla.column('#0', width=50,anchor=CENTER)
        self.tabla.column('Fecha Resurtido', width=100,anchor=CENTER)
        self.tabla.column('Total', width=75,anchor=CENTER)
        self.tabla.column('Proveedor', width=100,anchor=CENTER)
        self.tabla.column('Cantidad de SubSurtidos', width=50,anchor=CENTER)
        self.tabla.column('Clave tienda', width=50,anchor=CENTER)
        self.tabla.heading('#0',text='Clave Resurtido',anchor=CENTER)
        self.tabla.heading('Fecha Resurtido',text='Fecha Resurtido',anchor=CENTER)
        self.tabla.heading('Total',text='Total',anchor=CENTER)
        self.tabla.heading('Proveedor',text='Proveedor',anchor=CENTER)
        self.tabla.heading('Cantidad de SubSurtidos',text='Cantidad de SubSurtidos',anchor=CENTER)
        self.tabla.heading('Clave tienda',text='Clave tienda',anchor=CENTER)
        self.tabla.grid(column=1,row=0,ipadx=430,ipady=180)
        self.agregarDatos()
        return self.tabla

    def agregarDatos(self):
        self.onLimpiarTabla()
        count=0
        resurtidos=tablaResurtidos.listarResurtidosProcedure()
        for resurtir in resurtidos:
            proveedor=tablaProveedores.getProveedorProcedure(resurtir.getClaveProv())
            clave = tablaResurtidos.cantidadSubResurtidosProcedure(resurtir.getClaveRes())
            for i in clave:
                for x in i:
                    total=x
            self.tabla.insert(parent='',index='end',iid=count, text=resurtir.getClaveRes(),
                values=(resurtir.getFechaRes(),resurtir.getTotalRes(),proveedor.getNomEmpProv(),total,resurtir.getClaveTie()))
            count += 1

    def onLimpiarTabla(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
    
    def onSalir(self):
        for conElement in self.container.winfo_children():
            if not isinstance(conElement,Menu):
                conElement.destroy()
        
ventana = Ventana()
ventana.mainloop()