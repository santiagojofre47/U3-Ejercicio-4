from manejadorCalefactores import ManejadorCalefactores

class Menu:
    __opcion = None

    def mostrarMenu(self, UnManejador):
        if isinstance(UnManejador, ManejadorCalefactores):
            calefactor_gas = None
            calefactor_electrico = None
            salir = False
            while not salir:
                print('1- Mostrar calefactor a gas de menor consumo')
                print('2- Mostrar calefactor electrico de menor consumo')
                print('3- Mostrar datos de los calefactores de menor consumo')
                print('4- Salir')
                self.__opcion = int(input('Ingrese una opcion: '))
                
                if self.__opcion == 1:
                    costo = float(input('Ingrese el costo por metro cubico: '))
                    cantidad = float(input('Ingrese la cantidad estimada a consumir: '))
                    calefactor_gas = UnManejador.getCalefactorGasMenorConsumo(costo,cantidad)
                    print('Modelo: {} Marca: {}' .format(UnManejador.obtenerModelo(calefactor_gas),UnManejador.obtenerMarca(calefactor_gas)))

                elif self.__opcion == 2:   
                    costo = float(input('Ingrese el costo por kw/h: '))
                    cantidad = float(input('Ingrese la cantidad estimada a consumir: '))
                    calefactor_electrico = UnManejador.getCalefactorElectricoMenorConsumo(costo, cantidad)
                    print('Modelo: {} Marca: {}' .format(UnManejador.obtenerModelo(calefactor_electrico),UnManejador.obtenerMarca(calefactor_electrico)))

                elif self.__opcion == 3:
                    UnManejador.mostrarDatosMenorConsumo(calefactor_gas)
                    UnManejador.mostrarDatosMenorConsumo(calefactor_electrico)

                elif self.__opcion == 4:
                    salir = True
                    print('Cerrando menu...')
                    
                else:
                    print('ERROR: Opcion ingresada incorrecta!')
                    input('Presione ENTER para continuar....')        

                   
