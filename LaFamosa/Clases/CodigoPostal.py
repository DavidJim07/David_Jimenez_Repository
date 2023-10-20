class CodigoPostal:
    def __init__(self,**kwargs):
        for kwarg in kwargs:
            if kwarg=="cve_cod":
                self.__cve_cod = kwargs[kwarg]
            if kwarg=="cve_ciu":
                self.__cve_ciu = kwargs[kwarg]               

    def setClaveCod(self,cve_cod):
        self.__cve_cod=cve_cod    
    def getClaveCod(self):
        return self.__cve_cod

    def setClaveCiu(self,cve_ciu):
        self.__cve_ciu=cve_ciu    
    def getClaveCiu(self):
        return self.__cve_ciu