class Devolucion:
    def __init__(self,**kwargs):
        for kwarg in kwargs:
            if kwarg=="cve_dev":
                self.__cve_dev = kwargs[kwarg]
            if kwarg=="motivo_dev":
                self.__motivo_dev = kwargs[kwarg]
            if kwarg=="fecha_dev":
                self.__fecha_dev = kwargs[kwarg]
            if kwarg=="folio_tic":
                self.__folio_tic = kwargs[kwarg]

    def setClaveDev(self,cve_dev):
        self.__cve_dev=cve_dev    
    def getClaveDev(self):
        return self.__cve_dev

    def setMotivoDev(self,motivo_dev):
        self.__motivo_dev=motivo_dev  
    def getMotivoDev(self):
        return self.__motivo_dev

    def setFechaDev(self,fecha_dev):
        self.__fecha_dev=fecha_dev  
    def getFechaDev(self):
        return self.__fecha_dev

    def setFolioTic(self,folio_tic):
        self.__folio_tic=folio_tic    
    def getFolioTic(self):
        return self.__folio_tic