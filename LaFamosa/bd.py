class Estado:
    def __init__(self,**kwargs):
        for kwarg in kwargs:
            if kwarg=="cve_est":
                self.__cve_est = kwargs[kwarg]
            if kwarg=="nom_est":
                self.__nom_est = kwargs[kwarg]

    def setClaveEst(self,cve_est):
        self.__cve_est=cve_est    
    def getClaveEst(self):
        return self.__cve_est

    def setNomEst(self,nom_est):
        self.__nom_est=nom_est  
    def getNomEst(self):
        return self.__nom_est

class Ciudad:
    def __init__(self,**kwargs):
        for kwarg in kwargs:
            if kwarg=="cve_ciu":
                self.__cve_ciu = kwargs[kwarg]
            if kwarg=="nom_ciu":
                self.__nom_ciu = kwargs[kwarg]
            if kwarg=="cve_est":
                self.__cve_est = kwargs[kwarg]                

    def setClaveCiu(self,cve_ciu):
        self.__cve_ciu=cve_ciu    
    def getClaveCiu(self):
        return self.__cve_ciu

    def setNomCiu(self,nom_ciu):
        self.__nom_ciu=nom_ciu  
    def getNomCiu(self):
        return self.__nom_ciu

    def setClaveEst(self,cve_est):
        self.__cve_est=cve_est    
    def getClaveEst(self):
        return self.__cve_est

class CodigoPostal:
    def __init__(self,**kwargs):
        for kwarg in kwargs:
            if kwarg=="cve_cod":
                self.__cve_cod = kwargs[kwarg]
            if kwarg=="cve_ciu":
                self.__cve_ciu = kwargs[kwarg]               

    def setClaveCod(self,cve_cod):
        self.__cve_cod=cve_cod    
    def getClaveCod(self):
        return self.__cve_cod

    def setClaveCiu(self,cve_ciu):
        self.__cve_ciu=cve_ciu    
    def getClaveCiu(self):
        return self.__cve_ciu

class Colonia:
    def __init__(self,**kwargs):
        for kwarg in kwargs:
            if kwarg=="cve_col":
                self.__cve_col = kwargs[kwarg]
            if kwarg=="nom_col":
                self.__nom_col = kwargs[kwarg]
            if kwarg=="cve_cod":
                self.__cve_cod = kwargs[kwarg]                

    def setClaveCol(self,cve_col):
        self.__cve_col=cve_col    
    def getClaveCol(self):
        return self.__cve_col

    def setNomCol(self,nom_col):
        self.__nom_col=nom_col  
    def getNomCol(self):
        return self.__nom_col

    def setClaveCod(self,cve_cod):
        self.__cve_cod=cve_cod    
    def getClaveCod(self):
        return self.__cve_cod

class Persona:
    def __init__(self,**kwargs):
        for kwarg in kwargs:
            if kwarg=="cve_per":
                self.__cve_per = kwargs[kwarg]
            if kwarg=="nom_per":
                self.__nom_per = kwargs[kwarg]
            if kwarg=="ap_per":
                self.__ap_per = kwargs[kwarg]
            if kwarg=="am_per":
                self.__am_per = kwargs[kwarg]
            if kwarg=="calle_per":
                self.__calle_per = kwargs[kwarg]
            if kwarg=="numDomicilio_per":
                self.__numDomicilio_per = kwargs[kwarg]
            if kwarg=="orientacion_per": 
                self.__orientacion_per = kwargs[kwarg]
            if kwarg=="entreCalles_per":
                self.__entreCalles_per = kwargs[kwarg]
            if kwarg=="tel_per":
                self.__tel_per = kwargs[kwarg]
            if kwarg=="mail_per":
                self.__mail_per = kwargs[kwarg]
            if kwarg=="sexo_per":
                self.__sexo_per = kwargs[kwarg]
            if kwarg=="fNacimiento_per":
                self.__fNacimiento_per = kwargs[kwarg]
            if kwarg=="edoCivil_per":
                self.__edoCivil_per = kwargs[kwarg]
            if kwarg=="cve_col":
                self.__cve_col = kwargs[kwarg]
            if kwarg=="CURP_per":
                self.CURP_per = kwargs[kwarg]

    def setClavePer(self,cve_per):
        self.__cve_per=cve_per    
    def getClavePer(self):
        return self.__cve_per

    def setNomPer(self,nom_per):
        self.__nom_per=nom_per  
    def getNomPer(self):
        return self.__nom_per

    def setApPer(self,ap_per):
        self.__ap_per=ap_per  
    def getApPer(self):
        return self.__ap_per

    def setAmPer(self,am_per):
        self.__am_per=am_per  
    def getAmPer(self):
        return self.__am_per

    def setCallePer(self,calle_per):
        self.__calle_per=calle_per  
    def getCallePer(self):
        return self.__calle_per

    def setNumDomPer(self,num_per):
        self.__numDomicilio_per=num_per  
    def getNumDomPer(self):
        return self.__numDomicilio_per

    def setOrientacionPer(self,orientacion_per):
        self.__orientacion_per=orientacion_per  
    def getOrientacionPer(self):
        return self.__orientacion_per   

    def setEntreCallesPer(self,entreCalles_per):
        self.__entreCalles_per=entreCalles_per  
    def getEntreCallesPer(self):
        return self.__entreCalles_per

    def setTelefonoPer(self,tel_per):
        self.__tel_per=tel_per  
    def getTelefonoPer(self):
        return self.__tel_per 

    def setMailPer(self,mail_per):
        self.__mail_per=mail_per  
    def getMailPer(self):
        return self.__mail_per  

    def setSexoPer(self,sexo_per):
        self.__sexo_per=sexo_per  
    def getSexoPer(self):
        return self.__sexo_per

    def setFnacimientoPer(self,fNacimiento_per):
        self.__fNacimiento_per=fNacimiento_per  
    def getFnacimientoPer(self):
        return self.__fNacimiento_per

    def setEdoCivilPer(self,edoCivil_per):
        self.__edoCivil_per=edoCivil_per  
    def getEdoCivilPer(self):
        return self.__edoCivil_per

    def setColPer(self,cve_col):
        self.__cve_col=cve_col  
    def getColPer(self):
        return self.__cve_col   

    def setCURPPer(self,CURP_per):
        self.__CURP_per=CURP_per  
    def getCURPPer(self):
        return self.__CURP_per

    def salidaNombre(self):
        return f"{self.__nom_per} {self.__ap_per} {self.__am_per}"   

    def parteDomicilio(self):
         return f"{self.__calle_per} {self.__orientacion_per} #{self.__numDomicilio_per}, "   

