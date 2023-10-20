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