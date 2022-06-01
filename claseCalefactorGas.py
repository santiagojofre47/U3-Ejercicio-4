from claseCalefactor import Calefactor

class CalefactorGas(Calefactor):
    __matricula = None
    __calorias = None

    def __init__(self, modelo = None, marca = None, matricula = None, calorias = None):
        super().__init__(modelo, marca)
        self.__matricula = matricula
        self.__calorias = calorias

    def __str__(self):
        return 'Marca: {} Modelo: {} Matricula: {} Calorias: {}' .format(self.getMarca(),self.getModelo(),self.__matricula,self.__calorias) 

    def calcularConsumo(self, costo, cantidad):
        total = (self.__calorias/1000)*costo*cantidad
        return total   
   