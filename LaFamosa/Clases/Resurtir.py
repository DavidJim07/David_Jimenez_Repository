class Resurtir:
    def __init__(self,**kwargs):
        for kwarg in kwargs:
            if kwarg=="cve_res":
                self.__cve_res = kwargs[kwarg]
            if kwarg=="fecha_res":
                self.__fecha_res = kwargs[kwarg]
            if kwarg=="total_res":
                self.__total_res = kwargs[kwarg]
            if kwarg=="cve_prov":
                self.__cve_prov = kwargs[kwarg]
            if kwarg=="cve_tie":
                self.__cve_tie = kwargs[kwarg]

    def setClaveRes(self,cve_res):
        self.__cve_res=cve_res    
    def getClaveRes(self):
        return self.__cve_res

    def setFechaRes(self,fecha_res):
        self.__fecha_res=fecha_res    
    def getFechaRes(self):
        return self.__fecha_res

    def setTotalRes(self,total_res):
        self.__total_res=total_res    
    def getTotalRes(self):
        return self.__total_res

    def setClaveProv(self,cve_prov):
        self.__cve_prov=cve_prov    
    def getClaveProv(self):
        return self.__cve_prov

    def setClaveTie(self,cve_tie):
        self.__cve_tie=cve_tie    
    def getClaveTie(self):
        return self.__cve_tie