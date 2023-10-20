class MinMax:
    def __init__(self,**kwargs):
        for kwarg in kwargs:
            if kwarg=="num_minmax":
                self.__num_minmax = kwargs[kwarg]
            if kwarg=="min_minmax":
                self.__min_minmax = kwargs[kwarg]
            if kwarg=="max_minmax":
                self.__max_minmax = kwargs[kwarg]
            if kwarg=="codbar_pro":
                self.__codbar_pro = kwargs[kwarg]
            if kwarg=="cve_tie":
                self.__cve_tie = kwargs[kwarg]

    def setNumMinMax(self,num_minmax):
        self.__num_minmax=num_minmax    
    def getNumMinMax(self):
        return self.__num_minmax

    def setMinMinMax(self,min_minmax):
        self.__min_minmax=min_minmax    
    def getMinMinMax(self):
        return self.__min_minmax

    def setMaxMinMax(self,max_minmax):
        self.__max_minmax=max_minmax    
    def getMaxMinMax(self):
        return self.__max_minmax

    def setClaveTie(self,cve_tie):
        self.__cve_tie=cve_tie    
    def getClaveTie(self):
        return self.__cve_tie

    def setCodbarPro(self,codbar_pro):
        self.__codbar_pro=codbar_pro    
    def getCodbarPro(self):
        return self.__codbar_pro                