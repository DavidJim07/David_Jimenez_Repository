class StatusVehiculo:
    def __init__(self,**kwargs):
        for kwarg in kwargs:
            if kwarg=="num_sta":
                self.__num_sta = kwargs[kwarg]
            if kwarg=="fecha_sta":
                self.__fecha_sta = kwargs[kwarg]
            if kwarg=="status_sta":
                self.__status_sta = kwargs[kwarg]
            if kwarg=="ns_veh":
                self.__ns_veh = kwargs[kwarg]

    def setNumSta(self,num_sta):
        self.__num_sta=num_sta  
    def getNumSta(self):
        return self.__num_sta

    def setFechaSta(self,fecha_sta):
        self.__fecha_sta=fecha_sta  
    def getFechaSta(self):
        return self.__fecha_sta

    def setStatusSta(self,status_sta):
        self.__status_sta=status_sta  
    def getStatusSta(self):
        return self.__status_sta
    
    def setNumSerieVeh(self,ns_veh):
        self.__ns_veh=ns_veh  
    def getNumSerieVeh(self):
        return self.__ns_veh