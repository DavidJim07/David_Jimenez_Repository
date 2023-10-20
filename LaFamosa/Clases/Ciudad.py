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