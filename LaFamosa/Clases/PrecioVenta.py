class PrecioVenta:
    def __init__(self,**kwargs):
        for kwarg in kwargs:
            if kwarg=="cve_pre":
                self.__cve_pre = kwargs[kwarg]
            if kwarg=="fecha_pre":
                self.__fecha_pre = kwargs[kwarg]
            if kwarg=="precio_pre":
                self.__precio_pre = kwargs[kwarg]
            if kwarg=="codbar_pro":
                self.__codbar_pro = kwargs[kwarg]

    def setClavePre(self,cve_pre):
        self.__cve_pre=cve_pre    
    def getClavePre(self):
        return self.__cve_pre

    def setFechaPre(self,fecha_pre):
        self.__fecha_pre=fecha_pre  
    def getFechaPre(self):
        return self.__fecha_pre

    def setPrecioPre(self,precio_pre):
        self.__precio_pre=precio_pre  
    def getPrecioPre(self):
        return self.__precio_pre
    
    def setCodbarPro(self,codbar_pro):
        self.__codbar_pro=codbar_pro    
    def getCodbarPro(self):
        return self.__codbar_pro