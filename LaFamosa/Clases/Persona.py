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

    def salidaNombre(self):
        return f"{self.__nom_per} {self.__ap_per} {self.__am_per}"   

    def parteDomicilio(self):
         return f"{self.__calle_per} {self.__orientacion_per} #{self.__numDomicilio_per}, "   

    