class Tienda:
    def __init__(self,**kwargs):
        for kwarg in kwargs:
            if kwarg=="cve_tie":
                self.__cve_tie = kwargs[kwarg]
            if kwarg=="fechaApertura_tie":
                self.__fechaApertura_tie = kwargs[kwarg]
            if kwarg=="calle_tie":
                self.__calle_tie = kwargs[kwarg]
            if kwarg=="numDomiclio_tie":
                self.__numDomiclio_tie = kwargs[kwarg]
            if kwarg=="orientacion_tie": 
                self.__orientacion_tie = kwargs[kwarg]
            if kwarg=="entreCalles_tie":
                self.__entreCalles_tie = kwargs[kwarg]
            if kwarg=="tel_tie": 
                self.__tel_tie = kwargs[kwarg]
            if kwarg=="mail_tie":
                self.__mail_tie = kwargs[kwarg]
            if kwarg=="cve_col":
                self.__cve_col = kwargs[kwarg]

    def setClaveTie(self,cve_tie):
        self.__cve_tie=cve_tie    
    def getClaveTie(self):
        return self.__cve_tie

    def setFaperturaTie(self,fechaApertura_tie):
        self.__fechaApertura_tie=fechaApertura_tie  
    def getFaperturaTie(self):
        return self.__fechaApertura_tie

    def setCalleTie(self,calle_tie):
        self.__calle_tie=calle_tie  
    def getCalleTie(self):
        return self.__calle_tie

    def setNumDomTie(self,numDomiclio_tie):
        self.__numDomiclio_tie=numDomiclio_tie  
    def getNumDomTie(self):
        return self.__numDomiclio_tie  

    def setOrientacionTie(self,orientacion_tie):
        self.__orientacion_tie=orientacion_tie  
    def getOrientacionTie(self):
        return self.__orientacion_tie 

    def setEntreCallesTie(self,entreCalles_tie):
        self.__entreCalles_tie=entreCalles_tie  
    def getEntreCallesTie(self):
        return self.__entreCalles_tie

    def setTelefonoTie(self,tel_tie):
        self.__tel_tie=tel_tie  
    def getTelefonoTie(self):
        return self.__tel_tie 

    def setMailTie(self,mail_tie):
        self.__mail_tie=mail_tie  
    def getMailTie(self):
        return self.__mail_tie  

    def setClaveCol(self,cve_col):
        self.__cve_col=cve_col  
    def getClaveCol(self):
        return self.__cve_col

    def parteDomicilio(self):
         return f"{self.__calle_tie} {self.__orientacion_tie} #{self.__numDomiclio_tie}, "

