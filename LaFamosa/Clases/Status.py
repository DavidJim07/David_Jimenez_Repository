class Status:
    def __init__(self,**kwargs):
        for kwarg in kwargs:
            if kwarg=="num_sta":
                self.__num_sta = kwargs[kwarg]
            if kwarg=="fecha_sta":
                self.__fecha_sta = kwargs[kwarg]
            if kwarg=="status_sta":
                self.__status_sta = kwargs[kwarg]
            if kwarg=="num_liscar":
                self.__num_liscar = kwargs[kwarg]

    def setNumStatus(self,num_sta):
        self.__num_sta=num_sta    
    def getNumStatus(self):
        return self.__num_sta

    def setFechaSta(self,fecha_sta):
        self.__fecha_sta=fecha_sta  
    def getFechaSta(self):
        return self.__fecha_sta

    def setStatusSta(self,status_sta):
        self.__status_sta=status_sta  
    def getStatusSta(self):
        return self.__status_sta
            
    def setNumLisCar(self,num_liscar):
        self.__num_liscar=num_liscar    
    def getNumLisCar(self):
        return self.__num_liscar