import abc
from abc import ABC

class Calefactor(ABC):
    __modelo = None
    __marca = None
    
    def __init__(self, modelo = None, marca = None):
        self.__modelo = modelo
        self.__marca = marca

    def getModelo(self):
        return self.__modelo

    def getMarca(self):
        return self.__marca

    @abc.abstractmethod    
    def calcularConsumo(self,costo,cantidad):
        pass
        