class Contrato:
    def __init__(self,**kwargs):
        for kwarg in kwargs:
            if kwarg=="folio_con":
                self.__folio_con = kwargs[kwarg]
            if kwarg=="fechaInicio_con":
                self.__fechaInicio_con = kwargs[kwarg]
            if kwarg=="fechaFin_con":
                self.__fechaFin_con = kwargs[kwarg]
            if kwarg=="puesto_con":
                self.__puesto_con = kwargs[kwarg]
            if kwarg=="sueldo_con":
                self.__sueldo_con = kwargs[kwarg]
            if kwarg=="periodoSueldo_con": 
                self.__periodoSueldo_con = kwargs[kwarg]
            if kwarg=="hEntrada_con":
                self.__hEntrada_con = kwargs[kwarg]
            if kwarg=="hSalida_con":
                self.__hSalida_con = kwargs[kwarg]
            if kwarg=="hInicioComida_con":
                self.__hInicioComida_con = kwargs[kwarg]
            if kwarg=="hFinComida_con":
                self.__hFinComida_con = kwargs[kwarg]
            if kwarg=="comisiones_con":
                self.__comisiones_con = kwargs[kwarg]
            if kwarg=="cve_tie":
                self.__cve_tie = kwargs[kwarg]
            if kwarg=="cve_per":
                self.__cve_per = kwargs[kwarg]

    def setClaveCon(self,folio_con):
        self.__folio_con=folio_con    
    def getClaveCon(self):
        return self.__folio_con

    def setFechaInicioCon(self,fechaInicio_con):
        self.__fechaInicio_con=fechaInicio_con    
    def getFechaInicioCon(self):
        return self.__fechaInicio_con

    def setFechaFinCon(self,fechaFin_con):
        self.__fechaFin_con=fechaFin_con    
    def getFechaFinCon(self):
        return self.__fechaFin_con

    def setPuestoCon(self,puesto_con):
        self.__puesto_con=puesto_con    
    def getPuestoCon(self):
        return self.__puesto_con

    def setSueldoCon(self,sueldo_con):
        self.__sueldo_con=sueldo_con    
    def getSueldoCon(self):
        return self.__sueldo_con

    def setPeriodoSueldoCon(self,periodoSueldo_con):
        self.__periodoSueldo_con=periodoSueldo_con    
    def getPeriodoSueldoCon(self):
        return self.__periodoSueldo_con

    def setHentradaCon(self,hEntrada_con):
        self.__hEntrada_con=hEntrada_con    
    def getHentradaCon(self):
        return self.__hEntrada_con

    def setHsalidaCon(self,hSalida_con):
        self.__hSalida_con=hSalida_con    
    def getHsalidaCon(self):
        return self.__hSalida_con

    def setHIniComidaCon(self,hInicioComida_con):
        self.__hInicioComida_con=hInicioComida_con    
    def getHIniComidaCon(self):
        return self.__hInicioComida_con

    def setHFinComidaCon(self,hFinComida_con):
        self.__hFinComida_con=hFinComida_con    
    def getHFinComidaCon(self):
        return self.__hFinComida_con

    def setComisionesCon(self,comisiones_con):
        self.__comisiones_con=comisiones_con    
    def getComisionesCon(self):
        return self.__comisiones_con

    def setClaveTie(self,cve_tie):
        self.__cve_tie=cve_tie    
    def getClaveTie(self):
        return self.__cve_tie

    def setClavePer(self,cve_per):
        self.__cve_per=cve_per    
    def getClavePer(self):
        return self.__cve_per        

class Checador:
    def __init__(self,**kwargs):
        for kwarg in kwargs:
            if kwarg=="num_che":
                self.__num_che = kwargs[kwarg]
            if kwarg=="hora_che":
                self.__hora_che = kwargs[kwarg]
            if kwarg=="tipo_che":
                self.__tipo_che = kwargs[kwarg]
            if kwarg=="folio_con":
                self.__folio_con = kwargs[kwarg]

    def setNumChe(self,num_che):
        self.__num_che=num_che    
    def getNumChe(self):
        return self.__num_che

    def setHoraChe(self,hora_che):
        self.__hora_che=hora_che    
    def getHoraChe(self):
        return self.__hora_che

    def setTipoChe(self,tipo_che):
        self.__tipo_che=tipo_che    
    def getTipoChe(self):
        return self.__tipo_che

    def setClaveCon(self,folio_con):
        self.__folio_con=folio_con    
    def getClaveCon(self):
        return self.__folio_con

class Proveedor:
    def __init__(self,**kwargs):
        for kwarg in kwargs:
            if kwarg=="cve_prov":
                self.__cve_prov = kwargs[kwarg]
            if kwarg=="nomEmpresa_prov":
                self.__nomEmpresa_prov = kwargs[kwarg]
            if kwarg=="calle_prov":
                self.__calle_prov = kwargs[kwarg]
            if kwarg=="numDomicilio_prov":
                self.__numDomicilio_prov = kwargs[kwarg]
            if kwarg=="orientacion_prov": 
                self.__orientacion_prov = kwargs[kwarg]
            if kwarg=="entreCalles_prov":
                self.__entreCalles_prov = kwargs[kwarg]
            if kwarg=="tel_prov":
                self.__tel_prov = kwargs[kwarg]
            if kwarg=="mail_prov":
                self.__mail_prov = kwargs[kwarg]
            if kwarg=="cve_col":
                self.__cve_col = kwargs[kwarg]

    def setClaveProv(self,cve_prov):
        self.__cve_prov=cve_prov    
    def getClaveProv(self):
        return self.__cve_prov

    def setNomEmpProv(self,nomEmpresa_prov):
        self.__nomEmpresa_prov=nomEmpresa_prov  
    def getNomEmpProv(self):
        return self.__nomEmpresa_prov

    def setCalleProv(self,calle_prov):
        self.__calle_prov=calle_prov  
    def getCalleProv(self):
        return self.__calle_prov

    def setNumDomProv(self,numDomicilio_prov):
        self.__numDomicilio_prov=numDomicilio_prov  
    def getNumDomProv(self):
        return self.__numDomicilio_prov

    def setOrientacionProv(self,orientacion_prov):
        self.__orientacion_prov=orientacion_prov  
    def getOrientacionProv(self):
        return self.__orientacion_prov    

    def setEntreCallesProv(self,entreCalles_prov):
        self.__entreCalles_prov=entreCalles_prov  
    def getEntreCallesProv(self):
        return self.__entreCalles_prov 

    def setTelefonoProv(self,tel_prov):
        self.__tel_prov=tel_prov  
    def getTelefonoProv(self):
        return self.__tel_prov 

    def setMailProv(self,mail_prov):
        self.__mail_prov=mail_prov  
    def getMailProv(self):
        return self.__mail_prov

    def setClaveCol(self,cve_col):
        self.__cve_col=cve_col  
    def getClaveCol(self):
        return self.__cve_col

    def parteDomicilio(self):
         return f"{self.__calle_prov}  #{self.__numDomicilio_prov}, " 

