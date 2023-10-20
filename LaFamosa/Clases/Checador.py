class Checador:
    def __init__(self,**kwargs):
        for kwarg in kwargs:
            if kwarg=="num_che":
                self.__num_che = kwargs[kwarg]
            if kwarg=="hora_che":
                self.__hora_che = kwargs[kwarg]
            if kwarg=="tipo_che":
                self.__tipo_che = kwargs[kwarg]
            if kwarg=="folio_con":
                self.__folio_con = kwargs[kwarg]

    def setNumChe(self,num_che):
        self.__num_che=num_che    
    def getNumChe(self):
        return self.__num_che

    def setHoraChe(self,hora_che):
        self.__hora_che=hora_che    
    def getHoraChe(self):
        return self.__hora_che

    def setTipoChe(self,tipo_che):
        self.__tipo_che=tipo_che    
    def getTipoChe(self):
        return self.__tipo_che

    def setClaveCon(self,folio_con):
        self.__folio_con=folio_con    
    def getClaveCon(self):
        return self.__folio_con