from claseCalefactor import Calefactor

class CalefactorElectrico(Calefactor):
    __potenciaMaxima = None

    def __init__(self, modelo  = None, marca = None, potenciaMaxima = None):
        super().__init__(modelo, marca)
        self.__potenciaMaxima = potenciaMaxima

    def __str__(self):
        return 'Modelo: {} Marca: {} Potencia Maxima: {} Watts' .format(self.getModelo(),self.getMarca(), self.__potenciaMaxima)    
    
    def calcularConsumo(self, costo, cantidad):
        total = (self.__potenciaMaxima/1000) * costo * cantidad
        return total       


