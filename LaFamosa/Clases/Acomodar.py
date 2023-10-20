class Acomodar:
    def __init__(self,**kwargs):
        for kwarg in kwargs:
            if kwarg=="cve_aco":
                self.__cve_aco = kwargs[kwarg]
            if kwarg=="fecha_aco":
                self.__fecha_aco = kwargs[kwarg]
            if kwarg=="cantidad_aco":
                self.__cantidad_aco = kwargs[kwarg]
            if kwarg=="lugar_aco":
                self.__lugar_aco = kwargs[kwarg]
            if kwarg=="num_renres":
                self.__num_renres = kwargs[kwarg]
            if kwarg=="cve_tie":
                self.__cve_tie = kwargs[kwarg]

    def setClaveAco(self,cve_aco):
        self.__cve_aco=cve_aco    
    def getClaveAco(self):
        return self.__cve_aco

    def setFechaAco(self,fecha_aco):
        self.__fecha_aco=fecha_aco  
    def getFechaAco(self):
        return self.__fecha_aco

    def setCantidadAco(self,cantidad_aco):
        self.__cantidad_aco=cantidad_aco  
    def getCantidadAco(self):
        return self.__cantidad_aco

    def setLugarAco(self,lugar_aco):
        self.__lugar_aco=lugar_aco  
    def getLugarAco(self):
        return self.__lugar_aco

    def setNumRenRes(self,num_renres):
        self.__num_renres=num_renres    
    def getNumRenRes(self):
        return self.__num_renres

    def setClaveTie(self,cve_tie):
        self.__cve_tie=cve_tie    
    def getClaveTie(self):
        return self.__cve_tie