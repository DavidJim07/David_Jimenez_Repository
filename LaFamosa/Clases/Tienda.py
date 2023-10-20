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