class Representante:
    def __init__(self,**kwargs):
        for kwarg in kwargs:
            if kwarg=="num_rep":
                self.__num_rep = kwargs[kwarg]
            if kwarg=="fecha_rep":
                self.__fecha_rep = kwargs[kwarg]
            if kwarg=="cve_per":
                self.__cve_per = kwargs[kwarg]
            if kwarg=="cve_prov":
                self.__cve_prov = kwargs[kwarg]

    def setNumRep(self,num_rep):
        self.__num_rep=num_rep    
    def getNumRep(self):
        return self.__num_rep

    def setFechaRep(self,fecha_rep):
        self.__fecha_rep=fecha_rep    
    def getFechaRep(self):
        return self.__fecha_rep

    def setClavePer(self,cve_per):
        self.__cve_per=cve_per    
    def getClavePer(self):
        return f'{self.__cve_per}'

    def setClaveProv(self,cve_prov):
        self.__cve_prov=cve_prov    
    def getClaveProv(self):
        return self.__cve_prov

class Producto:
    def __init__(self,**kwargs):
        for kwarg in kwargs:
            if kwarg=="codbar_pro":
                self.__codbar_pro = kwargs[kwarg]
            if kwarg=="nom_pro":
                self.__nom_pro = kwargs[kwarg]
            if kwarg=="tipo_pro":
                self.__tipo_pro = kwargs[kwarg]
            if kwarg=="marca_pro":
                self.__marca_pro = kwargs[kwarg]
            if kwarg=="color_pro":
                self.__color_pro = kwargs[kwarg]
            if kwarg=="garantia_pro":
                self.__garantia_pro = kwargs[kwarg]
            if kwarg=="uMedidaGarantia_pro": 
                self.__uMedidaGarantia_pro = kwargs[kwarg]
            if kwarg=="presentacion_pro":
                self.__presentacion_pro = kwargs[kwarg]
            if kwarg=="modelo_pro":
                self.__modelo_pro = kwargs[kwarg]
            if kwarg=="alto_pro":
                self.__alto_pro = kwargs[kwarg]
            if kwarg=="largo_pro":
                self.__largo_pro = kwargs[kwarg]
            if kwarg=="ancho_pro":
                self.__ancho_pro = kwargs[kwarg]
            if kwarg=="contenido_pro":
                self.__contenido_pro = kwargs[kwarg]
            if kwarg=="uMedida_pro":
                self.__uMedida_pro = kwargs[kwarg]
            if kwarg=="codigo_pro":
                self.__codigo_pro = kwargs[kwarg]

    def setCodbarPro(self,codbar_pro):
        self.__codbar_pro=codbar_pro    
    def getCodbarPro(self):
        return self.__codbar_pro

    def setNomPro(self,nom_pro):
        self.__nom_pro=nom_pro  
    def getNomPro(self):
        return self.__nom_pro

    def setTipoPro(self,tipo_pro):
        self.__tipo_pro=tipo_pro  
    def getTipoPro(self):
        return self.__tipo_pro

    def setMarcaPro(self,marca_pro):
        self.__marca_pro=marca_pro  
    def getMarcaPro(self):
        return self.__marca_pro

    def setColorPro(self,color_pro):
        self.__color_pro=color_pro  
    def getColorPro(self):
        return self.__color_pro

    def setGarantiaPro(self,garantia_pro):
        self.__garantia_pro=garantia_pro  
    def getGarantiaPro(self):
        return self.__garantia_pro

    def setUmedidaGarantiaPro(self,uMedidaGarantia_pro):
        self.__uMedidaGarantia_pro=uMedidaGarantia_pro  
    def getUmedidaGarantiaPro(self):
        return self.__uMedidaGarantia_pro   

    def setPresentacionPro(self,presentacion_pro):
        self.__presentacion_pro=presentacion_pro  
    def getPresentacionPro(self):
        return self.__presentacion_pro

    def setModeloPro(self,modelo_pro):
        self.__modelo_pro=modelo_pro  
    def getModeloPro(self):
        return self.__modelo_pro 

    def setAltoPro(self,alto_pro):
        self.__alto_pro=alto_pro  
    def getAltoPro(self):
        return self.__alto_pro  

    def setLargoPro(self,largo_pro):
        self.__largo_pro=largo_pro  
    def getLargoPro(self):
        return self.__largo_pro

    def setAnchoPro(self,ancho_pro):
        self.__ancho_pro=ancho_pro  
    def getAnchoPro(self):
        return self.__ancho_pro

    def setContenidoPro(self,contenido_pro):
        self.__contenido_pro=contenido_pro  
    def getContenidoPro(self):
        return self.__contenido_pro

    def setUmedidaPro(self,uMedida_pro):
        self.__uMedida_pro=uMedida_pro  
    def getUmedidaPro(self):
        return self.__uMedida_pro  

    def setCodigoPro(self,codigo_pro):
        self.__codigo_pro=codigo_pro  
    def getCodigoPro(self):
        return self.__codigo_pro 

