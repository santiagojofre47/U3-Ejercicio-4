import csv
import numpy as np
from claseCalefactor import Calefactor
from claseCalefactorElectrico import CalefactorElectrico
from claseCalefactorGas import CalefactorGas

class ManejadorCalefactores:
    __dimension = None
    __incremento = None
    __indice = None
    __Calefactores = None

    def __init__(self, dimension = None, incremento = 5):
        self.__dimension = dimension
        self.__incremento = incremento
        self.__indice = 0
        self.__Calefactores = np.empty(self.__dimension,dtype=Calefactor)

    def agregarCalefactor(self, unCalefactor):
        if self.__indice == self.__dimension:
            self.__dimension+=self.__incremento
            self.__Calefactores.resize(self.__dimension)
        self.__Calefactores[self.__indice] = unCalefactor
        self.__indice+=1

    def cargarCalefactoresElectricos(self):
        archivo = open('calefactor-electrico.csv')
        reader = csv.reader(archivo,delimiter=',')
        for fila in reader:
            unCalefactorElectrico = CalefactorElectrico(fila[0],fila[1],float(fila[2]))
            self.agregarCalefactor(unCalefactorElectrico)
        archivo.close() 

    def cargarCalefactoresGas(self):
        archivo = open('calefactor-a-gas.csv')
        reader = csv.reader(archivo,delimiter = ',')
        for fila in reader:
            unCalefactorGas = CalefactorGas(fila[0],fila[1],fila[2],float(fila[3]))
            self.agregarCalefactor(unCalefactorGas)
        archivo.close()

    def obtenerModelo(self, calefactor):
        if isinstance(calefactor, Calefactor):
            return calefactor.getModelo()

    def obtenerMarca(self, calefactor):
        if isinstance(calefactor, Calefactor):
            return calefactor.getMarca()


    def mostrarCalefactoresGas(self):
        i = 0
        s = ''
        print('Lista de calefactores a gas:')
        while i < self.__indice:
            if isinstance(self.__Calefactores[i], CalefactorGas):
                s+= str(self.__Calefactores[i])+'\n'
                i+=1
            else:
                i+=1    
        print(s)           

    def mostrarCalefactoresElectricos(self):
        i = 0
        s = ''
        print('Lista de calefactores eléctricos:')
        while i < self.__indice:
            if isinstance(self.__Calefactores[i], CalefactorElectrico):
                s+= str(self.__Calefactores[i])+'\n'
                i+=1
            else:
                i+=1    
        print(s)      

    def getMinimoElectrico(self,costo,cantidad):
        minimo = 9999
        i = 0
        consumo = None
        while i < self.__indice:
            if isinstance(self.__Calefactores[i], CalefactorElectrico):
                consumo = self.__Calefactores[i].calcularConsumo(costo,cantidad)
                if consumo < minimo:
                    minimo = consumo
                    i+=1
                else:
                    i+=1
            else:
                i+=1
        return minimo

    def getMinimoGas(self,costo,cantidad):
        minimo = 999999
        i = 0
        consumo = None
        while i < self.__indice:
            if isinstance(self.__Calefactores[i], CalefactorGas):
                consumo = self.__Calefactores[i].calcularConsumo(costo,cantidad)
                if consumo < minimo:
                    minimo = consumo
                    i+=1
                else:
                    i+=1
            else:
                i+=1
        return minimo     

    def getCalefactorElectricoMenorConsumo(self, costo, cantidad):
        i = 0
        encontro = False
        minimo = None
        calefactor = None
        while i < self.__indice and not encontro:
            if isinstance(self.__Calefactores[i], CalefactorElectrico):
                minimo = self.getMinimoElectrico(costo, cantidad)
                if self.__Calefactores[i].calcularConsumo(costo, cantidad) == minimo:
                    calefactor = self.__Calefactores[i]
                    encontro = True
                else:
                    i+=1
            else:
                i+=1
        return calefactor        

    def getCalefactorGasMenorConsumo(self, costo, cantidad):
        i = 0
        encontro = False
        minimo = None
        calefactor = None
        while i < self.__indice and not encontro:
            if isinstance(self.__Calefactores[i], CalefactorGas):
                minimo = self.getMinimoGas(costo, cantidad)
                if self.__Calefactores[i].calcularConsumo(costo, cantidad) == minimo:
                    calefactor = self.__Calefactores[i]
                    encontro = True
                else:
                    i+=1
            else:
                i+=1
        return calefactor   

    def mostrarDatosMenorConsumo(self, uncalefactor):
        if isinstance(uncalefactor, CalefactorElectrico):
            print('Tipo de calefactor: Elecrico')
            print(uncalefactor)
        else:
            print('Tipo de calefactor: A gas')
            print(uncalefactor)














