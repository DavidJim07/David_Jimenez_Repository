class RenglonResurtir:
    def __init__(self,**kwargs):
        for kwarg in kwargs:
            if kwarg=="num_renres":
                self.__num_renres = kwargs[kwarg]
            if kwarg=="cantidad_renres":
                self.__cantidad_renres = kwargs[kwarg]
            if kwarg=="baja_renres":
                self.__baja_renres = kwargs[kwarg]
            if kwarg=="fCaducidad_renres":
                self.__fCaducidad_renres = kwargs[kwarg]
            if kwarg=="precio_renres":
                self.__precio_renres = kwargs[kwarg]
            if kwarg=="codbar_pro":
                self.__codbar_pro = kwargs[kwarg]
            if kwarg=="cve_res":
                self.__cve_res = kwargs[kwarg]

    def setNumRenRes(self,num_renres):
        self.__num_renres=num_renres    
    def getNumRenRes(self):
        return self.__num_renres

    def setCantidadRenRes(self,cantidad_renres):
        self.__cantidad_renres=cantidad_renres    
    def getCantidadRenRes(self):
        return self.__cantidad_renres

    def setBajaRenRes(self,baja_renres):
        self.__baja_renres=baja_renres    
    def getBajaRenRes(self):
        return self.__baja_renres

    def setfCaducidadRenREs(self,fCaducidad_renres):
        self.__fCaducidad_renres=fCaducidad_renres    
    def getfCaducidadRenREs(self):
        return self.__fCaducidad_renres

    def setPrecioRenRes(self,precio_renres):
        self.__precio_renres=precio_renres    
    def getPrecioRenRes(self):
        return self.__precio_renres
    
    def setCodbarPro(self,codbar_pro):
        self.__codbar_pro=codbar_pro    
    def getCodbarPro(self):
        return self.__codbar_pro
        
    def setClaveRes(self,cve_res):
        self.__cve_res=cve_res    
    def getClaveRes(self):
        return self.__cve_res

    