class MinMax:
    def __init__(self,**kwargs):
        for kwarg in kwargs:
            if kwarg=="num_minmax":
                self.__num_minmax = kwargs[kwarg]
            if kwarg=="min_minmax":
                self.__min_minmax = kwargs[kwarg]
            if kwarg=="max_minmax":
                self.__max_minmax = kwargs[kwarg]
            if kwarg=="codbar_pro":
                self.__codbar_pro = kwargs[kwarg]
            if kwarg=="cve_tie":
                self.__cve_tie = kwargs[kwarg]

    def setNumMinMax(self,num_minmax):
        self.__num_minmax=num_minmax    
    def getNumMinMax(self):
        return self.__num_minmax

    def setMinMinMax(self,min_minmax):
        self.__min_minmax=min_minmax    
    def getMinMinMax(self):
        return self.__min_minmax

    def setMaxMinMax(self,max_minmax):
        self.__max_minmax=max_minmax    
    def getMaxMinMax(self):
        return self.__max_minmax

    def setClaveTie(self,cve_tie):
        self.__cve_tie=cve_tie    
    def getClaveTie(self):
        return self.__cve_tie

    def setCodbarPro(self,codbar_pro):
        self.__codbar_pro=codbar_pro    
    def getCodbarPro(self):
        return self.__codbar_pro                

class Resurtir:
    def __init__(self,**kwargs):
        for kwarg in kwargs:
            if kwarg=="cve_res":
                self.__cve_res = kwargs[kwarg]
            if kwarg=="fecha_res":
                self.__fecha_res = kwargs[kwarg]
            if kwarg=="total_res":
                self.__total_res = kwargs[kwarg]
            if kwarg=="cve_prov":
                self.__cve_prov = kwargs[kwarg]
            if kwarg=="cve_tie":
                self.__cve_tie = kwargs[kwarg]

    def setClaveRes(self,cve_res):
        self.__cve_res=cve_res    
    def getClaveRes(self):
        return self.__cve_res

    def setFechaRes(self,fecha_res):
        self.__fecha_res=fecha_res    
    def getFechaRes(self):
        return self.__fecha_res

    def setTotalRes(self,total_res):
        self.__total_res=total_res    
    def getTotalRes(self):
        return self.__total_res

    def setClaveProv(self,cve_prov):
        self.__cve_prov=cve_prov    
    def getClaveProv(self):
        return self.__cve_prov

    def setClaveTie(self,cve_tie):
        self.__cve_tie=cve_tie    
    def getClaveTie(self):
        return self.__cve_tie

class RenglonResurtir:
    def __init__(self,**kwargs):
        for kwarg in kwargs:
            if kwarg=="num_renres":
                self.__num_renres = kwargs[kwarg]
            if kwarg=="cantidad_renres":
                self.__cantidad_renres = kwargs[kwarg]
            if kwarg=="baja_renres":
                self.__baja_renres = kwargs[kwarg]
            if kwarg=="fCaducidad_renres":
                self.__fCaducidad_renres = kwargs[kwarg]
            if kwarg=="precio_renres":
                self.__precio_renres = kwargs[kwarg]
            if kwarg=="codbar_pro":
                self.__codbar_pro = kwargs[kwarg]
            if kwarg=="cve_res":
                self.__cve_res = kwargs[kwarg]

    def setNumRenRes(self,num_renres):
        self.__num_renres=num_renres    
    def getNumRenRes(self):
        return self.__num_renres

    def setCantidadRenRes(self,cantidad_renres):
        self.__cantidad_renres=cantidad_renres    
    def getCantidadRenRes(self):
        return self.__cantidad_renres

    def setBajaRenRes(self,baja_renres):
        self.__baja_renres=baja_renres    
    def getBajaRenRes(self):
        return self.__baja_renres

    def setfCaducidadRenREs(self,fCaducidad_renres):
        self.__fCaducidad_renres=fCaducidad_renres    
    def getfCaducidadRenREs(self):
        return self.__fCaducidad_renres

    def setPrecioRenRes(self,precio_renres):
        self.__precio_renres=precio_renres    
    def getPrecioRenRes(self):
        return self.__precio_renres
    
    def setCodbarPro(self,codbar_pro):
        self.__codbar_pro=codbar_pro    
    def getCodbarPro(self):
        return self.__codbar_pro
        
    def setClaveRes(self,cve_res):
        self.__cve_res=cve_res    
    def getClaveRes(self):
        return self.__cve_res

