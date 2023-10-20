class Producto:
    def __init__(self,**kwargs):
        for kwarg in kwargs:
            if kwarg=="codbar_pro":
                self.__codbar_pro = kwargs[kwarg]
            if kwarg=="nom_pro":
                self.__nom_pro = kwargs[kwarg]
            if kwarg=="tipo_pro":
                self.__tipo_pro = kwargs[kwarg]
            if kwarg=="marca_pro":
                self.__marca_pro = kwargs[kwarg]
            if kwarg=="color_pro":
                self.__color_pro = kwargs[kwarg]
            if kwarg=="garantia_pro":
                self.__garantia_pro = kwargs[kwarg]
            if kwarg=="uMedidaGarantia_pro": 
                self.__uMedidaGarantia_pro = kwargs[kwarg]
            if kwarg=="presentacion_pro":
                self.__presentacion_pro = kwargs[kwarg]
            if kwarg=="modelo_pro":
                self.__modelo_pro = kwargs[kwarg]
            if kwarg=="alto_pro":
                self.__alto_pro = kwargs[kwarg]
            if kwarg=="largo_pro":
                self.__largo_pro = kwargs[kwarg]
            if kwarg=="ancho_pro":
                self.__ancho_pro = kwargs[kwarg]
            if kwarg=="contenido_pro":
                self.__contenido_pro = kwargs[kwarg]
            if kwarg=="uMedida_pro":
                self.__uMedida_pro = kwargs[kwarg]

    def setCodbarPro(self,codbar_pro):
        self.__codbar_pro=codbar_pro    
    def getCodbarPro(self):
        return self.__codbar_pro

    def setNomPro(self,nom_pro):
        self.__nom_pro=nom_pro  
    def getNomPro(self):
        return self.__nom_pro

    def setTipoPro(self,tipo_pro):
        self.__tipo_pro=tipo_pro  
    def getTipoPro(self):
        return self.__tipo_pro

    def setMarcaPro(self,marca_pro):
        self.__marca_pro=marca_pro  
    def getMarcaPro(self):
        return self.__marca_pro

    def setColorPro(self,color_pro):
        self.__color_pro=color_pro  
    def getColorPro(self):
        return self.__color_pro

    def setGarantiaPro(self,garantia_pro):
        self.__garantia_pro=garantia_pro  
    def getGarantiaPro(self):
        return self.__garantia_pro

    def setUmedidaGarantiaPro(self,uMedidaGarantia_pro):
        self.__uMedidaGarantia_pro=uMedidaGarantia_pro  
    def getUmedidaGarantiaPro(self):
        return self.__uMedidaGarantia_pro   

    def setPresentacionPro(self,presentacion_pro):
        self.__presentacion_pro=presentacion_pro  
    def getPresentacionPro(self):
        return self.__presentacion_pro

    def setModeloPro(self,modelo_pro):
        self.__modelo_pro=modelo_pro  
    def getModeloPro(self):
        return self.__modelo_pro 

    def setAltoPro(self,alto_pro):
        self.__alto_pro=alto_pro  
    def getAltoPro(self):
        return self.__alto_pro  

    def setLargoPro(self,largo_pro):
        self.__largo_pro=largo_pro  
    def getLargoPro(self):
        return self.__largo_pro

    def setAnchoPro(self,ancho_pro):
        self.__ancho_pro=ancho_pro  
    def getAnchoPro(self):
        return self.__ancho_pro

    def setContenidoPro(self,contenido_pro):
        self.__contenido_pro=contenido_pro  
    def getContenidoPro(self):
        return self.__contenido_pro

    def setUmedidaPro(self,uMedida_pro):
        self.__uMedida_pro=uMedida_pro  
    def getUmedidaPro(self):
        return self.__uMedida_pro  

    