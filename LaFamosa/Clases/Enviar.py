class Enviar:
    def __init__(self,**kwargs):
        for kwarg in kwargs:
            if kwarg=="cve_env":
                self.__cve_env = kwargs[kwarg]
            if kwarg=="fecha_env":
                self.__fecha_env = kwargs[kwarg]
            if kwarg=="ns_veh":
                self.__ns_veh = kwargs[kwarg]
            if kwarg=="folio_con":
                self.__folio_con = kwargs[kwarg]
    
    def setClaveEnv(self,cve_env):
        self.__cve_env=cve_env    
    def getClaveEnv(self):
        return self.__cve_env

    def setFechaEnv(self,fecha_env):
        self.__fecha_env=fecha_env  
    def getFechaEnv(self):
        return self.__fecha_env

    def setNumSerieVeh(self,ns_veh):
        self.__ns_veh=ns_veh  
    def getNumSerieVeh(self):
        return self.__ns_veh

    def setClaveCon(self,folio_con):
        self.__folio_con=folio_con    
    def getClaveCon(self):
        return self.__folio_con