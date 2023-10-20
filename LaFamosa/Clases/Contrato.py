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