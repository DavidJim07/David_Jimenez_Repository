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