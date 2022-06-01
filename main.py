from manejadorCalefactores import ManejadorCalefactores
from claseMenu import Menu

if __name__ == '__main__':
    es_entero = False
    dimension = None
    while not es_entero:
        try:
            dimension = int(input('Ingrese la dimension del arreglo: '))
        except ValueError:
            print('ERROR: el dato ingresado no es un numero entero!')
        else:
            es_entero = True

    unManejadorCalefactor = ManejadorCalefactores(dimension)
    unManejadorCalefactor.cargarCalefactoresElectricos()
    unManejadorCalefactor.cargarCalefactoresGas()
    UnMenu = Menu()
    UnMenu.mostrarMenu(unManejadorCalefactor)


           
    
    