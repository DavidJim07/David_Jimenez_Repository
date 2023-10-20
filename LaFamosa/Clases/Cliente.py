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