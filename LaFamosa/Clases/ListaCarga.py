class ListaCarga:
    def __init__(self,**kwargs):
        for kwarg in kwargs:
            if kwarg=="num_liscar":
                self.__num_liscar = kwargs[kwarg]
            if kwarg=="cve_dat":
                self.__cve_dat = kwargs[kwarg]
            if kwarg=="cve_env":
                self.__cve_env = kwargs[kwarg]
    
    def setNumLisCar(self,num_liscar):
        self.__num_liscar=num_liscar    
    def getNumLisCar(self):
        return self.__num_liscar

    def setClaveDat(self,cve_dat):
        self.__cve_dat=cve_dat    
    def getClaveDat(self):
        return self.__cve_dat

    def setClaveEnv(self,cve_env):
        self.__cve_env=cve_env    
    def getClaveEnv(self):
        return self.__cve_env