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