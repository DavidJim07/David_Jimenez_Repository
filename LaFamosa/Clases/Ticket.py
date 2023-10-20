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

    