class Vehiculo:
    def __init__(self,**kwargs):
        for kwarg in kwargs:
            if kwarg=="ns_veh":
                self.__ns_veh = kwargs[kwarg]
            if kwarg=="modelo_veh":
                self.__modelo_veh = kwargs[kwarg]
            if kwarg=="marca_veh":
                self.__marca_veh = kwargs[kwarg]
            if kwarg=="color_veh":
                self.__color_veh = kwargs[kwarg]
            if kwarg=="cantPuertas_veh":
                self.__cantPuertas_veh = kwargs[kwarg]
            if kwarg=="año_veh":
                self.__año_veh = kwargs[kwarg]
            if kwarg=="precioCompra_veh": 
                self.__precioCompra_veh = kwargs[kwarg]
            if kwarg=="tipo_veh":
                self.__tipo_veh = kwargs[kwarg]
            if kwarg=="cve_tie":
                self.__cve_tie = kwargs[kwarg]

    def setNumSerieVeh(self,ns_veh):
        self.__ns_veh=ns_veh  
    def getNumSerieVeh(self):
        return self.__ns_veh

    def setModeloVeh(self,modelo_veh):
        self.__modelo_veh=modelo_veh  
    def getModeloVeh(self):
        return self.__modelo_veh

    def setMarcaVeh(self,marca_veh):
        self.__marca_veh=marca_veh  
    def getMarcaVeh(self):
        return self.__marca_veh

    def setColorVeh(self,color_veh):
        self.__color_veh=color_veh  
    def getColorVeh(self):
        return self.__color_veh

    def setCantPuertasVeh(self,cantPuertas_veh):
        self.__cantPuertas_veh=cantPuertas_veh  
    def getCantPuertasVeh(self):
        return self.__cantPuertas_veh

    def setAñoVeh(self,año_veh):
        self.__año_veh=año_veh  
    def getAñoVeh(self):
        return self.__año_veh   

    def setPrecioCompraVeh(self,precioCompra_veh):
        self.__precioCompra_veh=precioCompra_veh  
    def getPrecioCompraVeh(self):
        return self.__precioCompra_veh

    def setTipoVeh(self,tipo_veh):
        self.__tipo_veh=tipo_veh  
    def getTipoVeh(self):
        return self.__tipo_veh 

    def setClaveTie(self,cve_tie):
        self.__cve_tie=cve_tie    
    def getClaveTie(self):
        return self.__cve_tie

class StatusVehiculo:
    def __init__(self,**kwargs):
        for kwarg in kwargs:
            if kwarg=="num_sta":
                self.__num_sta = kwargs[kwarg]
            if kwarg=="fecha_sta":
                self.__fecha_sta = kwargs[kwarg]
            if kwarg=="status_sta":
                self.__status_sta = kwargs[kwarg]
            if kwarg=="ns_veh":
                self.__ns_veh = kwargs[kwarg]

    def setNumSta(self,num_sta):
        self.__num_sta=num_sta  
    def getNumSta(self):
        return self.__num_sta

    def setFechaSta(self,fecha_sta):
        self.__fecha_sta=fecha_sta  
    def getFechaSta(self):
        return self.__fecha_sta

    def setStatusSta(self,status_sta):
        self.__status_sta=status_sta  
    def getStatusSta(self):
        return self.__status_sta
    
    def setNumSerieVeh(self,ns_veh):
        self.__ns_veh=ns_veh  
    def getNumSerieVeh(self):
        return self.__ns_veh

class Cliente:
    def __init__(self,**kwargs):
        for kwarg in kwargs:
            if kwarg=="cve_clie":
                self.__cve_clie = kwargs[kwarg]
            if kwarg=="fecha_clie":
                self.__fecha_clie = kwargs[kwarg]
            if kwarg=="cve_per":
                self.__cve_per = kwargs[kwarg]

    def setClaveClie(self,cve_clie):
        self.__cve_clie=cve_clie    
    def getClaveClie(self):
        return self.__cve_clie

    def setFechaClie(self,fecha_clie):
        self.__fecha_clie=fecha_clie  
    def getFechaClie(self):
        return self.__fecha_clie

    def setClavePer(self,cve_per):
        self.__cve_per=cve_per    
    def getClavePer(self):
        return self.__cve_per

class Ticket:
    def __init__(self,**kwargs):
        for kwarg in kwargs:
            if kwarg=="folio_tic":
                self.__folio_tic = kwargs[kwarg]
            if kwarg=="fechaVenta_tic":
                self.__fechaVenta_tic = kwargs[kwarg]
            if kwarg=="finGarantia_tic":
                self.__finGarantia_tic = kwargs[kwarg]
            if kwarg=="precioVenta_tic":
                self.__precioVenta_tic = kwargs[kwarg]
            if kwarg=="descuento_tic":
                self.__descuento_tic = kwargs[kwarg]
            if kwarg=="cantidad_tic":
                self.__cantidad_tic = kwargs[kwarg]
            if kwarg=="formaPago_tic": 
                self.__formaPago_tic = kwargs[kwarg]
            if kwarg=="numTarjeta_tic":
                self.__numTarjeta_tic = kwargs[kwarg]
            if kwarg=="institucionBancaria_tic":
                self.__institucionBancaria_tic = kwargs[kwarg]
            if kwarg=="codbar_pro":
                self.__codbar_pro = kwargs[kwarg]
            if kwarg=="folio_con":
                self.__folio_con = kwargs[kwarg]
            if kwarg=="cve_tie":
                self.__cve_tie = kwargs[kwarg]
            if kwarg=="cve_clie":
                self.__cve_clie = kwargs[kwarg]

    def setFolioTic(self,folio_tic):
        self.__folio_tic=folio_tic    
    def getFolioTic(self):
        return self.__folio_tic

    def setFechaVentaTic(self,fechaVenta_tic):
        self.__fechaVenta_tic=fechaVenta_tic  
    def getFechaVentaTic(self):
        return self.__fechaVenta_tic

    def setFinGarantiaTic(self,finGarantia_tic):
        self.__finGarantia_tic=finGarantia_tic  
    def getFinGarantiaTic(self):
        return self.__finGarantia_tic

    def setPrecioVentaTic(self,precioVenta_tic):
        self.__precioVenta_tic=precioVenta_tic  
    def getPrecioVentaTic(self):
        return self.__precioVenta_tic

    def setDescuentoTic(self,descuento_tic):
        self.__descuento_tic=descuento_tic  
    def getDescuentoTic(self):
        return self.__descuento_tic

    def setCantidadTic(self,cantidad_tic):
        self.__cantidad_tic=cantidad_tic  
    def getCantidadTic(self):
        return self.__cantidad_tic

    def setFormaPagoTic(self,formaPago_tic):
        self.__formaPago_tic=formaPago_tic  
    def getFormaPagoTic(self):
        return self.__formaPago_tic   

    def setNumTarjetaTic(self,numTarjeta_tic):
        self.__numTarjeta_tic=numTarjeta_tic  
    def getNumTarjetaTic(self):
        return self.__numTarjeta_tic

    def setInstitucionBancariaTic(self,institucionBancaria_tic):
        self.__institucionBancaria_tic=institucionBancaria_tic  
    def getInstitucionBancariaTic(self):
        return self.__institucionBancaria_tic 

    def setCodbarPro(self,codbar_pro):
        self.__codbar_pro=codbar_pro    
    def getCodbarPro(self):
        return self.__codbar_pro  

    def setClaveCon(self,folio_con):
        self.__folio_con=folio_con    
    def getClaveCon(self):
        return self.__folio_con

    def setClaveTie(self,cve_tie):
        self.__cve_tie=cve_tie    
    def getClaveTie(self):
        return self.__cve_tie

    def setClaveClie(self,cve_clie):
        self.__cve_clie=cve_clie    
    def getClaveClie(self):
        return self.__cve_clie

