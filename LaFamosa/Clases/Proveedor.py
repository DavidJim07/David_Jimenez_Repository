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