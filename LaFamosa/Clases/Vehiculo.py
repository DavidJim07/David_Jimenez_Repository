class Vehiculo:
    def __init__(self,**kwargs):
        for kwarg in kwargs:
            if kwarg=="ns_veh":
                self.__ns_veh = kwargs[kwarg]
            if kwarg=="modelo_veh":
                self.__modelo_veh = kwargs[kwarg]
            if kwarg=="marca_veh":
                self.__marca_veh = kwargs[kwarg]
            if kwarg=="color_veh":
                self.__color_veh = kwargs[kwarg]
            if kwarg=="cantPuertas_veh":
                self.__cantPuertas_veh = kwargs[kwarg]
            if kwarg=="año_veh":
                self.__año_veh = kwargs[kwarg]
            if kwarg=="precioCompra_veh": 
                self.__precioCompra_veh = kwargs[kwarg]
            if kwarg=="tipo_veh":
                self.__tipo_veh = kwargs[kwarg]
            if kwarg=="cve_tie":
                self.__cve_tie = kwargs[kwarg]

    def setNumSerieVeh(self,ns_veh):
        self.__ns_veh=ns_veh  
    def getNumSerieVeh(self):
        return self.__ns_veh

    def setModeloVeh(self,modelo_veh):
        self.__modelo_veh=modelo_veh  
    def getModeloVeh(self):
        return self.__modelo_veh

    def setMarcaVeh(self,marca_veh):
        self.__marca_veh=marca_veh  
    def getMarcaVeh(self):
        return self.__marca_veh

    def setColorVeh(self,color_veh):
        self.__color_veh=color_veh  
    def getColorVeh(self):
        return self.__color_veh

    def setCantPuertasVeh(self,cantPuertas_veh):
        self.__cantPuertas_veh=cantPuertas_veh  
    def getCantPuertasVeh(self):
        return self.__cantPuertas_veh

    def setAñoVeh(self,año_veh):
        self.__año_veh=año_veh  
    def getAñoVeh(self):
        return self.__año_veh   

    def setPrecioCompraVeh(self,precioCompra_veh):
        self.__precioCompra_veh=precioCompra_veh  
    def getPrecioCompraVeh(self):
        return self.__precioCompra_veh

    def setTipoVeh(self,tipo_veh):
        self.__tipo_veh=tipo_veh  
    def getTipoVeh(self):
        return self.__tipo_veh 

    def setClaveTie(self,cve_tie):
        self.__cve_tie=cve_tie    
    def getClaveTie(self):
        return self.__cve_tie