class Acomodar:
    def __init__(self,**kwargs):
        for kwarg in kwargs:
            if kwarg=="cve_aco":
                self.__cve_aco = kwargs[kwarg]
            if kwarg=="fecha_aco":
                self.__fecha_aco = kwargs[kwarg]
            if kwarg=="cantidad_aco":
                self.__cantidad_aco = kwargs[kwarg]
            if kwarg=="lugar_aco":
                self.__lugar_aco = kwargs[kwarg]
            if kwarg=="num_renres":
                self.__num_renres = kwargs[kwarg]
            if kwarg=="cve_tie":
                self.__cve_tie = kwargs[kwarg]

    def setClaveAco(self,cve_aco):
        self.__cve_aco=cve_aco    
    def getClaveAco(self):
        return self.__cve_aco

    def setFechaAco(self,fecha_aco):
        self.__fecha_aco=fecha_aco  
    def getFechaAco(self):
        return self.__fecha_aco

    def setCantidadAco(self,cantidad_aco):
        self.__cantidad_aco=cantidad_aco  
    def getCantidadAco(self):
        return self.__cantidad_aco

    def setLugarAco(self,lugar_aco):
        self.__lugar_aco=lugar_aco  
    def getLugarAco(self):
        return self.__lugar_aco

    def setNumRenRes(self,num_renres):
        self.__num_renres=num_renres    
    def getNumRenRes(self):
        return self.__num_renres

    def setClaveTie(self,cve_tie):
        self.__cve_tie=cve_tie    
    def getClaveTie(self):
        return self.__cve_tie

class Devolucion:
    def __init__(self,**kwargs):
        for kwarg in kwargs:
            if kwarg=="cve_dev":
                self.__cve_dev = kwargs[kwarg]
            if kwarg=="motivo_dev":
                self.__motivo_dev = kwargs[kwarg]
            if kwarg=="fecha_dev":
                self.__fecha_dev = kwargs[kwarg]
            if kwarg=="folio_tic":
                self.__folio_tic = kwargs[kwarg]

    def setClaveDev(self,cve_dev):
        self.__cve_dev=cve_dev    
    def getClaveDev(self):
        return self.__cve_dev

    def setMotivoDev(self,motivo_dev):
        self.__motivo_dev=motivo_dev  
    def getMotivoDev(self):
        return self.__motivo_dev

    def setFechaDev(self,fecha_dev):
        self.__fecha_dev=fecha_dev  
    def getFechaDev(self):
        return self.__fecha_dev

    def setFolioTic(self,folio_tic):
        self.__folio_tic=folio_tic    
    def getFolioTic(self):
        return self.__folio_tic

