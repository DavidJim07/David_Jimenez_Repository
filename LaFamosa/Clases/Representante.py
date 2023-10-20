class Representante:
    def __init__(self,**kwargs):
        for kwarg in kwargs:
            if kwarg=="num_rep":
                self.__num_rep = kwargs[kwarg]
            if kwarg=="fecha_rep":
                self.__fecha_rep = kwargs[kwarg]
            if kwarg=="cve_per":
                self.__cve_per = kwargs[kwarg]
            if kwarg=="cve_prov":
                self.__cve_prov = kwargs[kwarg]

    def setNumRep(self,num_rep):
        self.__num_rep=num_rep    
    def getNumRep(self):
        return self.__num_rep

    def setFechaRep(self,fecha_rep):
        self.__fecha_rep=fecha_rep    
    def getFechaRep(self):
        return self.__fecha_rep

    def setClavePer(self,cve_per):
        self.__cve_per=cve_per    
    def getClavePer(self):
        return self.__cve_per

    def setClaveProv(self,cve_prov):
        self.__cve_prov=cve_prov    
    def getClaveProv(self):
        return self.__cve_prov