class DatoEnvio:
    def __init__(self,**kwargs):
        for kwarg in kwargs:
            if kwarg=="cve_dat":
                self.__cve_dat = kwargs[kwarg]
            if kwarg=="calle_dat":
                self.__calle_dat = kwargs[kwarg]
            if kwarg=="numDomicilio_dat":
                self.__numDomicilio_dat = kwargs[kwarg]
            if kwarg=="orientacion_dat": 
                self.__orientacion_dat = kwargs[kwarg]
            if kwarg=="entreCalles_dat":
                self.__entreCalles_dat = kwargs[kwarg]
            if kwarg=="cve_col":
                self.__cve_col = kwargs[kwarg]
            if kwarg=="folio_tic":
                self.__folio_tic = kwargs[kwarg]

    def setClaveDat(self,cve_dat):
        self.__cve_dat=cve_dat    
    def getClaveDat(self):
        return self.__cve_dat

    def setCalleDat(self,calle_dat):
        self.__calle_dat=calle_dat  
    def getCalleDat(self):
        return self.__calle_dat

    def setNumDomDat(self,numDomicilio_dat):
        self.__numDomicilio_dat=numDomicilio_dat  
    def getNumDomDat(self):
        return self.__numDomicilio_dat

    def setOrientacionDat(self,orientacion_dat):
        self.__orientacion_dat=orientacion_dat  
    def getOrientacionDat(self):
        return self.__orientacion_dat    

    def setEntreCallesDat(self,entreCalles_dat):
        self.__entreCalles_dat=entreCalles_dat  
    def getEntreCallesDat(self):
        return self.__entreCalles_dat 

    def setTelefonoDat(self,tel_Dat):
        self.__tel_Dat=tel_Dat  
    def getTelefonoDat(self):
        return self.__tel_Dat 

    def setMailDat(self,mail_Dat):
        self.__mail_Dat=mail_Dat  
    def getMailDat(self):
        return self.__mail_Dat

    def setClaveCol(self,cve_col):
        self.__cve_col=cve_col  
    def getClaveCol(self):
        return self.__cve_col

    def setFolioTic(self,folio_tic):
        self.__folio_tic=folio_tic    
    def getFolioTic(self):
        return self.__folio_tic

    def parteDomicilio(self):
         return f"{self.__calle_dat}  #{self.__numDomicilio_dat}, " 

class Enviar:
    def __init__(self,**kwargs):
        for kwarg in kwargs:
            if kwarg=="cve_env":
                self.__cve_env = kwargs[kwarg]
            if kwarg=="fecha_env":
                self.__fecha_env = kwargs[kwarg]
            if kwarg=="ns_veh":
                self.__ns_veh = kwargs[kwarg]
            if kwarg=="folio_con":
                self.__folio_con = kwargs[kwarg]
    
    def setClaveEnv(self,cve_env):
        self.__cve_env=cve_env    
    def getClaveEnv(self):
        return self.__cve_env

    def setFechaEnv(self,fecha_env):
        self.__fecha_env=fecha_env  
    def getFechaEnv(self):
        return self.__fecha_env

    def setNumSerieVeh(self,ns_veh):
        self.__ns_veh=ns_veh  
    def getNumSerieVeh(self):
        return self.__ns_veh

    def setClaveCon(self,folio_con):
        self.__folio_con=folio_con    
    def getClaveCon(self):
        return self.__folio_con

class ListaCarga:
    def __init__(self,**kwargs):
        for kwarg in kwargs:
            if kwarg=="num_liscar":
                self.__num_liscar = kwargs[kwarg]
            if kwarg=="cve_dat":
                self.__cve_dat = kwargs[kwarg]
            if kwarg=="cve_env":
                self.__cve_env = kwargs[kwarg]
    
    def setNumLisCar(self,num_liscar):
        self.__num_liscar=num_liscar    
    def getNumLisCar(self):
        return self.__num_liscar

    def setClaveDat(self,cve_dat):
        self.__cve_dat=cve_dat    
    def getClaveDat(self):
        return self.__cve_dat

    def setClaveEnv(self,cve_env):
        self.__cve_env=cve_env    
    def getClaveEnv(self):
        return self.__cve_env

class Status:
    def __init__(self,**kwargs):
        for kwarg in kwargs:
            if kwarg=="num_sta":
                self.__num_sta = kwargs[kwarg]
            if kwarg=="fecha_sta":
                self.__fecha_sta = kwargs[kwarg]
            if kwarg=="status_sta":
                self.__status_sta = kwargs[kwarg]
            if kwarg=="num_liscar":
                self.__num_liscar = kwargs[kwarg]

    def setNumStatus(self,num_sta):
        self.__num_sta=num_sta    
    def getNumStatus(self):
        return self.__num_sta

    def setFechaSta(self,fecha_sta):
        self.__fecha_sta=fecha_sta  
    def getFechaSta(self):
        return self.__fecha_sta

    def setStatusSta(self,status_sta):
        self.__status_sta=status_sta  
    def getStatusSta(self):
        return self.__status_sta
            
    def setNumLisCar(self,num_liscar):
        self.__num_liscar=num_liscar    
    def getNumLisCar(self):
        return self.__num_liscar

class PrecioVenta:
    def __init__(self,**kwargs):
        for kwarg in kwargs:
            if kwarg=="cve_pre":
                self.__cve_pre = kwargs[kwarg]
            if kwarg=="fecha_pre":
                self.__fecha_pre = kwargs[kwarg]
            if kwarg=="precio_pre":
                self.__precio_pre = kwargs[kwarg]
            if kwarg=="codbar_pro":
                self.__codbar_pro = kwargs[kwarg]

    def setClavePre(self,cve_pre):
        self.__cve_pre=cve_pre    
    def getClavePre(self):
        return self.__cve_pre

    def setFechaPre(self,fecha_pre):
        self.__fecha_pre=fecha_pre  
    def getFechaPre(self):
        return self.__fecha_pre

    def setPrecioPre(self,precio_pre):
        self.__precio_pre=precio_pre  
    def getPrecioPre(self):
        return self.__precio_pre
    
    def setCodbarPro(self,codbar_pro):
        self.__codbar_pro=codbar_pro    
    def getCodbarPro(self):
        return self.__codbar_pro